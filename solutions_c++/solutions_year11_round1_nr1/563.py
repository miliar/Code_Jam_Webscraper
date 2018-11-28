#include<cstdio>
#include<cstring>
using namespace std;
typedef long long ll;
int T;
ll N,pd,pg;
ll gcd(ll a,ll b)
{
    return b?gcd(b,a%b):a;
}
int main()
{
    freopen("yy.in","r",stdin);
    freopen("yy.out","w",stdout);
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        scanf("%lld%lld%lld",&N,&pd,&pg);
        printf("Case #%d: ",cas);
        if(pg==100&&pd!=100||pg==0&&pd!=0) 
            printf("Broken\n");
        else 
        {
            ll temp=gcd(pd,100);
            if(temp) temp=100/temp;
            if(temp>N) printf("Broken\n");
            else printf("Possible\n");
        }
    }
    return 0;
}
