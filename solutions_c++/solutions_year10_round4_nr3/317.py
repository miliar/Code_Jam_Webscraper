#include <iostream>
#include <cstring>
using namespace std;
const long maxn = 100 + 10;

bool map[maxn][maxn], map2[maxn][maxn];
long ans;

bool exist_live(void)
{
        for (long i = 1; i <= 100; i++)
                for (long j = 1; j <= 100; j++)
                        if (map[i][j])
                                return true;
        return false;
}

int main(void)
{
              freopen("c.in", "r", stdin);
              freopen("c.out", "w", stdout);
        long T;
        cin >> T;
        for (long loop = 1; loop <= T; loop++) {
                long r;
                cin >> r;
                memset(map, false, sizeof(map));
                for (long i = 0; i < r; i++) {
                        long x1, y1, x2, y2;
                        cin >> x1 >> y1 >> x2 >> y2;
                        for (long x = x1; x <= x2; x++)
                                for (long y = y1; y <= y2; y++)
                                        map[x][y] = true;
                }
                        
                ans = 0;
                while (exist_live()) {
                        for (long i = 1; i <= 100; i++)
                                for (long j = 1; j <= 100; j++) {
                                        map2[i][j] = map[i][j];
                                        if (map[i][j] && !map[i - 1][j] && !map[i][j - 1])
                                                map2[i][j] = false;
                                        if (!map[i][j] && map[i - 1][j] && map[i][j - 1])
                                                map2[i][j] = true;
                                }
                        ++ans;
                        for (long i = 1; i <= 100; i++)
                                for (long j = 1; j <= 100; j++)
                                        map[i][j] = map2[i][j];
                }
                cout << "Case #" << loop << ": " << ans << endl;
        }
        return 0;
}
