#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <set>
#include <sstream>

using namespace std;

typedef pair<int, int> pi;
typedef unsigned long long ull;

#define x first
#define y second
#define mp make_pair

const double eps = 1e-7;

void solution(int tstNum) {
    int n, d;
    scanf("%d%d", &n, &d);
    vector<pi> pt(n);
    for (int i = 0; i < n; ++i) {
        scanf("%d%d", &pt[i].x, &pt[i].y);
    }
    double l = 0, r = 1e13;
    for (int tt = 0; tt < 100; ++tt) {
        double m = (r + l) / 2;

        double curr = pt[0].x - m;
        bool can = true;
        for (int i = 0; i < n; ++i) {
            double tm = m;
            if (pt[i].x - curr < -eps) {
                tm -= curr - pt[i].x;                
            }
            if (tm < -eps) {
                can = false;
                break;
            }

            curr = max(curr, pt[i].x - tm);

            curr += (pt[i].y - 1) * d;
            if (curr - pt[i].x > m) {
                can = false;
                break;
            }
            curr += d;
        }
        if (can) {
            r = m;
        } else {
            l = m;
        }
    }
    printf("%lf\n", (r + l) / 2.0);
}

int main() {

    //freopen("in.in", "rt", stdin);
    //freopen("out.out", "wt", stdout);


    freopen("B-small.in", "rt", stdin);
    freopen("B-small.out", "wt", stdout);

    //freopen("B-large.in", "rt", stdin);
    //freopen("B-large.out", "wt", stdout);

    int t = 0;
    scanf("%d", &t);
    for (int tt = 0; tt < t; tt++) {
        printf("Case #%d: ", tt + 1);
        solution(tt);
    }

    return 0;
}