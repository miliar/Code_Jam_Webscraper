/*
 * Sun May 22 17:13:19 CST 2011
 *
 * @Author: Xiantao Jiao
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
#include <fstream>
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
const int inf = 1000000000;
const double eps = 1e-10;

const int maxn = 1000000 + 100;
int cases, cas = 1;
int n, nbooster, loop;
double tim;
double a[maxn];
double dis[maxn];

struct Node {
    int id; double dist;
    Node(int id, double dist) : id(id), dist(dist) {
    }
    bool operator<(const Node& p) const {
        return dist < p.dist;
    }
};

bool booster[maxn];
double solve() {
    double ret = 0; for (int i = 1; i < n; ++i) {
        if (booster[i - 1]) {
            if (ret >= tim) {
                ret += dis[i];
            } else {
                double need = 2.0 * dis[i];
                if (ret + need >= tim) {
                    double gone = 0.5 * (tim - ret);
                    ret = tim + (dis[i] - gone);
                } else {
                    ret += 2 * dis[i];
                }
            }
        } else {
            ret += 2 * dis[i];
        }
    }
    return ret;
}

int main() {
    for (scanf("%d", &cases); cases--; cas++) {
cerr << "case = " << cas << endl;
        scanf("%d%lf%d%d", &nbooster, &tim, &n, &loop);
        for (int i = 0; i < loop; ++i) {
            scanf("%lf", &a[i]);
        }
        dis[0] = 0; n++; for (int i = 1, k = 0; i < n; ++i, ++k) {
            dis[i] = a[k % loop];
        }
        double accumulate = 0; int pos = -1; for (int i = 1; i < n; ++i) {
            accumulate += 2.0 * dis[i]; if (accumulate >= tim) {
                pos = i; break;
            }
        }
        priority_queue<Node> que;
        if (accumulate == tim) {
            for (int i = pos + 1; i < n; ++i) {
                que.push(Node(i - 1, dis[i]));
            }
        } else if (accumulate > tim) {
            for (int i = pos + 1; i < n; ++i) {
                que.push(Node(i - 1, dis[i]));
            }
            que.push(Node(pos - 1, 0.5 * (accumulate - tim)));
        }
        memset(booster, false, sizeof(booster));
        for ( ; nbooster > 0; --nbooster) {
            if (que.empty()) {
                break;
            }
            int id = que.top().id; que.pop();
            booster[id] = true;
        }
        double ans = solve();
        printf("Case #%d: %.0lf\n", cas, ans);
    }
    return 0;
}
