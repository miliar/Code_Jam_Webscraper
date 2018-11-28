#include<cstdio>
#include<string.h>
using namespace std;
#define maxn 110
struct Edge
{
       long x,w,a,b;
}s[maxn];
long n,m,i,j,tst=1,tt;
long a,b,ans;
char c[1];
long abs(long x)
{
     if (x<0) return -x;
     return x;
}
int main()
{
    for (scanf("%ld",&tt);tst<=tt;tst++)
    {
        scanf("%ld",&n);
        a=1;b=1;ans=0;
        for (i=0;i<n;i++)
        {
            scanf("%s%ld",c,&m);
            if (c[0]=='O') s[i].x=1;
               else s[i].x=2;
            s[i].w=m;
        }
        s[n].x=s[n].w=s[n].a=s[n].b=0;
        for (i=n-1;i>=0;i--)
        {
            if (s[i].x==s[i+1].x)
            {
               s[i].a=s[i+1].a;
               s[i].b=s[i+1].b;
               if (s[i].x==1) s[i].a=s[i].w;
                  else s[i].b=s[i].w;
            }
            else
            {
               if (s[i].x==1)
               {
                  s[i].a=s[i].w;
                  s[i].b=s[i+1].w;
               }
               else
               {
                  s[i].b=s[i].w;
                  s[i].a=s[i+1].w;
               }
            }
        }
        for (i=0;i<n;i++)
        {
            if (s[i].x==1)
            {
               j=abs(s[i].w-a)+1;
               a=s[i].w;
               ans+=j;
               if (s[i].b>b)
               {
                  if (s[i].b-b>j) b+=j;
                     else b=s[i].b;
               }
               else
               {
                  if (b-s[i].b>j) b-=j;
                     else b=s[i].b;
               }
            }
            else
            {
               j=abs(s[i].w-b)+1;
               b=s[i].w;
               ans+=j;
               if (s[i].a>a)
               {
                  if (s[i].a-a>j) a+=j;
                     else a=s[i].a;
               }
               else
               {
                  if (a-s[i].a>j) a-=j;
                     else a=s[i].a;
               }
            }
        }
        printf("Case #%ld: %ld\n",tst,ans);
    }
    return 0;
}
