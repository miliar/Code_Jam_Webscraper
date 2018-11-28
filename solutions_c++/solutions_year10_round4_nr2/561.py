# include <iostream>
# include <cstdio>
# include <cstring>
# include <cmath>
# include <ctime>
# include <cstdlib>
# include <ctime>
# include <algorithm>
# include <set>
# include <string>
# include <vector>
# include <list>
# include <map>
# include <queue>
# include <stack>
# include <iomanip>
# include <numeric>
# include <functional>
# include <iterator>
# define MAXN 10000
# define MAXM 20
# define INF 0x7f7f7f7f
using namespace std;

long long int dp[MAXM][MAXN];
int size, v[MAXN], w[MAXN];

/*
    a = altura
    b = faltantes
    c = nodos
*/
long long int go(int a, int b, int c)
{
    int i;
    if (a == 0) {
        if (b > v[c - size]) {
            return INF;
        }
        return 0;
    }
    long long int &best = dp[b][c];
    if (best != -1LL) {
        return best;
    }
    best =  min(
                go(a - 1, b + 1, 2 * c) + go(a - 1, b + 1, 2 * c + 1),
                (long long int)(w[c]) + go(a - 1, b, 2 * c) + go(a - 1, b, 2 * c + 1)
            );
    return best;
}

int main()
{
    int t, ans, i, p, n, j, m, temp[MAXN], k;
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++) {
        scanf("%d", &p);
        size = 1 << p;
        for (i = 0; i < size; i++) {
            scanf("%d", &v[i]);
        }
        n = (1 << p) - 1;
        for (i = 1; i <= n; i++) {
            scanf("%d", &temp[i]);
        }
        k = 1;
        m = 0;
        for (i = 0; i < p; i++) {
            m += 1 << i;
            for (j = 1; j <= (1 << i); j++) {
                w[k++] = temp[n - m + j];
            }
        }
        memset(dp, -1, sizeof dp);
        printf("Case #%d: %lld\n", tt, go(p, 0, 1));
    }
	return 0;
}
