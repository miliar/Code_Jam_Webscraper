#include <cstdio>
#include <algorithm>
using namespace std;

int ID(char ch)
{
    return ch == 'O' ? 0 : 1;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, n, p;
    char r;

    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%d", &n);
        int pre[2] = {1, 1}, cur = -1, ans = 0, t = 0;
        for (int i = 0; i < n; ++i) {
            scanf(" %c%d", &r, &p);
            if (cur != ID(r)) {
                cur = ID(r);
                ans += max(0, abs(p - pre[cur]) - t) + 1;
                t = max(0, abs(p - pre[cur]) - t) + 1;
            }
            else {
                ans += abs(p - pre[cur]) + 1;
                t += abs(p - pre[cur]) + 1;
            }
            pre[cur] = p;
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
