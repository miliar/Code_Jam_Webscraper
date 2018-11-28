#include <cstdio>
#include <cstring>

#include <algorithm>
#include <queue>
using namespace std;

const int MAX_LEN = 100005;
const int MAX_N = 105;
const int INF = 0x3f3f3f3f;

long long l;
int n;
int v[MAX_N];

int max_val;
int best[MAX_LEN];
long long val[MAX_LEN];

int main() {
    freopen("date.in", "r", stdin);
    freopen("date.out", "w", stdout);

    int t; scanf("%d", &t);
    for (int test_no = 1; test_no <= t; ++test_no) {
        scanf("%lld %d", &l, &n);
        for (int i = 1; i <= n; ++i)
            scanf("%d", &v[i]);

        max_val = 0;
        for (int i = 1; i <= n; ++i)
            max_val = max(max_val, v[i]);

        memset(best, INF, sizeof(best));
        best[0] = 0;
        val[0] = 0;

        long long sol = l + 1;

        queue<int> Q; Q.push(0);
        while (!Q.empty()) {
            int nr = Q.front();
            Q.pop();

            for (int i = 1; i <= n; ++i) {
                int new_nr = (nr + v[i]) % max_val;
                int new_val = val[nr] + v[i];

                if (best[new_nr] == INF || ((new_val - val[new_nr]) / max_val + best[new_nr] > best[nr] + 1)) {
                    best[new_nr] = best[nr] + 1;
                    val[new_nr] = val[nr] + v[i];
                    Q.push(new_nr);

                    if ((new_nr % max_val) == (l % max_val))
                        if (new_val <= l) {
                            long long new_sol = best[new_nr] + (l - new_val) / max_val;
                            sol = min(sol, new_sol);
                        }
                }
            }
        }

        if (l % max_val == 0)
            sol = l / max_val;

        if (sol == l + 1) printf("Case #%d: IMPOSSIBLE\n", test_no);
        else printf("Case #%d: %lld\n", test_no, sol);
    }
}
