#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

int A,N,M;
int a,b,c,d;

void init(){
  scanf("%d%d%d",&N,&M,&A);
}

int solveCD(int t){
  int tt;
  if (t==0){
    c=d=0;
    return 1;
  }
  tt=sqrt(t)+1;
  if (tt>t) tt=t;
  if (tt>N) tt=N;
  for (c=1;c<=tt;c++){
    if (t%c==0){
      d=t/c;
      if (d<=M) return 1;
    }
  }
  return 0;
}

int solveAB(){
  int t;
  for (a=0;a<=N;a++){
    for (b=0;b<=M;b++) if(a*b>=A){
      t=a*b-A;
      //printf("t=%d\n",t);
      if (solveCD(t)) return 1;
    }
  }
  return 0;
}

int main(){
  int C,i;
  scanf("%d",&C);
  for (i=1;i<=C;i++){
    printf("Case #%d: ",i);
    init();
    if (solveAB()){
      printf("0 0 %d %d %d %d\n",a,d,c,b);
    }else{
      printf("IMPOSSIBLE\n");
    }
  }
  return 0;
}

