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
# define MAXN 200
using namespace std;

int main()
{
    int t, r, i, x1, x2, y1, y2, ii, jj, ans;
    bool v[MAXN][MAXN], w[MAXN][MAXN];
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++) {
        scanf("%d", &r);
        ans = 0;
        memset(v, false, sizeof v);
        for (i = 0; i < r; i++) {
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            for (ii = x1; ii <= x2; ii++) {
                for (jj = y1; jj <= y2; jj++) {
                    v[jj - 1][ii - 1] = true;
                }
            }
        }
        while(true) {
            for (ii = 0; ii < MAXN; ii++) {
                for (jj = 0; jj < MAXN; jj++) {
                    if (v[ii][jj]) {
                        break;
                    }
                }
                if (jj < MAXN) {
                    break;
                }
            }
            if (ii == MAXN) {
                break;
            }
            ans++;
            for (ii = 0; ii < MAXN; ii++) {
                for (jj = 0; jj < MAXN; jj++) {
                    if (v[ii][jj]) {
                        if (!(ii > 0 && v[ii - 1][jj] || jj > 0 && v[ii][jj - 1])) {
                            w[ii][jj] = false;
                        }
                        else {
                            w[ii][jj] = true;
                        }
                    }
                    else if (ii > 0 && v[ii - 1][jj] && jj > 0 && v[ii][jj - 1]) {
                        w[ii][jj] = true;
                    }
                    else {
                        w[ii][jj] = false;
                    }
                }
            }
            for (ii = 0; ii < MAXN; ii++) {
                for (jj = 0; jj < MAXN; jj++) {
                    v[ii][jj] = w[ii][jj];
                }
            }
        }
        printf("Case #%d: %d\n", tt, ans);
    }
	return 0;
}
