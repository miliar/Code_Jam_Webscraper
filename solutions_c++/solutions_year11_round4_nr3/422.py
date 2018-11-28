#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstdlib>

using namespace std;


const int MAXN = 1111111;

bool f[MAXN];
long long p[MAXN];
long long n;
int k;

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("in", "rt", stdin);
        freopen("out", "wt", stdout);
    #endif

    memset(f, true, sizeof(f));
    f[0] = f[1] = false;
    for (long long i = 2; i < MAXN; i++)
        if (f[i])
        {
            p[k++] = i;
            for (long long j = i * i; j < MAXN; j += i) f[j] = false;
        }
    int ctest;
    scanf("%d", &ctest);
    for (int test = 1; test <= ctest; test++)
    {
        printf("Case #%d: ", test);

        cin >> n;
//        n = 1000000000000LL;
//        printf("%d\n", rand() % 10000 + 1);

        long long ans = 0;
        int m = (int)sqrt((double)n);
        for (int i = 0; i < k && p[i] * p[i] <= n; i++)
        {
            long long x = p[i];
            while (x <= n)
            {
                ans++;
                x *= p[i];
            }
            ans--;
        }
        cout << ans + (n > 1) << endl;
    }
    return 0;
}
