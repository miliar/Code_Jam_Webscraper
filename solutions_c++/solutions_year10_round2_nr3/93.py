#include <cstdio>
#include <cstring>
using namespace std;

int N;

long long int table[512][512];
long long int ctable[512][512];
const int MOD = 100003;

int C(int n, int k)
{
    if(n < k)
        return 0;
    else if(n == k || k == 0)
        return 1;
    else if(ctable[n][k])
        return ctable[n][k] - 1;
    else
        return (ctable[n][k] = (C(n - 1, k - 1) + C(n - 1, k)) % MOD)++;
}

long long int calc(int n, int size)
{
    if(size == 1)
        return 1;
    else if(table[n][size])
        return table[n][size] - 1;
    else
    {
        long long int& v = table[n][size];

        for(int s = size - 1; s >= 1; s--)
            (v += (calc(size, s) * C(n - size - 1, size - s - 1)) % MOD) %= MOD;
        return v++;
    }
}

int main()
{
    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        printf("Case #%d: ", t);

        scanf("%d", &N);

        long long int ans = 0;
        for(int s = N - 1; s >= 1; s--)
            (ans += calc(N, s)) %= MOD;
        printf("%d\n", (int)ans);


    }

    return 0;
}
