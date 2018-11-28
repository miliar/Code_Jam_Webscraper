#include<cstdio>
#include<queue>
#include<vector>
#include<utility>
using namespace std;
typedef pair<int,int> PII;
priority_queue<PII,vector<PII>,greater<PII> > pq;

int arr[4] = {-1,0,0,1};
int arc[4] = {0,-1,1,0};
int map[200][200],hash[200][200];
int nbasin,pbasin;
int r,c;

bool valid (int ri, int ci){
  if ((ri < 1) || (ci < 1) || (ri > r) || (ci > c))return false;
  return true;
}

void dfs (int ri, int ci){     
     if (hash[ri][ci] != -1) {pbasin = hash[ri][ci]; return; }

     while (!pq.empty()) pq.pop();
     for (int i = 0; i < 4; i++){
         if (!valid(arr[i]+ri,arc[i]+ci))continue;
         if (map[arr[i]+ri][arc[i]+ci] >= map[ri][ci]) continue;
         pq.push(make_pair(map[arr[i]+ri][arc[i]+ci],i));
     }
     if (pq.empty()){
                     nbasin++; pbasin = nbasin; hash[ri][ci] = pbasin; return;
     }
     int temp = (pq.top()).second;
     dfs(arr[temp]+ri,arc[temp]+ci);
     hash[ri][ci] = pbasin;
}


int main(){
int tc;
 scanf("%d",&tc);
 for (int ti = 1; ti <= tc; ti++){
  scanf("%d %d",&r, &c);
  for (int i = 1; i <= r; i++){
      for (int j = 1; j <= c; j++){
          scanf("%d",&map[i][j]);    
      }    
  }   
  memset(hash,-1,sizeof(hash));
  nbasin = 0;
  for (int i = 1; i <= r; i++){
      for (int j = 1; j <= c; j++){
              if (hash[i][j] != -1) continue;

              dfs(i,j);

      }    
  }
  printf("Case #%d:\n",ti);
  for (int i = 1; i <= r; i++){
      for (int j = 1; j <= c; j++){
          if (j != 1) printf(" ");
          printf("%c",hash[i][j]-1+'a');    
      }    
      printf("\n");
  }
 }
}
