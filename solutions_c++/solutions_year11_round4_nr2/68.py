#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <set>
#include <map>
#include <cassert>
#include <queue>
#include <deque>
#include <stack>
#include <sstream>
#include <cstring>
#include <string>
#include <functional>
#include <numeric>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()

const int INF = ((1 << 31) - 1);
const long long LLINF = (((1LL << 63) - 1LL));
const double eps = 1e-9;
const double PI = 3.14159265358979323846;

typedef long long ll;

ll sum(int i, int j, int ni, int nj, vector<vector<ll> > & wx) { 
    ll sum_x = wx[ni][nj];
    if (i > 0)
        sum_x -= wx[i - 1][nj];
    if (j > 0)
        sum_x -= wx[ni][j - 1];
    if (i > 0 && j > 0)
        sum_x += wx[i - 1][j - 1];
    return sum_x;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; ++test) {
        int R, C, D;
        cin >> R >> C >> D;
        vector<string> plan(R);
        for (int i = 0; i < R; ++i) {
            cin >> plan[i];
        }
        vector<vector<ll> > wx(R, vector<ll> (C, 0));
        vector<vector<ll> > wy(R, vector<ll> (C, 0));
        vector<vector<ll> > w(R, vector<ll> (C, 0));
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                wx[i][j] = 1LL * i * (plan[i][j] - '0');
                wy[i][j] = 1LL *  j * (plan[i][j] - '0');
                w[i][j] = 1LL *  (plan[i][j] - '0');
            }
        }

        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                wx[i][j] += (i > 0 ? wx[i - 1][j] : 0) + 
                            (j > 0 ? wx[i][j - 1] : 0) -
                            (j > 0 && i > 0 ? wx[i - 1][j - 1] : 0);
                wy[i][j] += (i > 0 ? wy[i - 1][j] : 0) + 
                            (j > 0 ? wy[i][j - 1] : 0) -
                            (j > 0 && i > 0 ? wy[i - 1][j - 1] : 0);
                w[i][j] += (i > 0 ? w[i - 1][j] : 0) + 
                            (j > 0 ? w[i][j - 1] : 0) -
                            (j > 0 && i > 0 ? w[i - 1][j - 1] : 0);
            }
        }
        int res = -1;
        for (int k = 3; k <= min(R, C); ++k) {
            for (int i = 0; i + k - 1 < R; ++i)
                for (int j = 0; j + k - 1 < C; ++j) {
                    int ni = i + k - 1;
                    int nj = j + k - 1;
                    ll sum_x = sum(i, j, ni, nj, wx) - sum(i, j, i, j, wx) - sum(ni, nj, ni, nj, wx) - sum(ni, j, ni, j, wx) - sum(i, nj, i, nj, wx);
                    ll sum_y = sum(i, j, ni, nj, wy) - sum(i, j, i, j, wy) - sum(ni, nj, ni, nj, wy) - sum(ni, j, ni, j, wy) - sum(i, nj, i, nj, wy);
                    ll sum_w = sum(i, j, ni, nj, w) - sum(i, j, i, j, w) - sum(ni, nj, ni, nj, w) - sum(ni, j, ni, j, w) - sum(i, nj, i, nj, w);
                    if (1LL * (i + ni) * sum_w == 2LL * sum_x &&
                        1LL * (j + nj) * sum_w == 2LL * sum_y)
                        res = k;
                }
        }
        printf("Case #%d: ", test + 1);
        if (res == -1)
            cout << "IMPOSSIBLE\n";
        else
            cout << res << "\n";
    }
	return 0;
}