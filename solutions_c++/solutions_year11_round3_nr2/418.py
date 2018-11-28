#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>

using namespace std;

int T,L,t,n,m;
int dis[1000001],a[1000001];
double speed[1000001],d[1000001];

bool cmp(const double &a,const double &b)
{
    return a-b>0.000000001;
}
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&T);
    for (int ca=1;ca<=T;ca++)
    {
        scanf("%d%d%d%d",&L,&t,&n,&m);
        for (int i=0;i<m;i++)
         scanf("%d",&a[i]);

        int j=0;
        for (int i=0;i<n;i++)
        {
            dis[i]=a[j];
            j=(j+1)%m;
        }
        int loc,i=0,sum=0;
        while ((sum*2<=t) && (i<n))
        {
            sum+=dis[i];
            i++;
        }
        if (sum*2<=t)
        {
            printf("%s%d%s%d\n","Case #",ca,": ",sum*2);
            continue;
        }
        i--;
        sum-=dis[i];

        if (sum*2==t)
        {
            loc=i+1;
            for (int i=loc;i<=n;i++)
            {
                d[i]=dis[i-1];
                speed[i]=d[i]/1;
            }
        }
        else
        {
            loc=i+1;
            double delta=t-sum*2;
            d[loc]=dis[loc-1]-delta/2;
            speed[loc]=d[loc]/1;
            for (int i=loc+1;i<=n;i++)
            {
                d[i]=dis[i-1];
                speed[i]=d[i]/1;
            }
        }
        sort(speed+loc,speed+n+1,cmp);
        double ans=t;
        if (loc+L-1<=n)
        {
            for (int i=loc;i<=loc+L-1;i++)
             ans+=speed[i];
            for (int i=loc+L;i<=n;i++)
             ans+=speed[i]*2;
        }
        else
        {
            for (int i=loc;i<=n;i++)
             ans+=speed[i];
        }
        long long anss=floor(ans);
        long long aa=0;
        for (int i=0;i<=n-1;i++) aa+=dis[i];


        printf("%s%d%s%d\n","Case #",ca,": ",anss);
    }
    return 0;
}
