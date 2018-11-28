#include <cstdio>
#include <algorithm>
using namespace std;

int gcd(int a, int b)
{
    while(b)
        swap(a %= b, b);

    return a;
}

int main()
{
    int T;
    scanf("%d", &T);

    for(int testnum = 1; testnum  <= T; testnum++)
    {
        long long int N;
        int PD, PG;

        scanf("%lld%d%d", &N, &PD, &PG);

        printf("Case #%d: ", testnum);

        if((PG == 100 && PD != 100) || (PG == 0 && PD != 0) || 100 / gcd(100, PD) > N)
            printf("Broken\n");
        else
            printf("Possible\n");
    }
    return 0;
}
