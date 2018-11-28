#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

int gcd(int a, int b)
{
    if (a > b) return gcd(b, a);
    if (a == 0) return b;
    return gcd(b%a, a);
}

int main()
{
    int teste, t;
    scanf("%d", &teste);
    for (t=0; t<teste; t++)
    {
        long long n;
        int pd, pg;
        scanf("%I64d %d %d", &n, &pd, &pg);

        bool ans = false;

        if (pg == 100)
        {
            ans = (pd == 100);
        }
        else if (pg == 0)
        {
            ans = (pd == 0);
        }
        else
        {
            if (pd == 0 || pd == 100)
            {
                ans = true;
            }
            else
            {
                int d = gcd(pd, 100-pd);
                int m = 100/d;
                ans = (m <= n);
            }
        }

        if (ans)
            printf("Case #%d: Possible\n", t+1);
        else
            printf("Case #%d: Broken\n", t+1);
    }
    return 0;
}
