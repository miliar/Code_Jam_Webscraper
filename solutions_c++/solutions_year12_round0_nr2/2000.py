#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <math.h>
#include <iostream>
#include <string>
using namespace std;
int n,s,p;
int a[1100];
int main()
{
    int t;
   //freopen("in.in","r",stdin);
    //freopen("out.out","w",stdout);
    scanf("%d",&t);
    int num=0;
    while (t--)
    {
          int i;
          scanf("%d%d%d",&n,&s,&p);
          for (i=0;i<n;i++)
          scanf("%d",&a[i]);
          int ans=0;
          for (i=0;i<n;i++)
          {
              int sc=a[i]/3;
              if (a[i]%3!=0)
              sc++;
              if (sc>=p)
              {
                 ans++;
                 continue;
              }
              else if (s>0)
              {
                   
                   int r=max(2,p);
                   if (a[i]-3*r+4>=0)
                   {
                                 s--;
                                 ans++;
                   }
              }
          }
          printf("Case #%d: ",++num);
          printf("%d\n",ans);
    }
}
                    
          
