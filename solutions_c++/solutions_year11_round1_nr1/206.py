#include <cstdio>
#include <cstdlib>
#include <cstring>

long long n;
int A, B;

    int gcd(int aa, int bb)
    {
        if (!bb) return aa;
        return gcd(bb, aa % bb);
    }

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int Test, tts = 0;
    for (scanf("%d", &Test); Test--; ) {
        scanf("%I64d%d%d", &n, &A, &B);
        printf("Case #%d: ", ++tts);
        int g;
        if (A == 0) g = 1; else g = 100 / gcd(A, 100);
        if (g > n) puts("Broken");
        else
        if (A == 100 && B == 100) puts("Possible");
        else
        if (A < 100 && B == 100) puts("Broken");
        else
        if (A > 0 && B == 0) puts("Broken");
        else
        puts("Possible");
    }
    return 0;
}
