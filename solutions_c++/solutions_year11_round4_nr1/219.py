#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <deque>
#include <queue>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <string>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <cassert>
using namespace std;

//BEGIN TEMPLATE HERE
typedef long long int64;

#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
//END TEMPLATE HERE

const double eps = 1e-8;

struct T {
    double add, speed, len;

    T() {
    }
    T(double a, double s, double l): add(a), speed(s), len(l) {
    }

    bool operator <(const T &t) const {
        return make_pair(1.0 / speed - 1.0 / add, speed) > make_pair(1.0 / t.speed - 1.0 / t.add, t.speed);
    }
};

double b[3000], e[3000], w[3000];
int n;

bool cmp(const int &x, const int &y) {
    return make_pair(b[x], e[x]) < make_pair(b[y], e[y]);
}

int main() {
    freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
    //freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
    int tests;
    double S, R, X, t;
    scanf("%d", &tests);
    for (int caseId = 1; caseId <= tests; ++caseId) {
        scanf("%lf%lf%lf%lf%d", &X, &S, &R, &t, &n);
        for (int i = 0; i < n; ++i) {
            scanf("%lf%lf%lf", &b[i], &e[i], &w[i]);
            X -= e[i] - b[i];
        }
        vector <T> a;
        a.push_back(T(R, S, X));
        for (int i = 0; i < n; ++i) {
            a.push_back(T(R + w[i], S + w[i], e[i] - b[i]));
        }
        sort(a.begin(), a.end());
        double ans = 0.0;
        for (int i = 0; i < SIZE(a); ++i) {
            if (a[i].len / a[i].add <= t) {
                t -= a[i].len / a[i].add;
                ans += a[i].len / a[i].add;
            } else {
                a[i].len -= t * a[i].add;
                ans += t;
                ans += a[i].len / a[i].speed;
                t = 0.0;
            }
        }
        printf("Case #%d: %.6f\n", caseId, ans);
    }
    return 0;
}

