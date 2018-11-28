#include <iostream>
#include <fstream>
using namespace std;

long long n;
int pd, pg;

int gcd(int x, int y)
{
    if (0 == y) return x;
    return gcd(y, x % y);
}

int main()
{
    freopen("game.in", "r", stdin);
    freopen("game.out", "w", stdout);

    int tt;
    scanf("%d", &tt);
    for (int i = 0; i < tt; i++)
    {
        printf("Case #%d: ", i + 1);
        scanf("%lld%d%d", &n, &pd, &pg);
        if ((pg == 0 && pd != 0) || (pd != 100 && pg == 100)) printf("Broken\n");
        else
        {
            int tmp = 100 / gcd(100, pd);
            if (tmp <= n) printf("Possible\n");
            else printf("Broken\n");
        }
    }


    return 0;
}
