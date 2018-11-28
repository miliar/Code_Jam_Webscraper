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
typedef pair<double, double> pdd;

int N;
char s[105][105];

inline double RPI(double WP, double OWP, double OOWP) {
    return 0.25 * WP + 0.50 * OWP + 0.25 * OOWP;
}

int main() {
    int t, casN;
    int i, j;

    double aa[105][105];
    double a[105];
    double b[105];
    double c[105];
    int cnt;

    scanf("%d", &t);
    for (casN = 1; casN <= t; casN++) {
        scanf("%d", &N);
        for (i = 0; i < N; i++) {
            scanf("%s", s[i]);
        }
        for (i = 0; i < N; i++) {
            a[i] = 0;
            cnt = 0;
            for (j = 0; j < N; j++) {
                if (s[i][j] == '.') continue;
                if (s[i][j] == '1') a[i] += 1.0;
                cnt++;
            }
            a[i] /= cnt;
        }
        for (i = 0; i < N; i++) {
            for (j = 0; j < N; j++) {
                aa[i][j] = 0;
                cnt = 0;
                for (int k = 0; k < N; k++) {
                    if (k == j) continue;
                    if (s[i][k] == '.') continue;
                    if (s[i][k] == '1') aa[i][j] += 1.0;
                    cnt++;
                }
                aa[i][j] /= cnt;
            }
        }
        for (i = 0; i < N; i++) {
            b[i] = 0;
            cnt = 0;
            for (j = 0; j < N; j++) {
                if (s[i][j] == '.') continue;
                b[i] += aa[j][i];
                cnt++;
            }
            b[i] /= cnt;
        }
        for (i = 0; i < N; i++) {
            c[i] = 0;
            cnt = 0;
            for (j = 0; j < N; j++) {
                if (s[i][j] == '.') continue;
                c[i] += b[j];
                cnt++;
            }
            c[i] /= cnt;
        }
        printf("Case #%d:\n", casN);
        for (i = 0; i < N; i++) {
            printf("%.9f\n", RPI(a[i], b[i], c[i]));
        }
    }

    return 0;
}

