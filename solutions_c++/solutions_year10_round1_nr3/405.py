#include "stdio.h"
#include "math.h"
#include "string.h"

int a1,a2,b1,b2;

bool game(int const &a,int const &b){
   if(b>a)return game(b,a);
   if(a==b)return false;
   if(a/b>1)return true;
   else return !game(b,a%b);
}

int main(void){
   freopen("num2.in","r",stdin);
   freopen("num2.out","w",stdout);
   int T;
   int count;
   scanf("%d",&T);
   for(int t=0;t<T;t++){
      count=0;
      scanf("%d %d %d %d",&a1,&a2,&b1,&b2);
      for(int i=a1;i<=a2;i++){
         for(int j=b1;j<=b2;j++){
            if(game(i,j)){
               count++;
               //printf("i=%d j=%d\n",i,j);
            }
         }
      }
      printf("Case #%d: %d\n",t+1,count);
   }
   return 0;
}
