#include "stdio.h"

int n , k;
__int64 s;
void solve()
{
     __int64 temp = 1;
     for(int i = 1 ; i < n;i++)
     {
         temp = 2*temp;
         s += temp;
     }
}    
int main()
{
     freopen("A-large.in","r",stdin);
     freopen("A-large.out","w",stdout);
     int test , t = 0;
     scanf("%d",&test);
     while(test--)
     {
        
         s = 2;
         scanf("%d%d",&n,&k);
         solve();
         k++; t++;
       //  printf("%d\n",s);
         if(k % s == 0 && k >= s)
             printf("Case #%d: ON\n",t);
         else
             printf("Case #%d: OFF\n",t);   
     }
    // while(1);
     return 0;
}
     
