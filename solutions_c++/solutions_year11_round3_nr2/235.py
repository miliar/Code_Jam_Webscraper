#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;

long long a[1000005],C[1005],dist[1000005];
long long b[1000005];
long long MAX(long long a,long long b)
{
    return a>b?a:b;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        printf("Case #%d: ",cas);
        long long l,t,n,c;
        cin>>l>>t>>n>>c;
        for (int i=0;i<c;i++) cin>>C[i];
        int now=0;
        for (int i=1;i<=n;i++)
        {
            a[i]=C[now];
            now=(now+1)%c;
        }
        dist[0]=0;
        for (int i=1;i<=n;i++)
            dist[i]=dist[i-1]+a[i];
        long long pos=-1;
        long long d=0;
        long long sum=0;
        for (int i=1;i<=n;i++)
        {
            if (2*dist[i]==t)
            {
                pos=i;d=0;break;
            }
            if (2*dist[i]>t)
            {
                pos=i;d=dist[i]-t/2;
                break;
            }
        }
        if (pos==-1)
        {
            printf("%llu\n",dist[n]*2);
            continue;
        }
        sum+=t;
        long long tot=0;
        if (d>0)
            b[tot++]=d;
        for (long long i=pos+1;i<=n;i++)
            b[tot++]=a[i];
        sort(b,b+tot);
        for (long long i=tot-1;i>=MAX(0,tot-l);i--)
            sum+=b[i];
        for (long long i=MAX(-1,tot-l-1);i>=0;i--)
            sum+=b[i]*2;
        printf("%llu\n",sum);
    }
}
