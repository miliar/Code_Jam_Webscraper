#include<iostream>
#include<cstdio>
#include<cmath>
#include<string.h>
#include<string>
using namespace std;

int T,i,a[1000],ans,t,n,s,p;

int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    scanf("%d",&T);
    for (int tt=1;tt<=T;tt++)
    {
        scanf("%d%d%d",&n,&s,&p);
        ans=0;
        for (i=1;i<=n;i++) scanf("%d",&a[i]);
        sort(a+1,a+1+n);
        for (i=n;i>=1;i--)
        {
            t=a[i]%3;
            if (t==0)
            {
                     if (a[i]/3>=p)
                     {
                        ans++; continue;
                     }
                     if (s>0&&a[i]/3+1>=p&&a[i]/3-1>=0)
                     {
                        ans++; s--;
                        continue;
                     }
            }
            if (t==1)
            {
                     if (a[i]/3+1>=p) ans++;
                     continue;
            }
            if (t==2)
            {
                     if (a[i]/3+1>=p)
                     {
                        ans++; continue;
                     }
                     if (s>0&&(a[i]+4)/3>=p&&(a[i]-2)/3>=0)
                     {
                        ans++; s--;
                        continue;
                     }
            }
        }
        printf("Case #%d: %d\n",tt,ans);
    }
    return 0;
}
