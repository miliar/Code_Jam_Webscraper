#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int list[100];
int rearrange[100];
int n;

void init(){
  int i,j,k;
  char t;
  char tmp[100];
  scanf("%d",&n);
  for (i=0;i<n;i++){
    k=0;
    gets(tmp);
    for (j=0;j<n;j++){
      scanf("%c",&t);
      if (t=='1') k=j;
    }
    list[i]=k+1;
  }
}

int solve(){
  int i,j;
  int res;
  memset(rearrange,-1,sizeof(rearrange));
  //printf("n=%d\n",n);
  for (i=1;i<=n;i++){
    for (j=0;j<n;j++){
      if (list[j]<=i && rearrange[j]==-1){
        rearrange[j]=i;
        break;
      }
    }
  }
  
  /*for (i=0;i<n;i++) printf("%d ",list[i]); printf("\n");
  for (i=0;i<n;i++) printf("%d ",rearrange[i]);*/
  res=0;
  for (i=0;i<n;i++){
    for (j=i+1;j<n;j++){
      if (rearrange[j]<rearrange[i]) res++;
    }
  }
  return res;
}

int main(){
  int t,k=0;
  scanf("%d",&t);
  while (t--){
    k++;
    printf("Case #%d: ",k);
    init();
    printf("%d\n",solve());
  }
  return 0;
}

