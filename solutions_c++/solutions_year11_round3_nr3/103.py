#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>
#include <cstring>
#include <queue>
#include <map>
#include <set>
#define u 10000000
using namespace std;

int t,i,C,l,k,a,ind,L,H,N,m[u],boo;

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    
    scanf("%d",&t);
    for (i = 1; i <= t; i++)
    {
          scanf("%d%d%d",&N,&L,&H);
          for (l=0; l<N; l++) scanf("%d",&m[l]);
       
          for (l=L; l<=H; l++)
          {
                   boo = 1;
                for (k=0; k<N; k++)
                    if (l%m[k]==0 || m[k]%l==0) continue; else { boo=0; break; }
                if (boo) break;
          }
          printf("Case #%d: ",i); 
          if (!boo) puts("NO"); else printf("%d\n",l);
    }
    
    
    return 0;
}
