# include <iostream>
# include <cstdio>
# include <cmath>
# include <cstring>
# include <cstdlib>
# include <ctime>
# include <string>
# include <vector>
# include <stack>
# include <set>
# include <numeric>
# include <list>
# include <map>
# include <queue>
# include <iomanip>
# include <functional>
# include <algorithm>
# include <utility>
# include <iterator>
# include <sstream>
# define FOR(i, n, m) for (i = (n); i < (m); i++)
# define LLI long long int
# define MP make_pair
# define ULL unsigned long long
# define FORR(i, n, m) for (i = (n); i >= (m); i--)
# define INF 0x3f3f3f3f
using namespace std;

const int MAXN = 100;
const int MAXS = MAXN;

int p, n;
int v[MAXN];
int dp[MAXN + 1][MAXS + 1];

int go(int i, int j)
{
    int a, b, k1, k2, k3, jj, pp;

    if (i == n) {
        return (j == 0 ? 0: -INF);
    }

    int& best = dp[i][j];
    if (best != -1) {
        return best;
    }

    best = -INF;
    for (a = 0; a <= 10; a++) {
        b = a + (j == 0 ? 1 : 2);
        b = min(b, 10);
        for (k1 = a; k1 <= b; k1++) {
            for (k2 = a; k2 <= b; k2++) {
                for (k3 = a; k3 <= b; k3++) {
                    if (k1 + k2 + k3 == v[i]) {
                        jj = j;
                        pp = 0;

                        if (max(k1, max(k2, k3)) - min(k1, min(k2, k3)) == 2) {
                            jj--;
                        }

                        if (jj < 0) {
                            continue;
                        }

                        if (max(k1, max(k2, k3)) >= p) {
                            pp++;
                        }

                        best = max(best, pp + go(i + 1, jj));
                    }
                }
            }
        }
    }

    return best;
}

int main()
{
    int t, i, s, tt;
    tt = 1;
    cin >> t;
    FOR (tt, 1, t + 1) {
        cin >> n >> s >> p;

        FOR (i, 0, n) {
            cin >> v[i];
        }

        memset(dp, -1, sizeof (dp));

        printf("Case #%d: %d\n", tt, go(0, s));
    }

    return 0;
}
