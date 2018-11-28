#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

const double pi = 3.1415926535;
const double eps = 1e-6;

double sx[510][510], sy[510][510], zh[510][510], su[510][510];
int n, m, d;
char ch;
int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int T, ca = 0;
    for (scanf("%d", &T); T; T--) {
        scanf("%d%d%d", &n, &m, &d);
        memset(sx, 0, sizeof(sx));
        memset(sy, 0, sizeof(sy));
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++) {
                scanf(" %c", &ch);
                zh[i][j] = ch - '0' + d;
                su[i][j] = su[i - 1][j] + su[i][j - 1] - su[i - 1][j - 1] + (ch - '0' + d);
                sx[i][j] = sx[i - 1][j] + sx[i][j - 1] - sx[i - 1][j - 1] + (ch - '0' + d) * i;
                sy[i][j] = sy[i - 1][j] + sy[i][j - 1] - sy[i - 1][j - 1] + (ch - '0' + d) * j;
            }
        int ans = 0;
        for (int L = 3; L <= min(n, m); L++)
        for (int x = L; x <= n; x++)
        for (int y = L; y <= m; y++) {
            double mx = (double)(x + x - L + 1) / 2.;
            double my = (double)(y + y - L + 1) / 2.;
            double dx = (sx[x][y] - sx[x - L][y] - sx[x][y - L] + sx[x - L][y - L]);
            double dy = (sy[x][y] - sy[x - L][y] - sy[x][y - L] + sy[x - L][y - L]);
            dx -= x * zh[x][y] + x * zh[x][y - L + 1];
            dx -= (x - L + 1) * zh[x - L + 1][y] + (x - L + 1) * zh[x - L + 1][y - L + 1];
            
            dy -= y * zh[x][y] + y * zh[x - L + 1][y];
            dy -= (y - L + 1) * zh[x][y - L + 1] + (y - L + 1) * zh[x - L + 1][y - L + 1];
            
            double s = su[x][y] - su[x - L][y] - su[x][y - L] + su[x - L][y - L] - zh[x][y] - zh[x - L + 1][y] - zh[x][y - L + 1] - zh[x - L + 1][y - L + 1];
            dx /= s, dy /= s;
//            cout << L << ' ' << x << ' ' << y << endl;
  //          cout << mx << ' ' << my << ' ' << '!' << ' ' << dx << ' ' << dy << endl;
            if (fabs(mx - dx) < eps && fabs(my - dy) < eps)
                ans = L;
        }
        printf("Case #%d: ", ++ca);
        if (ans == 0)
            puts("IMPOSSIBLE");
        else
            printf("%d\n", ans);
    }
}
