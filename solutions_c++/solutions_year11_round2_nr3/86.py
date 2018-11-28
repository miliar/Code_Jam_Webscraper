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

int par[20];
int getPar(int x) {
    return x == par[x]?x:par[x] = getPar(par[x]);
}

void Merge(int x, int y) {
    x = getPar(x);
    y = getPar(y);
    if (rand() & 1)
        swap(x, y);
    par[x] = y;
}

bool isIntersected(int a, int b, int c, int d, int n) {
    int left = 0;
    int right = 0;
    if (a == c || a == d || b == c || b == d)
        return false;
    for (int x = a; x != b; x = (x + 1) % n) 
        if (x == c || x == d)
            ++left;
    for (int x = b; x != a; x = (x + 1) % n) 
        if (x == c || x == d)
            ++right;
    return left == right;
}

int colors[20];
int res_colors[20];
int res;
bool can[20];
bool am[20][20];

vector<vector<int> > rooms;

void go(int pos, int ma, int n) {
    if (pos == n) {
        bool ok = true;
        for (int i = 0; i < rooms.size() && ok; ++i) {
            memset(can, false, sizeof(can));
            for (int j = 0; j < rooms[i].size(); ++j)
                can[colors[rooms[i][j]]] = true;
            for (int k = 0; k < ma; ++k) {
                ok = ok && can[k];
            }
        }
        if (ok && res < ma) {
            res = ma;
            memcpy(res_colors, colors, sizeof(colors));
        }
        return;
    }
    for (int i = 0; i <= ma; ++i) {
        colors[pos] = i;
        go(pos + 1, max(ma, i + 1), n);
    }
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; ++test) {
        memset(res_colors, 0, sizeof(res_colors));
        memset(colors, 0, sizeof(colors));
        int n, m;
        for (int i = 0; i < 20; ++i)
            par[i] = i;
        cin >> n >> m;
        vector<int> b(m);
        vector<int> e(m);
        for (int i = 0 ;i < m; ++i) {
            cin >> b[i];
            --b[i];
        }
        for (int i = 0 ;i < m; ++i) {
            cin >> e[i];
            --e[i];
        }
        memset(am, false, sizeof(am));
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j) {
                bool ok = true;
                for (int k = 0; ok && k < m; ++k)
                    if (isIntersected(i, j, b[k], e[k], n))
                        ok = false;
                am[i][j] = ok || (i == j);
            }
        rooms.clear();
        for (int i = 0; i < n; ++i)
            for (int j = i + 1; j < n; ++j)
                for (int k = j + 1; k < n; ++k) {
                    if (am[i][j] && am[j][k] && am[i][k]) {
                        vector<int> new_room;
                        new_room.push_back(i);
                        new_room.push_back(j);
                        new_room.push_back(k);
                        for (int y = 0; y < n; ++y) {
                            if (count(all(new_room), y))
                                continue;
                            bool ok = true;
                            for (int x = 0; x < new_room.size(); ++x)
                                ok = ok && am[new_room[x]][y];
                            if (ok)
                                new_room.push_back(y);
                        }
                            sort(all(new_room));
                            if (count(all(rooms), new_room) == 0)
                                rooms.push_back(new_room);
                    }
                }
        res = 0;
        go(0, 0, n);
        printf("Case #%d: %d\n", test + 1, res);
        for (int i = 0; i < n; ++i)
            cout << res_colors[i] + 1 << " ";
        cout << "\n";
    }
	return 0;
}