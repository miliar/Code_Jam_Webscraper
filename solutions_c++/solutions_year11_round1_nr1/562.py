#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<queue>
#include<vector>
#include<stack>
#include<map>
using namespace std;
void rw();
int pd,pg;
long long n;
int gcd(int a,int b)
{
    return b==0?a:gcd(b,a%b);
}
void init()
{
    scanf("%lld%d%d",&n,&pd,&pg);
    int k=100/gcd(100,pd);
    if(k<=n)
    {
        if((pd!=100&&pg==100)||(pg==0&&pd!=0))
        printf("Broken\n");
        else
        printf("Possible\n");
    }
    else
    printf("Broken\n");
}
void solve(){}
int main()
{
    int Case;
    rw();
    scanf("%d",&Case);
    for(int i=1;i<=Case;i++)
    {
        printf("Case #%d: ",i);
        init();
    }
return 0;
}

void rw()
{
freopen("E:\\A-large.in","r",stdin);
freopen("E:\\ans_A_small.out","w",stdout);
}
