#include<iostream>
#include<string.h>
#include<stdio.h>
#include<algorithm>
using namespace std;
int gcd(int a,int b)
{
    if (b==0) return a;
    return gcd(b,a%b);
}
int main()
{
    int cas,t=0,n,a,b,c;
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&cas);
    while (cas--)
    {
          scanf("%d",&n);
          if (n==2)
          {
             scanf("%d%d",&a,&b);
             int tt=max(a,b)-min(a,b);
             int y;
             if (a%tt==0)
             y=0;
             else y=tt-a%tt;
             printf("Case #%d: %d\n",++t,y);
          }
          else
          {
              scanf("%d%d%d",&a,&b,&c);
              int tt=gcd(max(a,b)-min(a,b),max(a,c)-min(a,c));
              int y;
              if (a%tt==0)
              y=0;
              else 
              y=tt-a%tt;
              printf("Case #%d: %d\n",++t,y);
          }
    }
}
