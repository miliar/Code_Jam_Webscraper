#include<cstdio>
#include<cstring>
#define LL long long
int r,k,n;
int tc;
int next[1005],jum[1005],ar[1005];


int main(){
 scanf("%d",&tc);
 for (int ti = 1; ti <= tc; ti++){
     memset(next,0,sizeof(next));
     memset(jum,0,sizeof(jum));
     scanf("%d %d %d",&r,&k,&n);
     for (int i = 1; i <= n; i++){
         scanf("%d",&ar[i]);    
     }    
     for (int i = 1; i <= n; i++){
         int now = i; 

         while(true){
              jum[i] += ar[now];
              if (jum[i] > k){
                 jum[i] = jum[i]-ar[now];    
                 next[i] = now;   
                 break;
              }
              now++;

              if (now > n) now = 1;
              if (now == i){
                 next[i] = i; break;        
              }              
         }    

     }
     LL price = 0LL;
     int now = 1;
     for (int i = 1; i <= r; i++){
         price += (LL)jum[now];
         now = next[now];
     }
     printf("Case #%d: %I64d\n",ti,price);
 }   
}
