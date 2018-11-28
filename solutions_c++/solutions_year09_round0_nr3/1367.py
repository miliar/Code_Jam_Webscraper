#include<cstdio>
#include<cstring>
#define REP(i,n) for(int i=0;i<(int)(n);++i)
char *p="welcome to code jam";
char q[1000];
int h[100];
int h2[100];
int main(){
  int n;
  scanf("%d ",&n);

  int m=strlen(p);
  REP(X,n) {
    gets(q);
    REP(i,m+1) h[i]=0;
    h[0]=1; 
    for(int i=0;q[i];++i) {
      REP(j,m+1) h2[j]=h[j];
      REP(j,m+1) if(p[j]==q[i]) h2[j+1]+=h[j];
      REP(j,m+1) h[j]=h2[j] % 10000;
    }
    printf("Case #%d: %04d\n",X+1,h[m]);
  }
  
}
