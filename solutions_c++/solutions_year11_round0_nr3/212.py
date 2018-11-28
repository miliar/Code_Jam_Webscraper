#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int ss, s, n, a[1005];

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int Test; scanf("%d", &Test);
    for (int tts = 1; tts <= Test; ++tts) {
        printf("Case #%d: ", tts);
        scanf("%d", &n); ss = s = 0;
        for (int i = 1; i <= n; ++i) {
            scanf("%d", &a[i]);
            ss ^= a[i];
            s += a[i];
        }

        if (ss) puts("NO");
        else {
            sort(a + 1, a + n + 1);
            printf("%d\n", s - a[1]);
        }
    }
    return 0;
}
