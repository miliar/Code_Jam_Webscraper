#include<cstdio>
int tc,n,k,walk;
int main(){
 scanf("%d",&tc);
 for (int ti = 1; ti <= tc; ti++){
      scanf("%d %d",&n,&k);

      if ((k % (1<<n)) == ((1<<n) -1)){
         printf("Case #%d: ON\n",ti);       
      } else{
         printf("Case #%d: OFF\n",ti);       
      }
 }   
}

/*      int a = 0;
      int walk = 0;
      while(a != ((1<<n)-1)){
         printf("%d %d\n",walk,a);
         int b = a;
         for (int i = 0; i < n; i++){
             if ((a & (1<< i)) == 0){
                b = b + (1<<i);       
             } else{
                b = b - (1<<i);       
             }
             if ((a & (1<< i)) == 0) //berarti 0, atau off
                break;
         }     
         a = b;
         walk++;
      }            */
