#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <string>
#include <map>
#include <vector>

using namespace std;


long test, i, t, m[3][300][300],l,sz[200],size, n, cnt, cnt2, a,b,c,d,k,j,X1,Y1;

int main()
{
    freopen("c-small.in","r",stdin);
    freopen("c-small.out","w",stdout);
    
    
    scanf("%d",&t);
    for (test = 1; test <= t; test ++ )
    {
        X1 = 200; Y1 = 200;
        scanf("%d",&n);
        printf("Case #%d: ", test);
                memset(m,0,sizeof(m));
 
        for (l=0; l<n; l++)
        {
            scanf("%d%d%d%d",&a,&b,&c,&d);
            
            for (k=a; k<=c; k++)
             for (j=b; j<=d; j++)
             {  m[0][j][k] = 1; cnt++; }
        }
       i=0;
        long step = 0;
        while (cnt)
        {
              step ++;
              cnt2 = 0;
              for (l=0; l<=X1; l++)
               for (k=0; k<=Y1; k++)
                if (m[i][l][k]==1)
                {
                    if (m[i][l-1][k]==0 && m[i][l][k-1]==0) m[1-i][l][k] = 0; else { m[1-i][l][k] = 1; cnt2++; }             
                } else
                {
                    if (m[i][l-1][k]==1 && m[i][l][k-1]==1) { m[1-i][l][k] = 1; cnt2++; } else m[1-i][l][k] = 0;
                }
               
               i^=1;
               cnt = cnt2;
        }
        
        printf("%d\n",step);
    }
    return 0;
}
