#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#include <complex>
#include <utility>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <numeric>
#include <functional>
using namespace std;

const double PI = acos(-1.0);
const double EPS = 1e-9;

#define MP make_pair
#define PB push_back
#define SIZE(X) ((int)((X).size()))

typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;
typedef vector<int> vint;
typedef vector<int64> vint64;
typedef vector<double> vdouble;
typedef vector<string> vstring;
typedef pair<int, int> pii;
typedef pair<int64, int64> pii64;
typedef pair<double, double> pdd;


int N;
int64 D, V;
pii64 s[205];

inline double Abs(double a) {
    return a >= 0 ? a : -a;
}
inline double dist(double a, double b) {
    return Abs(a - b);
}

int main() {
    int t, casN;
    int i, j;

    scanf("%d", &t);
    for (casN = 1; casN <= t; casN++) {
        scanf("%d%lld", &N, &D);
        V = 0;
        for (i = 0; i < N; i++) {
            scanf("%lld%lld", &s[i].first, &s[i].second);
            V += s[i].second;
        }
        double L = 0.0;
        double R = V * D * 2;
        double M;
        double pM = 1e+100;
        while (R - L > 1e-9) {
            M = (L + R) / 2;
            if (M == pM) break;
            pM = M;
            double curr = s[0].first - M;
            double cost = 0.0;
            for (i = 0; i < N; i++) {
                curr = max(curr, s[i].first - M);
                curr += s[i].second * D;
                if (dist(curr - D, (double)s[i].first) > M) break;
            }
            if (i < N) {
                L = M;
            } else {
                R = M;
            }
        }
        printf("Case #%d: %.9f\n", casN, (L + R) / 2);
    }

    return 0;
}

