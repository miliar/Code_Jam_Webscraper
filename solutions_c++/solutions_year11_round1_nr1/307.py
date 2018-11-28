#include <cstdio>

using namespace std;

int minDen[101];

int gcd(int a, int b)
{
    while (b != 0)
    {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

bool possible(int N, int PD, int PG)
{
    if (PG == 0 && PD != 0)
        return false;
    if (PG == 100 && PD != 100)
        return false;
    return minDen[PD] <= N;
}

int main()
{
    for (int p = 0; p <= 100; ++p)
        minDen[p] = 100 / gcd(p, 100);
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        int N, PD, PG;
        scanf("%d%d%d", &N, &PD, &PG);
        const char* res;
        if (possible(N, PD, PG))
            res = "Possible";
        else
            res = "Broken";
        printf("Case #%d: %s\n", testcase, res);
    }
    return 0;
}
