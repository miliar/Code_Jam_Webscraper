#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

int L,D,N;
char words[5005][20];

void init(){
  int i;
  scanf("%d%d%d",&L,&D,&N);
  for (i=0;i<D;i++) scanf("%s",words[i]);
}

int solve(char *st){
  int i,l,j,tl;
  char list[20][2000],*tmp;
  int k=0,res=0;
  
  l=strlen(st);
  for (i=0;i<l;i++){
    if (st[i]=='('){
      tmp=st+i+1;
      for (;i<l;i++) if(st[i]==')') break;
      st[i]=0;
      strcpy(list[k],tmp);
      k++;
      continue;
    }
    list[k][0]=st[i];
    list[k][1]=0;
    k++;
  }
  if (k!=L) return 0;
  
  for (i=0;i<D;i++){
    for (j=0;j<L;j++){
      tl=strlen(list[j]);
      for (k=0;k<tl;k++){
        if (list[j][k]==words[i][j]) break;
      }
      if (k==tl) break;
    }
    if (j==L) res++;
  }
  return res;
}

int main(){
  int i;
  char st[100000];
  init();
  for (i=0;i<N;i++){
    scanf("%s",st);
    printf("Case #%d: %d\n",i+1,solve(st));
  }
  return 0;
}

