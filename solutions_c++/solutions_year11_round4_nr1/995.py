#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

int tt,x,s,r,n;
double t;
int a[200200][3];
int na[200200][3];
int lab[200200];
double ans;

bool cmp(int x,int y)
{
    return a[x][0]<a[y][0];
}

bool cmp2(int x,int y)
{
    return na[x][2]<na[y][2];
}

int main()
{
    freopen("al.in","r",stdin);
    freopen("al.out","w",stdout);
    scanf("%d",&tt);
    for (int ii=1;ii<=tt;ii++)
    {
        ans=0;
        scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
        for (int i=1;i<=n;i++)
        {
            scanf("%d%d%d",a[i],a[i]+1,a[i]+2);
            lab[i]=i;
        }
        sort(lab+1,lab+n+1,cmp);
        int ss=0;
        int now=0;
        for (int i=1;i<=n;i++)
        {
            if (a[lab[i]][0]>now)
            {
                na[++ss][0]=now;
                na[ss][1]=a[lab[i]][0];
                na[ss][2]=0;
                now=a[i][0];
            }
            ss++;
            memmove(na[ss],a[lab[i]],12);
            now=a[lab[i]][1];
        }
        if (now<x)
        {
            na[++ss][0]=now;
            na[ss][1]=x;
            na[ss][2]=0;
        }
        for (int i=1;i<=ss;i++)
            lab[i]=i;
        sort(lab+1,lab+ss+1,cmp2);
        for (int i=1;i<=ss;i++)
        {
            if (t>0)
            {
                double te=min((na[lab[i]][1]-na[lab[i]][0])*1.0/(r+na[lab[i]][2]*1.0),t*1.0);
                ans+=te+((na[lab[i]][1]-na[lab[i]][0])-te*(r+na[lab[i]][2]*1.0))/(na[lab[i]][2]+s*1.0);
                t-=te;
            }
            else
                ans+=(na[lab[i]][1]-na[lab[i]][0])*1.0/(na[lab[i]][2]+s*1.0);
        }
        printf("Case #%d: %.9lf\n",ii,ans);
    }
    return 0;
}
