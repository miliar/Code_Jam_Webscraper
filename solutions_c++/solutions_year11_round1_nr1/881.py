#include<iostream>
#include <cstdio>
#include <string.h>
#include <map>
#include <string>
#include <algorithm>
using namespace std;
int gcd(int x)
{
    for (int i=100;i>=1;--i)
    if (x%i==0&&100%i==0) return i;
    return 1;
}
int main()
{
    int tc,cas,pg,pd;
    long long n;
    freopen("A-large.in","r",stdin);
        freopen("iall2.txt","w",stdout);
    cin>>tc;
    for (cas=1;cas<=tc;++cas)
    {
        bool ans = false;
        cin>>n>>pd>>pg;
        if (pg==0) ans=(pd==0);
        else if (pg==100) ans=(pd==100);
        else
        {
            ans=(n>=100/gcd(pd));
        }
        if (ans) printf("Case #%d: Possible\n", cas);
        else printf("Case #%d: Broken\n", cas);

    }
    return 0;
}
