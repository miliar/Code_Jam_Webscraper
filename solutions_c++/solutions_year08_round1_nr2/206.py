#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

int N,M;
int need[2005][2005];
int ns[2005];
int mark[2005];

void init(){
  int i,j,k,a,b;
  scanf("%d%d",&N,&M);
  memset(need,-1,sizeof(need));
  memset(mark,0,sizeof(mark));
  for (i=0;i<M;i++){
    scanf("%d",&k);
    ns[i]=k;
    for (j=0;j<k;j++){
      scanf("%d%d",&a,&b);
      a--;
      need[i][a]=b;
    }
    if (k==1 && b==1) mark[a]=1; 
  }
}

int solve(){
  int i,j,k;
  int changed=0;
  
  while (1){
    changed=0;
    for (i=0;i<N;i++)if(mark[i]){
      for (j=0;j<M;j++){
        if (need[j][i]==0){
          need[j][i]=-1;
          ns[j]--;
          if (ns[j]==0) return 0;
          if (ns[j]==1){
            for (k=0;k<N;k++) if (need[j][k]==1){
              mark[k]=1;
              changed=1;
              break;
            }
          }
        }
      }
    }
    if (changed==0) break;  
  }
  return 1;
}

int main(){
  int k,i,j;
  scanf("%d",&k);
  for (i=1;i<=k;i++){
    init();
    printf("Case #%d:",i);
    if (!solve()){
      printf(" IMPOSSIBLE\n");
      continue;
    }
    
    for (j=0;j<N;j++){
      printf(" %d",mark[j]);
    }
    printf("\n");
  }
  return 0;
}

