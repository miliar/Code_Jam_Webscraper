#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#pragma comment(linker, "/STACK:64000000")

template<class T> inline T sqr (T x) {return x * x;}

typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;
typedef pair<int, pii> pip;
typedef pair<pii, int> ppi;
typedef pair<int64, int64> pii64;
typedef pair<double, double> pdd;
typedef pair<string, int> psi;
typedef pair<int, string> pis;
#define FAIL ++*(int*)0
#define eps  1e-9
#define inf  0x7f7f7f7f
#define MP make_pair
#define sz(C) (int)((C).size())
#define all(C) (C).begin(), (C).end()
#define TASK "test"
#define RR 151

int dx[] = {-1, 0, 1};

struct node {
    int x, ox, bx, time;
    node () {}
    node (int x, int ox, int bx, int time)
        : x (x), ox (ox), bx (bx), time (time) {}
    bool operator < (const node &o) const {
        return time > o.time || time == o.time && x < o.x;
    }
};

int n;
char a[1 << 7];
int b[1 << 7];

int dist[1 << 7][1 << 7][1 << 7];

inline bool ok (int x) {
    return x >= 0 && x < 100;
}

int dijkstra () {
    memset(dist, 127, sizeof dist);
    priority_queue<node> pq;
    pq.push(node(0, 0, 0, 0));
    dist[0][0][0] = 0;
    while (!pq.empty()) {
        node cur = pq.top(); pq.pop();
        if (dist[cur.x][cur.ox][cur.bx] != cur.time) continue;
        if (cur.x == n)
            return cur.time;
        if (a[cur.x] == 'O' && cur.ox == b[cur.x]) {
            for (int i = 0; i < 3; ++i) {
                int bx = cur.bx + dx[i];
                if (ok(bx) && dist[cur.x + 1][cur.ox][bx] > cur.time + 1) {
                    dist[cur.x + 1][cur.ox][bx] = cur.time + 1;
                    pq.push(node(cur.x + 1, cur.ox, bx, cur.time + 1));
                }
            }
        }
        if (a[cur.x] == 'B' && cur.bx == b[cur.x]) {
            for (int i = 0; i < 3; ++i) {
                int ox = cur.ox + dx[i];
                if (ok(ox) && dist[cur.x + 1][ox][cur.bx] > cur.time + 1) {
                    dist[cur.x + 1][ox][cur.bx] = cur.time + 1;
                    pq.push(node(cur.x + 1, ox, cur.bx, cur.time + 1));
                }
            }
        }
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                int ox = cur.ox + dx[i];
                int bx = cur.bx + dx[j];
                if (ok(ox) && ok(bx) && dist[cur.x][ox][bx] > cur.time + 1) {
                    dist[cur.x][ox][bx] = cur.time + 1;
                    pq.push(node(cur.x, ox, bx, cur.time + 1));
                }
            }
        }
    }
    FAIL;
    return -1;
}

void solve () {
    printf("%d\n", dijkstra());
}

//#define SMALL
#define LARGE
//#define DEBUG

int main() {
#ifdef SMALL                                   
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
#endif
#ifdef LARGE
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        cin >> n;
        for (int i = 0; i < n; ++i) {
            cin >> a[i] >> b[i];
            --b[i];
        }
        solve();
    }

    return 0;
}
