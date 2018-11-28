#include <cstdio>
#include <string>
using namespace std;

int T;
int N;
int K;
int mat[200][200];
bool adj[200][200];
int deg[200];
int color[200];
int used[200][200];
int ucolor[200];
int mcount;
int target;
int limit;
int colors;
bool done;

void printvec(int r){
  for(int i = 0; i < K; i++){
    if(i) putchar(' ');
    printf("%d",mat[r][i]);
  }
  putchar('\n');
}

bool intersect(int r1, int r2){
  if(mat[r1][0]==mat[r2][0]) return true;
  int up = mat[r1][0] > mat[r2][0] ? 1 : 2;
  for(int i = 1; i < K; i++){
    if(up==1){
      if(mat[r1][i] <= mat[r2][i] ) return true;
    }else{
      if(mat[r2][i] <= mat[r1][i] ) return true;
    }
  }
  return false;
}

void go(int p){
  if(!limit) return;
  limit--;
  //if(mcount==target) return;
  if(p==N){
    done = true;
    return;
    /*limit--;
    int count = 0;
    for(int i = 0; i <= N; i++){
      if(ucolor[i]) count++;
    }
    mcount = min(count,mcount);
    //printf("count: %d\n",count);*/
  }
  else {
    for(int i = 0; i < colors; i++){
      if(!used[p][i]){
        ucolor[i]++;
        for(int k = 0; k < N; k++){
          if(adj[p][k]) used[k][i]++;
        }
        go(p+1);
        for(int k = 0; k < N; k++){
          if(adj[p][k]) used[k][i]--;
        }
        ucolor[i]--;
      }
    }
  }
}

int solve(){
  // printvec(0);
  //printvec(1);
  int res = 0;
  for(int i = 0; i < N; i++){
    deg[i] = 0;
    for(int k = 0; k < N; k++){
      if(k==i) continue;
      adj[i][k] = intersect(i,k);
      //printf("intersect(%d,%d) = %d\n",i,k,adj[i][k]);
      deg[i] += adj[i][k];
    }
  }
  for(int i = 0; i < N; i++){
    res = max(res,deg[i]);
  }
  memset(used,0,sizeof(used));
  memset(ucolor,0,sizeof(ucolor));
  mcount = N+1;
  target = res+1;
  done = false;
  for(colors = 1; ; colors++){
    limit = 1000000;
    go(0);
    //if(mcount==colors) break;
    if(done) break;
  }
  //printf("%d %d\n",colors,res+1);
  //return res+1;
  return colors;
}

int main(){
  scanf("%d",&T);
  for(int i = 1; i <= T; i++){
    scanf("%d%d",&N,&K);
    for(int n = 0; n < N; n++){
      for(int k = 0; k < K; k++){
        scanf("%d",&mat[n][k]);
      }
    }
    printf("Case #%d: %d\n",i,solve());
  }
  return 0;
}
