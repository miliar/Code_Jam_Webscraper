#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
const int maxn = 1000;

int n, casen;
int a[maxn], b[maxn];

void init()
{
     scanf("%d", &n);
     for (int i(1); i <= n; ++i) scanf("%d", &a[i]);
     for (int i(1); i <= n; ++i) scanf("%d", &b[i]);
}

void work()
{
     sort(a + 1, a + 1 + n);
     sort(b + 1, b + 1 + n);
     long long ans = 0;
     for (int i(1); i <= n; ++i)
     {
         ans += (long long)a[i] * (long long)b[n - i + 1];
     }
     printf("%I64d\n", ans);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.ans", "w", stdout);
    scanf("%d", &casen);
    for (int i(1); i <= casen; ++i)
    {
        init();
        printf("Case #%d: ", i);
        work();
    }
    return 0;
}
