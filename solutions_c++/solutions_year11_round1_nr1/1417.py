#include <cstdio>
#include <algorithm>

using namespace std;


long long gcd(long long a, long long b)
{
    return b == 0? a : gcd(b, a % b);
}

long long lcm(long long a, long long b)
{
    return a / gcd(a, b) * b;
}

int main(int argc, char *argv[])
{

    freopen(1 < argc? argv[1] : "in", "rt", stdin);
    freopen(2 < argc? argv[2] : "out", "wt", stdout);
    
    int countTest = 0;
    scanf("%d", &countTest);
    for (int currTest = 1; currTest <= countTest; currTest++)
    {
        printf("Case #%d: ", currTest);

        int pd, pg;
        long long n;
        scanf("%I64d %d %d", &n, &pd, &pg);

        bool f = false;
        for (int d = 1; d <= n && !f; d++)
        {
            if (d * pd % 100) continue;
            int x = d * pd / 100;
            for (int g = d; g < 10000000 && !f; g++)
            {
                if (g * pg % 100) continue;
                int y = g * pg / 100;

                if (y < x || g - y < d - x) continue;
//                printf("%d %d, %d %d (%d)\n", x, d, y, g, pg);
                f = true;
            }
        }

        printf("%s", f? "Possible" : "Broken");
        printf("\n");
    }


    return 0;
}
