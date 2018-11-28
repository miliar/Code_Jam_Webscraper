#include <stdio.h>
#include <math.h>
#include <iostream>
#include <memory.h>
using namespace std;
int tests,n,x,y;
                    int t[10];
bool fl;
int v[110][110];

int check(int c,int d)
{
    if (c>=n*2||d>=n*2) return -1;
    if (c<1||d<1) return -1;
    return v[c][d]; 
}
int max(int a,int b,int c,int d)
{
    if (a>=b&&a>=c&&a>=d) return a;
    if (b>=c&&b>=d) return b;
    if (c>=d) return c;
    return d;
}
int main()
{
    freopen("alarge.in","r",stdin);
    freopen("alarge.out","w",stdout);
    scanf("%d",&tests);
    for (int t0=1;t0<=tests;t0++)
    {
        scanf("%d",&n);
        memset(v,-1,sizeof(v));
        for (int i=1;i<=n*2-1;i++)
        {
            if (i<=n) x=n-i+1,y=n+i-1; else x=i-n+1,y=n*3-i-1;
            
            for (int j=x;j<=y;j+=2) scanf("%d",&v[i][j]);
        }
        int ans=100000;
        for (int i=1;i<=n*2-1;i++)
          for (int j=1;j<=n*2-1;j++)
          {           
                fl=true;     
            for (int k=1;k<=n*2-1;k++)
              for (int l=1;l<=n*2-1;l++)
              {

                 t[0]=check(k,l);
                 t[1]=check(k,2*j-l);
                 t[2]=check(2*i-k,l);
                 t[3]=check(2*i-k,2*j-l);
                 for (x=0;x<4;x++)
                   for (y=x+1;y<4;y++)
                     if (t[x]!=-1&&t[y]!=-1&&t[x]!=t[y]) fl=false;
                if (!fl) break;
              }
            if (fl)
            {
                int tmp=abs(n-i)+abs(n-j)+n;
                if (tmp<ans) ans=tmp;
            }
          }
          printf("Case #%d: %d\n",t0,ans*ans-n*n);
    }
}


