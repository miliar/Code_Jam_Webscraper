#include <stdio.h>
#include <iostream>

using namespace std;
typedef long long LL;

LL gcd(LL a, LL b)
{
    return b == 0 ? a : gcd(b, a % b);
}

int main()
{
    int test, cas(1);
    LL n, d, g;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    cin>>test;
    while(test--)
    {
        cin>>n>>d>>g;
        LL k(1);
        bool flag(true);
        if(g == 100 && d != 100 || d != 0 && g == 0)
            flag = false;
        if(g > 100 || d > 100) flag = false;
        LL gg = gcd(100,d);
        if(100 / gg > n)    flag = false;

        printf("Case #%d: ",cas++);
        if(flag)   printf("Possible\n");
        else  printf("Broken\n");
    }
    return 0;
}
