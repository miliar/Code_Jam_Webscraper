/*
 * Author: ZaviOr
 * Created Time:  2011/6/4 22:06:28
 * File Name: A.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <numeric>
#include <sstream>
#include <string>
using namespace std;
#define out(X) cerr << #X << ": " << (X) << endl
#define SZ(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
#define REP(I,N) for (int I = 0; I < (N); ++I)
#define FOR(I,L,H) for (int I = (L); I < (H); ++I)
#define for_each(I,V) for (typeof(V.begin()) I = V.begin(); I != V.end(); ++I)
#define MP(X,Y) make_pair((X),(Y))
#define PB push_back
#define ALL(X) X.begin(), X.end()
typedef long long LL;

int b[1001], e[1001], w[1001];

double gao() {
    int s, r, n;
    double x, t;
    scanf("%lf%d%d%lf%d", &x, &s, &r, &t, &n);
    REP(i, n) {
        cin >> b[i] >> e[i] >> w[i];
        x -= e[i] - b[i];
    }
    double ans = 0.0;
    if (r * t >= x) {
        ans += x / r;
        t -= ans;
    } else {
        ans += t + (x - r * t) / s;
        t = 0;
    }
    REP(i, n) {
        if (t > 0) {
            double l = t * (r + w[i]);
            if (l >= (e[i] - b[i])) {
                t -= (0.0 + e[i] - b[i]) / (r + w[i]);
                ans += (0.0 + e[i] - b[i]) / (r + w[i]);
            } else {
                double tmp = 0.0 + e[i] - b[i] - l;
                ans += t;
                t = 0;
                ans += tmp / (w[i] + s);
            }
        } else {
            ans += (0.0 + e[i] - b[i]) / (w[i] + s);
        }
    }
    return ans;
}

int main() {
    int T, t = 0;
    cin >> T;
    while (t++ < T) {
        printf("Case #%d: %f\n", t, gao());
    }
    return 0;
}

