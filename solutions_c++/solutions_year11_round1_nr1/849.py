#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int t, pd, pg;
long long n;

int gcd(int a, int b)
{
    int c;
    while (b > 0)
    {
          c = b;
          b = a % b;
          a = c;
    }
    return a;
}

bool check()
{
     if (pg == 0)
     {
            if (pd == 0) return true;
            return false;
     }
     if (pg == 100)
     {
            if (pd == 100) return true;
            return false;
     }
     if (pd == 0) return true;
     return 100 / gcd(100, pd) <= n;
}      

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    scanf("%d", &t);
    for (int cas = 1; cas <= t; cas++)
    {
        cin >> n;
        scanf("%d%d", &pd, &pg);
        printf("Case #%d: ", cas);
        if (check()) printf("Possible\n");
        else printf("Broken\n");
    }
    return 0;
}
