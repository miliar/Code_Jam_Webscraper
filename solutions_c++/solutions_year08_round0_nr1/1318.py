#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

char name[105][200];
int quer[1005];
int S,Q;

int findInd(char *st){
  int i;
  for (i=0;i<S;i++) if (strcmp(name[i],st)==0) return i;
  printf("Error!\n");
  return -99999999;
}

void init(){
  int i;
  char st[200];
  scanf("%d\n",&S);
  for (i=0;i<S;i++){
    gets(name[i]);
    /*printf("i=%d %s\n",i,name[i]);*/
  }
  scanf("%d\n",&Q);
  for (i=0;i<Q;i++){
    gets(st);
    quer[i]=findInd(st);
    /*printf("i=%d %s %d\n",i,st,quer[i]);*/
  }
}

int findOne(int k){
  int i,t=0;
  char flag[200];
  for (i=0;i<S;i++) flag[i]=0;
  for (i=k;i<Q;i++){
    if (flag[quer[i]]==0){
      flag[quer[i]]=1;
      t++;
    }
    if (t==S-1) break;
  }
  for (i=0;i<S;i++) if(flag[i]==0) return i;
  printf("Error on findOne!\n");
  return -999999999;
}

int solve(){
  int res=0;
  int k=0,t;
  while (k<Q){
    res++;
    t=findOne(k);
    /*printf("t=%d\n",t);*/
    while (k<Q && quer[k]!=t) k++;
  }
  if (Q==0) return 1;
  return res;
}

int main(){
  int n,i;
  scanf("%d",&n);
  for (i=1;i<=n;i++){
    init();
    printf("Case #%d: %d\n",i,solve()-1);
  }
  return 0;
}

