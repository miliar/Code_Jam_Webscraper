// simple

#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <iostream>
#include <cassert>
#include <string>

using namespace std;

const int inf = (int)1e+6;
const int n = 3100;

int ax[2*n + 3]; // minx
int bx[2*n + 3]; // maxx
int ay[2*n + 3]; // miny
int by[2*n + 3]; // maxy
long long ans;

void init() {
    int L;
    scanf("%d", &L);
    string s;
    int cnt;
    int x = 0, y = 0, nx, ny;
    pair < int , int > dir(0, 1);
    while (L > 0) {
        cin >> s >> cnt;
        while (cnt > 0) {
            for (int i = 0; i < (int)s.length(); ++i) {
                if (s[i] == 'F') {
                    nx = x + dir.first;
                    ny = y + dir.second;
                    ans += ((long long)nx*y - (long long)ny*x);

                    if (nx == x) {
                        ax[min(y, ny) + n] = min(ax[min(y, ny) + n], x);
                        bx[min(y, ny) + n] = max(bx[min(y, ny) + n], x);
                    } else {
                        ay[min(x, nx) + n] = min(ay[min(x, nx) + n], y);
                        by[min(x, nx) + n] = max(by[min(x, nx) + n], y);
                    }

                    x = nx, y = ny;
                }
                if (s[i] == 'L') dir = make_pair(-dir.second, dir.first);                    
                if (s[i] == 'R') dir = make_pair(dir.second, -dir.first);
            }
            --cnt;
        }

        --L;
    }
    ans = abs((int)ans);
    assert(ans % 2 == 0);
    ans = -ans / 2;
    for (x = -n; x < n; ++x) {
        for (y = -n; y < n; ++y) {
            if ((ay[x + n] <= y && y < by[x + n]) || (ax[y + n] <= x && x < bx[y + n])) {
                ans++;
//                cerr << x << " " << y << endl;
            }
        }
    }
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testcnt;
    scanf("%d", &testcnt);
    for (int testid = 0; testid < testcnt; ++testid) {
        for (int i = 0; i < 2*n + 3; ++i) {
            ax[i] = ay[i] = inf;
            bx[i] = by[i] = -inf;
        }
        ans = 0;
        init();
        printf("Case #%d: ", testid + 1);
        cout << ans << endl;

        cerr << testid + 1 << endl;
    }

    return 0;
}
