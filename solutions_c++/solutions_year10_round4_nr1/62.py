#include <iostream>
#include <cmath>
using namespace std;

int n, m, n0, a[200][200];

int calc(int x, int y)
{
    int ret = 0;
    for (int i = x; i < x + n; ++i)
        for (int j = y; j < y + n; ++j) {
            int ii = j, jj = i;
            ret >?= 2 * abs(ii - n0) + 1;
            ret >?= 2 * abs(jj - n0) + 1;
            if (ii >= x && ii < x + n && jj >= y && jj < y + n && a[i - x + 1][j - y + 1] != a[ii - x + 1][jj - y + 1])
                return int(1e9);
            ii = 2 * n0 - ii; jj = 2 * n0 - jj;
            ret >?= 2 * abs(ii - n0) + 1;
            ret >?= 2 * abs(jj - n0) + 1;
            if (ii >= x && ii < x + n && jj >= y && jj < y + n && a[i - x + 1][j - y + 1] != a[ii - x + 1][jj - y + 1])
                return int(1e9);
        }
    return ret * ret;
}

int calc2(int x, int y)
{
    int ret = 0;
    for (int i = x; i < x + n; ++i)
        for (int j = y; j < y + n; ++j) {
            int ii = j, jj = i;
            ret >?= 2 * int(abs(ii - (n0 - 0.5))) + 2;
            ret >?= 2 * int(abs(jj - (n0 - 0.5))) + 2;
            if (ii >= x && ii < x + n && jj >= y && jj < y + n && a[i - x + 1][j - y + 1] != a[ii - x + 1][jj - y + 1])
                return int(1e9);
            ii = 2 * n0 - 1 - ii; jj = 2 * n0 - 1 - jj;
            ret >?= 2 * int(abs(ii - (n0 - 0.5))) + 2;
            ret >?= 2 * int(abs(jj - (n0 - 0.5))) + 2;
            if (ii >= x && ii < x + n && jj >= y && jj < y + n && a[i - x + 1][j - y + 1] != a[ii - x + 1][jj - y + 1])
                return int(1e9);
        }
    return ret * ret;
}

int main()
{
    freopen("a2.in", "r", stdin);
    freopen("a2.out", "w", stdout);

    int t2; cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        cin >> n;
        for (int s = 2; s <= 2 * n; ++s)
            for (int i = 1; i <= n; ++i)
                if (i < s && s - i <= n)
                    cin >> a[i][s - i];
        m = 4 * n + 1; n0 = 2 * n + 1;
        int ret = m * m;
        for (int x = 1; x + n - 1 <= m; ++x)
            for (int y = 1; y + n - 1 <= m; ++y) {
                ret <?= calc(x, y);
                ret <?= calc2(x, y);
            }
        printf("Case #%d: %d\n", t1, ret - n * n);
    }

    return 0;
}
