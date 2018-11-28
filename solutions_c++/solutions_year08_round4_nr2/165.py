#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
using namespace std;
const long N = 40000,INF=1<<28;
const double eps = 1e-6,pi=acos(-1);

long min(long a,long b)
{return a<b?a:b;}
long max(long a,long b)
{return a>b?a:b;}
void swap(long &a,long &b)
{long tt;tt=a,a=b,b=tt;}
long a1,b1,a2,b2,a3,b3;
long n,m,v;
long det(long tx1,long ty1,long tx2,long ty2,long tx3,long ty3)
{return (tx2-tx1)*(ty3-ty1)-(tx3-tx1)*(ty2-ty1);}
void Init()
{
    long i,j,k;
    scanf("%ld%ld%ld",&n,&m,&v);
}
bool ok(long nn,long &a,long &b)
{
    long i;
    if(nn==0){a=b=0;return 1;}
    for(i=1;i*i<=nn;i++)
    {
        if(nn%i==0)
        {
            a=nn/i;
            b=i;
            if(a<=n&&b<=m)
                return 1;
            swap(a,b);
            if(a<=n&&b<=m)
                return 1;
        }
    }
    return 0;
}
bool Judge()
{
    long i,j,k;
    //long p1,p2,p3,p4;
    long ad,bc;
    a3=b3=0;
    if(n*m<v)return 0;
    for(ad=v;ad<=n*m;ad++)
    {
        bc=ad-v;
        //printf("%ld %ld\n",bc,ad);
        if(ok(ad,a1,b2)&&ok(bc,a2,b1))
        {
            return 1;
        }
    }
   /* for(a1=0;a1<=n;a1++)
    {
        for(b1=0;b1<=m;b1++)
            for(a2=0;a2<=n;a2++)
                for(b2=0;b2<=m;b2++)
                {
                    if(fabs(det(0,0,a1,b1,a2,b2))==v)return 1;
                }
    }*/
    return 0;
}
void Solve()
{
    long i,j,k;
    if(Judge())
    {
        printf("%ld %ld %ld %ld %ld %ld\n",a1,b1,a2,b2,a3,b3);
    }
    else printf("IMPOSSIBLE\n");
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long T,K=1;
    scanf("%ld",&T);
    while(T--)
    {
        printf("Case #%ld: ",K++);
        Init();
        Solve();
    }
    return 0;
}
