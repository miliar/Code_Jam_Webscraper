#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

void init()
{
    int cas;

    scanf("%d", &cas);
    for (int k = 1; k <= cas; ++k)
    {
        int n, sum = 0, a[1000], ans = 0;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
        {
            scanf("%d", a + i);
            sum ^= a[i];
            ans += a[i];
        }
        sort(a, a + n);
        printf("Case #%d: ", k);
        if (sum != 0) printf("NO");
        else printf("%d", ans - a[0]);
        printf("\n");
    }
}

int main()
{
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    init();
    fclose(stdin);
    fclose(stdout);
    return 0;
}