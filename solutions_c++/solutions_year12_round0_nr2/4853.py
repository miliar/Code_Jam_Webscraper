#include<stdio.h>
#define min(X,Y) ((X) < (Y) ? (X) : (Y))

int main ( void ){
  int t;
  scanf("%d\n",&t);
  for (int i=0; i<t; ++i){
    int n,s,p;
    scanf("%d%d%d",&n,&s,&p);
    int a=0,b=0;
    for (int j=0; j<n; ++j){
      int x;
      scanf("%d",&x); 
      if (x>=3*p-2) a++;
      else if ((x>=3*p-4)&&(p>1)) b++;  
    }
    printf("Case #%d: %d\n",i+1,a+min(b,s));
  }
  return 0;
}