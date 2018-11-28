#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int a[1005], n;
double ans;
int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);

    int Test; scanf("%d", &Test);
    for (int tts = 1; tts <= Test; ++tts) {
        printf("Case #%d: ", tts);
        scanf("%d", &n); ans = 0;
        for (int i = 1; i <= n; ++i)
            scanf("%d", &a[i]);

        for (int i = 1; i <= n; ++i)
        if (a[i] != i) ++ans;

        printf("%.6lf\n", ans);
    }
    return 0;
}
