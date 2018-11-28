#include<stdio.h>
#include<stdlib.h>


int T, N, l;
int candy[1005];
int bit[20];

void solve()
{
     scanf("%d", &N);
     for(int i = 0; i < 20; ++i)
         bit[i] = 0;
     int min = 10000000;  
     int sum = 0;
     for(int i = 0; i < N; ++i) {
          scanf("%d", &candy[i]);
          sum += candy[i];
          if(candy[i] < min) {
               min = candy[i];       
          }
          int price = candy[i];
          for(int j = 0; j < 20 && price > 0; ++j)  {
               bit[j] += price%2;
               price/=2;
          }  
     }
     
     for(int i = 0; i < 20; ++i) {
           if(bit[i] % 2 != 0) {
               printf("Case #%d: NO\n",l);
               return;  
           }
     }
     
     
     printf("Case #%d: %d\n", l, sum-min);
   
}
     
int main()
{    
     freopen("C-large.in","r",stdin);
     freopen("C-large.out","w",stdout);
     scanf("%d", &T);
     for(l = 1; l <= T; ++l) {
          solve();        
     }
     
     //system("pause");
     return 0;
}
