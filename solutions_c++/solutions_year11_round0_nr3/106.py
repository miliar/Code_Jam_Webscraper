#include <cstdio>
#include <algorithm>
using namespace std;

int T, n;
int c[1001];

int main()
{
    freopen("in.in", "r", stdin);
    //freopen("out.out", "w", stdout);
    scanf("%d", &T);
    for (int cases = 1; cases <= T; ++cases)
    {
        scanf("%d", &n);
        printf("Case #%d: ", cases);
        int minn = 2000000, sum = 0;
        for (int i = 1; i <= n; ++i)
        {
            scanf("%d", c + i);
            minn = min(minn, c[i]);
            sum += c[i];
        }
        int tot = c[1];
        for (int i = 2; i <= n; ++i)
            tot ^= c[i];
        if (tot) puts("NO");
        else printf("%d\n", sum - minn);
    }
    return 0;
}
