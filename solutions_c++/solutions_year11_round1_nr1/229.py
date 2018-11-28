#include <stdio.h>
#include <iostream>

using namespace std;

long long n;
int pd, pg;

void solve()
{
    cin >> n >> pd >> pg;
    if(pg == 100 && pd != 100)
    {
        printf("Broken\n");
        return;
    }
    if(pg == 0 && pd != 0)
    {
        printf("Broken\n");
        return;
    }
    int nod = __gcd(pd, 100);
    if(100 / nod > n)
    {
        printf("Broken\n");
        return;
    }
    
    printf("Possible\n");
}

int main()
{
    int t;
    scanf("%d",&t);
    for(int i = 1; i <= t; i ++)
    {
        printf("Case #%d: ",i);
        solve();
    }
    
    return 0;
}
