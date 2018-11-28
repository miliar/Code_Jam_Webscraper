/*
 * Sat May  7 14:04:13 CST 2011
 */
#define see(n) cerr << #n << " = " << n << endl
#define seeArray(n, a) cerr << #a << " = ";\
    for (int __i__ = 0; __i__ < (int) n; ++__i__)\
        cerr << a[__i__] << " ";\
    cerr << endl;
#define seeArray2(n, m, a) cerr << #a << " = " << endl;\
    for (int __i__ = 0; __i__ < (int) n; ++__i__) {\
        for (int __j__ = 0; __j__ < (int) m; ++__j__)\
            cerr << a[__i__][__j__] << " ";\
        cerr << endl;\
    }
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <list>
#include <sstream>
#include <cctype>
#include <ctime>
#include <numeric>
using namespace std;
const int dir[8][2] = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 }, { -1, -1 }, { -1, 1 }, { 1, -1 }, { 1, 1 } };
const int inf = 1000000000;
const long long infll = 1000000000000000000LL;
const double eps = 1e-10;
const double pi = acos(-1.0);

const int maxn = 128;
int cases, cas = 1;
struct Node {
    int x1, x2, finish;
    Node(int x1, int x2, int finish) : x1(x1), x2(x2), finish(finish) {
    }
};
int n, m;
vector<pair<int, int> > cmd;
bool inque[maxn][maxn][maxn];
int mem[maxn][maxn][maxn];

int main() {
    for (scanf("%d", &cases); cases--; ++cas) {
cerr << "cas = " << cas << endl;
        cmd.clear(); scanf("%d", &m); n = 0; for (int i = 0; i < m; ++i) {
            char buf[8]; int button; scanf("%s%d", buf, &button); n = max(n, button);
            if (buf[0] == 'O') {
                cmd.push_back(make_pair(0, button));
            } else {
                cmd.push_back(make_pair(1, button));
            }
        }
        for (int i = 0; i <= n; ++i) for (int j = 0; j <= n; ++j) for (int k = 0; k <= m; ++k) {
            inque[i][j][k] = false; mem[i][j][k] = inf;
        }
        mem[1][1][0] = 0; deque<Node> que; que.push_back(Node(1, 1, 0)); inque[1][1][0] = true;
        while (!que.empty()) {
            int x1 = que.front().x1, x2 = que.front().x2, finish = que.front().finish, dis = mem[x1][x2][finish] + 1; que.pop_front(); inque[x1][x2][finish] = false;
            if (cmd[finish].first == 0 && x1 == cmd[finish].second) for (int diff = -1; diff <= 1; ++diff) {
                int xx2 = x2 + diff; if (xx2 > 0 && xx2 <= n) if (dis < mem[x1][xx2][finish + 1]) {
                    mem[x1][xx2][finish + 1] = dis; if (!inque[x1][xx2][finish + 1]) {
                        que.push_back(Node(x1, xx2, finish + 1)); inque[x1][xx2][finish + 1] = true;
                    }
                }
            }
            if (cmd[finish].first == 1 && x2 == cmd[finish].second) for (int diff = -1; diff <= 1; ++diff) {
                int xx1 = x1 + diff; if (xx1 > 0 && xx1 <= n) if (dis < mem[xx1][x2][finish + 1]) {
                    mem[xx1][x2][finish + 1] = dis; if (!inque[xx1][x2][finish + 1]) {
                        que.push_back(Node(xx1, x2, finish + 1)); inque[xx1][x2][finish + 1] = true;
                    }
                }
            }
            for (int diff1 = -1; diff1 <= 1; ++diff1) for (int diff2 = -1; diff2 <= 1; ++diff2) {
                int xx1 = x1 + diff1, xx2 = x2 + diff2; if (xx1 > 0 && xx1 <= n && xx2 > 0 && xx2 <= n && dis < mem[xx1][xx2][finish]) {
                    mem[xx1][xx2][finish] = dis; if (!inque[xx1][xx2][finish]) {
                        que.push_back(Node(xx1, xx2, finish)); inque[xx1][xx2][finish] = true;
                    }
                }
            }
        }
        int ans = inf; for (int i = 0; i <= n; ++i) for (int j = 0; j <= n; ++j) {
            ans = min(ans, mem[i][j][m]);
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
