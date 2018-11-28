#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

__int64 n;
int pd,pg;

int gcd(int a,int b)
{
    return (b==0)?a:gcd(b,a%b);
}

int main()
{
    freopen("A-small-attempt7.in","r",stdin);
    freopen("A-small-attempt7.out","w",stdout);
    int t;
    int h=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%I64d%d%d",&n,&pd,&pg);
        if(pg==0&&pd!=0)
        {
            printf("Case #%d: Broken\n",h++);
            continue;
        }
        else if(pg==100&&pd!=100)
        {
            printf("Case #%d: Broken\n",h++);
            continue;
        }
        int a=gcd(pd,100);
        int b=gcd(pg,100);
        int e=pd/a;
        int f=pg/b;
        int c=100/a;
        int d=100/b;
        if(c<=n&&d>=c&&e<=f)
        {
            printf("Case #%d: Possible\n",h++);
        }
        else
        {
            printf("Case #%d: Broken\n",h++);
        }
    }
    return 0;
}
