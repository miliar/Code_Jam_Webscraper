#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 1111;
int a[MAXN];

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("in", "r", stdin);
        freopen("out", "w", stdout);
    #endif

    int countTest;
    scanf("%d", &countTest);
    for (int test = 1; test <= countTest; test++)
    {
        printf("Case #%d: ", test);
        int n, x;
        scanf("%d", &n);
        x = 0;
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &a[i]);
            x ^= a[i];
        }

        if (x)
        {
            printf("NO\n");
            continue;
        }

        partial_sort(a, a + 1, a + n);
        int s = 0;
        for (int i = 1; i < n; i++)
            s += a[i];
        printf("%d\n", s);
    }
    return 0;
}
