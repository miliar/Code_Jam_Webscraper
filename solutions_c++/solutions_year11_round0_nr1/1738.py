#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

int ww[105], pp[105];
int n;
int main()
{
    freopen("A-large.in","r", stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        char ch;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf(" %c %d", &ch, &pp[i]);
            if (ch == 'O') ww[i] = 0;
            else ww[i] = 1;
        }
        int x = 1, y = 1, t = 0;
        for (int i = 0; i < n; ++i) {
            int nx = -1, ny = -1;
            for (int j = i; j < n; ++j) {
                if (ww[j] == 0) {
                    nx = j;
                    break;
                }
            }
            for (int j = i; j < n; ++j) {
                if (ww[j] == 1) {
                    ny = j;
                    break;
                }
            }
            if (ww[i] == 0) {
                int s = abs(x - pp[i]) + 1;
                if (ny >= 0) {
                    if (pp[ny] >= y) {
                        y = min(pp[ny], y + s);
                    } else {
                        y = max(pp[ny], y - s);
                    }
                }
                x = pp[i];
                t += s;
            } else {
                int s = abs(y - pp[i]) + 1;
                if (nx >= 0) {
                    if (pp[nx] >= x) {
                        x = min(pp[nx], x + s);
                    } else {
                        x = max(pp[nx], x - s);
                    }
                }
                y = pp[i];
                t += s;
            }
        }
        printf("Case #%d: %d\n", ca, t);
    }
    return 0;
}
