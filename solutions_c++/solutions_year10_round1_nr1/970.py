#include <iostream>
#include <cstring>
using namespace std;
const long maxN = 50 + 4;
const int walk[][2] = { {0, 1}, {1, 0}, {1, 1}, {1, -1} };

long n, k;
string p[maxN];

bool valid(long u)
{
        return 0 <= u && u < n;
}

bool check(long sx, long sy, long dx, long dy, long r)
{
        long cnt = 0;
        long i, j;
        i = sx;
        j = sy;
        while (valid(i) && valid(j) && cnt < r) {
                if (p[i][j] == p[sx][sy])
                        ++cnt;
                else
                        break;
                i += dx;
                j += dy;
        }
        return cnt >= r;
}

int main(void)
{
              freopen("a.in", "r", stdin);
              freopen("a.out", "w", stdout);
        long T;
        cin >> T;
        for (long loop = 1; loop <= T; loop++) {
                cin >> n >> k;
                for (long i = 0; i < n; i++)
                        cin >> p[i];
                for (long i = 0; i < n; i++) {
                        long x = n - 1;
                        for (long j = n - 1; j >= 0; j--)
                                if (p[i][j] != '.') {
                                        p[i][x--] = p[i][j];
                                        if (x + 1 != j)
                                                p[i][j] = '.';
                                }
                }

                bool redwin, bluewin;
                redwin = bluewin = false;
                for (long i = 0; i < n; i++)
                        for (long j = 0; j < n; j++)
                                if (!redwin && p[i][j] == 'R') {
                                        for (long s = 0; s < 4; s++)
                                                if (check(i, j, walk[s][0], walk[s][1], k))
                                                        redwin = true;
                                } else if (!bluewin && p[i][j] == 'B') {
                                        for (long s = 0; s < 4; s++)
                                                if (check(i, j, walk[s][0], walk[s][1], k))
                                                        bluewin = true;
                                }
                cout << "Case #" << loop << ": ";
                if (redwin && bluewin)
                        cout << "Both" << endl;
                else if (!redwin && !bluewin)
                        cout << "Neither" << endl;
                else if (redwin)
                        cout << "Red" << endl;
                else
                        cout << "Blue" << endl;
        }
        return 0;
}
