#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;

char grid[512][512];
long long x[512][512], y[512][512], w[512][512];
long long sx[512][512], sy[512][512], sw[512][512];

void calcsum(int n, int m, long long a[512][512], long long sa[512][512])
{
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            sa[i+1][j+1] = sa[i+1][j] + sa[i][j+1] - sa[i][j] + a[i][j];
}

long long getsum(long long sa[512][512], int lx, int ly, int rx, int ry)
{
    return sa[lx][ly] + sa[rx][ry] - sa[lx][ry] - sa[rx][ly];
}

int main()
{
    int T, cas = 0;
    scanf("%d", &T);
    while (T--) {
        int n, m, mass;
        scanf("%d%d%d", &n, &m, &mass);
        for (int i = 0; i < n; i++)
            scanf("%s", grid[i]);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                w[i][j] = (grid[i][j] - '0') + mass;
                x[i][j] = w[i][j] * i;
                y[i][j] = w[i][j] * j;
            }
        calcsum(n, m, w, sw);
        calcsum(n, m, x, sx);
        calcsum(n, m, y, sy);
        int ans = 0;
        for (int len = min(n, m); len >= 3; len --) {
            bool found = false;
            for (int i = 0; i + len <= n; i++)
                for (int j = 0; j + len <= m; j++) {
                    long long sumx = getsum(sx, i, j, i + len, j + len);
                    long long sumy = getsum(sy, i, j, i + len, j + len);
                    long long sumw = getsum(sw, i, j, i + len, j + len);
                    sumx -= x[i][j] + x[i + len - 1][j] + x[i][j + len - 1] + x[i + len - 1][j + len - 1];
                    sumy -= y[i][j] + y[i + len - 1][j] + y[i][j + len - 1] + y[i + len - 1][j + len - 1];
                    sumw -= w[i][j] + w[i + len - 1][j] + w[i][j + len - 1] + w[i + len - 1][j + len - 1];
                    if (sumx * 2 != sumw * (i + i + len - 1) || sumy * 2 != sumw * (j + j + len - 1))
                        continue;
                    found = true;
                    break;
                }
            if (found) {
                ans = len;
                break;
            }
        }
        if (ans == 0)
            printf("Case #%d: IMPOSSIBLE\n", ++cas);
        else 
            printf("Case #%d: %d\n", ++cas, ans);
    }
}
