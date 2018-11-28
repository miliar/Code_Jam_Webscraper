#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <stack>
#include <string>
#include <map>
using namespace std;
int w[1200];


int main()
{
    int t,cas,n,l,h;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    scanf("%d",&t);
    cas=0;
    while(t--)
    {
       scanf("%d%d%d",&n,&l,&h);
       for(int i=0;i<n;i++)
          scanf("%d",&w[i]);
       bool flag=false;
       int re;
       for(int i=l;i<=h;i++)
       {
           int j;
           for(j=0;j<n;j++)
           {
               if(w[j]%i==0||i%w[j]==0)
                  continue;
                else
                  break;
           }
           if(j==n)
             {
                 flag=true;
                 re=i;
                 break;
             }
       }
       printf("Case #%d: ",++cas);
       if(!flag)
         printf("NO\n");
        else
          printf("%d\n",re);
    }
    return 0;

}
