#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cstring>
//#include <conio.h>

using namespace std;

#define X first
#define Y second
#define pb push_back
#define sqr(a) ((a)*(a))
#define FR(i,n) for (int i = 0; i < (n); i++)
#define DN(i,a) for(int i = (a)-1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define oo 1000000000
#define MAXN 10005
#define esl 0.0

typedef pair<int, int> PII;
typedef vector<int> VI;

double resX[MAXN], resY[MAXN];
int n, W, L;
PII r[MAXN];

bool cmp(int i, int j) {
    return i > j;
}
int main () {
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int ntest;
    cin >> ntest;
    bool swaped;
    FOR(test, 1, ntest) {
        cin >> n >> W >> L;
        printf("Case #%d: ", test);
        swaped = 0;
        if (W > L) {
            swap(W, L);
            swaped = 1;
        }
        FOR(i, 1, n) {
            cin >> r[i].X;
            r[i].Y = i;
        }
        sort(r + 1, r + n + 1);
        int j = 1;
        double cur = 0;
        double h = 0, hh = 0;
        FOR(i, 1, n) {
            if (cur + r[i].X + esl > L) {
                j++;
                cur = 0;
                h = hh;
            }
            double kk = h + r[i].X;
            if (j == 1) kk = 0.0;
            int ii = r[i].Y;
            if (cur <= esl) {
                resY[ii] = 0.0;
                resX[ii] = kk;
            }
            else {
                resY[ii] = cur + r[i].X;
                resX[ii] = kk;
            }
            cur = resY[ii] + r[i].X;
            hh = max(hh, h + 2 * r[i].X + esl);
        }
        if (swaped) {
            FOR(i, 1, n) swap(resX[i], resY[i]);
            swap(W, L);
        }
        FOR(i, 1, n) if (resX[i] > W || resY[i] > L) cout << i << ' ' << "ngu vai" << endl << resX[i] << ' ' << W << ' ' << resY[i] << ' ' << L << endl;
        FOR(i, 1, n) printf("%.1lf %.1lf ", resX[i], resY[i]);
        printf("\n");
    }
    return 0;
}
