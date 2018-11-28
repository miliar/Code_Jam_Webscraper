#include <stdio.h>
#include <iostream>
#include <algorithm>
#define maxlong 2000000000

long boo,ans, t, test, DP[500][500], D, I, M, n, k, j, l, m[500];


long min(long a, long b)
{
 if (a<b) return a; else return b;
}

int main()
{
    freopen("b-small.in","r",stdin);
    freopen("b-large.out","w",stdout);
    scanf("%d",&t);
    for (test = 1; test<=t; test++)
    {
        printf("Case #%d: ",test);
        scanf("%d%d%d%d",&D,&I,&M,&n);
        for (l=0; l<n; l++) scanf("%d",&m[l]);
        
        for (l=0; l<=n; l++)
         for (k=0; k<302; k++) DP[l][k] = maxlong;
        
 
        for (l=0; l<300; l++) DP[1][l] = abs(m[0]-l);
        for (l=0; l<300; l++) DP[0][l] = I;
        DP[1][300] = D;
        
        for (l=0; l<n; l+=boo)
        {
            boo = 1;
          for (k=0; k<=300; k++)
          if (DP[l][k]!=maxlong)
          {
          
          
           for (j=299; j>=0; j--)
           {
            if (abs(j-k)<=M  || k==300) DP[l+1][j] =  min(DP[l+1][j], DP[l][k] + abs(m[l]-j) );            
            if (abs(j-k)<=M || k==300) 
            {
             if (j<k && DP[l][j]>DP[l][k]+I) boo = 0;
             DP[l][j] = min(DP[l][j], DP[l][k] + I);
            }
            
           } 
           DP[l+1][k] = min(DP[l+1][k], DP[l][k] + D);               
                    
          }
        }
        ans = maxlong;
        for (l=0; l<301; l++)
         if (DP[n][l]<ans) ans = DP[n][l];
        
    
        printf("%d\n",ans);
    }
    
    return 0;
}
