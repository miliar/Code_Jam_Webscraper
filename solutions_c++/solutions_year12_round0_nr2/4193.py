#include <stdio.h>
#include <algorithm>
using namespace std;

int a[105];
int sup[50];
int nsup[50];

bool cmp(int x,int y)
{
    return x<y;
}

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int i,j,n,T,ans,p,s,t,cnt=1;
    for (i=0;i<=30;i++)
    {
        sup[i]=(i+4)/3;
        nsup[i]=(i+2)/3;
    }
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        scanf("%d%d",&s,&p);
        for (i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
        }
        sort(a,a+n,cmp);
        t=0;
        ans=0;
        for (i=0;i<n;i++)
        {
            if (a[i]<2)
            {
                if (nsup[a[i]]>=p) ans++;
                continue;
            }
            if (a[i]>28)
            {
                ans++;
                continue;
            }
            if (sup[a[i]]<p) continue;
            if (nsup[a[i]]<p && t<s)
            {
                t++;
                ans++;
            }
            else if (nsup[a[i]]>=p) ans++;
        }
        printf("Case #%d: %d\n",cnt++,ans);
    }
    return 0;
}
