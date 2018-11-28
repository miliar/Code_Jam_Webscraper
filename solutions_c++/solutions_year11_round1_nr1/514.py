#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<deque>
using namespace std;

typedef long long ll;

int gcd(int a,int b)
{
    if(b==0) return a;
    return gcd(b,a%b);
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t,i,j;
    int pd,pg;
    ll n;
    scanf("%d",&t);
    int cs=0;
    while(t--)
    {
        scanf("%lld%d%d",&n,&pd,&pg);
        printf("Case #%d: ",++cs);
        int d=gcd(pd,100);
        d=100/d;
        if(pg==0)
        {
           if(pd>0) printf("Broken\n");
           else printf("Possible\n");
        }
        else if(pg==100)
        {
            if(pd<100) printf("Broken\n");
            else printf("Possible\n");
        }
        else
        {
        if(d<=n)
        printf("Possible\n");
        else printf("Broken\n");
        }
    }
    return 0;
}











