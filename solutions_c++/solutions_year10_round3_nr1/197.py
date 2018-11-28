#include <cstdio>
#include <algorithm>
using namespace std;
#define maxn 1024
pair<int, int>p[maxn];
int main() {
    int t;
    scanf("%d", &t);
    int kase = 1;
    while (t--) {
        int n, ans = 0;;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d%d", &p[i].first, &p[i].second);
        }
        sort(p, p + n);
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j <n; ++j) {
                int a = p[i].first - p[j].first;
                int b = p[i].second - p[j].second;
                if (a < 0 && b > 0 || a > 0 && b < 0) {
                    ans++;
                }
            }
        }
        printf("Case #%d: %d\n", kase++, ans);
    }
    return 0;
}
