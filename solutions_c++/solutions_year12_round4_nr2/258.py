#define _CRT_SECURE_NO_WARNINGS
#pragma comment (linker, "/STACK:16777216")
#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
#include <cassert>
#include <complex>
using namespace std;

///////////////// macros and typedefs ///////////////////
#define rep(i, n) for (int i = 0, _n = (n); i < _n; ++i)
#define repd(i, n) for (int i = (n)-1; i >= 0; --i)
#define _fill(a, x) memset((a), (x), sizeof((a)))
#define DEB(k) cerr<<"debug: "#k<<"="<<k<<endl;
#define all(c) (c).begin(), (c).end()
#define mp(a, b) make_pair(a, b)
#define l(c) (int)((c).size())
#define sqr(a) ((a)*(a))
#define inf 0x7f7f7f7f
#define pb push_back
#define ppb pop_back
#define x first
#define y second
typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef pair<int,int> pi;

struct quad {
    int X0, Y0, X1, Y1;
    quad(int _x0, int _y0, int _x1, int _y1) {
        X0 = _x0, Y0 = _y0, X1 = _x1, Y1 = _y1;
    }
};

int n;
int r[1000];
int X, Y;
int id[1000];
vector<quad> v;
int retX[1000];
int retY[1000];
int DR;

bool cmp(int i, int j) {
    return r[i] > r[j];
}

bool canPlace(const quad& q, int R) {
    int x = max(DR, q.X0+R);
    int y = max(DR, q.Y0+R);
    int x2 = min(X-DR, q.X1-R);
    int y2 = min(Y-DR, q.Y1-R);
    return x <= x2 && y <= y2;
}

void solveCase(int tc) {
    printf("Case #%d:", tc+1);
    scanf("%d %d %d", &n, &X, &Y);
    rep(i, n) {
        scanf("%d", r+i);
        id[i] = i;
    }
    sort(id, id+n, cmp);
    DR = r[id[0]];
    X += 2*DR;
    Y += 2*DR;
    v.clear();
    v.pb(quad(0, 0, X, Y));
    rep(it, n) {
        int i = id[it];
        int R = r[i];
        int pos = -1;
        int minSide = inf;
        for (int j = 0; j < l(v); j++) {
            const quad& q = v[j];
            int width = q.X1-q.X0;
            int height = q.Y1-q.Y0;
            int mn = min(width, height);
            if (!canPlace(q, R)) continue;
            if (pos == -1 || mn < minSide) {
                minSide = mn;
                pos = j;
            }
        }
        if (pos == -1) throw 1;
        quad q = v[pos];
        v.erase(v.begin()+pos);
        int X = max(DR, q.X0+R);
        int Y = max(DR, q.Y0+R);
        retX[i] = X-DR;
        retY[i] = Y-DR;
        int width = q.X1-q.X0;
        int height = q.Y1-q.Y0;
        if (height <= width) {
            v.pb(quad(q.X0, Y+R, X+R, q.Y1));
            v.pb(quad(X+R, q.Y0, q.X1, q.Y1));
        }
        else {
            v.pb(quad(q.X0, Y+R, q.X1, q.Y1));
            v.pb(quad(X+R, q.Y0, q.X1, Y+R));
        }
    }
    rep(i, n)
        printf(" %d %d", retX[i], retY[i]);
    puts("");
}

void solution()
{
    int tc;
    scanf("%d", &tc);
    rep(i, tc)
        solveCase(i);
}

int main()
{
#ifdef MY_JUDGE
    freopen("B-large.in", "rt", stdin);
    freopen("B-large.out", "wt", stdout);
#endif
    solution();
#ifdef MY_JUDGE
    double time = clock()*1./CLOCKS_PER_SEC;
    fprintf(stderr, "Time: %.2lf sec\n", time);
#endif
    return 0;
} 