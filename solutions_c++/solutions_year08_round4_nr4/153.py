#include <cstdio>
#include <cstring>

using namespace std;

int flag[20];
int P[20];
int L;
char str[100000];
char tmp[100000];
int ans;

void init(){
  scanf("%d%s",&L,str);
  ans=0x7fffffff;
  memset(flag,0,sizeof(flag));
}

int getSize(){
  int i,t,j;
  int res=0;
  t=strlen(str);
  for (i=0;i<t;i+=L){
    for (j=0;j<L;j++){
      tmp[i+j]=str[i+P[j]];
    }
  }
  
  res=1;
  for (i=1;i<t;i++){
    if (tmp[i]!=tmp[i-1]) res++;
  }
  return res;
}

void DFS(int k){
  int i,t;
  if (k==L){
    //for (i=0;i<L;i++) printf("%d",P[i]); printf("\n");
    t=getSize();
    if (t<ans){
      ans=t;
    }
    return;
  }
  for (i=0;i<L;i++) if(flag[i]==0){
    P[k]=i;
    flag[i]=1;
    DFS(k+1);
    flag[i]=0;
  }
}

int main(){
  int N,i;
  scanf("%d",&N);
  for (i=1;i<=N;i++){
    printf("Case #%d: ",i);
    init();
    DFS(0);
    printf("%d\n",ans);
  }
  return 0;
}

