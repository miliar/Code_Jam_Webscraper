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
typedef vector<pii> vpii;

struct XD {
    double st, ed, w;
    XD() {}
    XD(double _st, double _ed, double _w): st(_st), ed(_ed), w(_w) {}
};
struct cmp_st {
    bool operator()(const XD &a, const XD &b) {
        return a.st < b.st;
    }
};
struct cmp_w {
    bool operator()(const XD &a, const XD &b) {
        return a.w < b.w;
    }
};

int X, T, N;
int S, R;
XD s[1005];
XD v[100005];
int ptr;

int main() {
    int t, casN;

    scanf("%d", &t);
    for (casN = 1; casN <= t; casN++) {
        scanf("%d%d%d%d%d", &X, &S, &R, &T, &N);
        for (int i = 0; i < N; i++) {
            scanf("%lf%lf%lf", &s[i].st, &s[i].ed, &s[i].w);
            s[i].w += S;
        }
        sort(s, s + N, cmp_st());
        ptr = 0;
        int curr = 0;
        for (int i = 0; i < N; i++) {
            if (s[i].st > curr) {
                v[ptr++] = XD(curr, s[i].st, S);
            }
            v[ptr++] = s[i];
            curr = s[i].ed;
        }
        if (curr != X) v[ptr++] = XD(curr, X, S);
        double TT = T;
        R -= S;
        sort(v, v + ptr, cmp_w());
        for (int i = 0; i < ptr; i++) {
            if (T == 0) break;
            double uT = (v[i].ed - v[i].st) / (v[i].w + R);
            if (TT - uT >= 0.0) {
                v[i].w += R;
                TT -= uT;
            } else {
                TT *= (v[i].w + R);
                v[ptr++] = XD(v[i].st + TT, v[i].ed, v[i].w);
                v[i] = XD(v[i].st, v[i].st + TT, v[i].w + R);
                break;
            }
        }
        sort(v, v + ptr, cmp_st());
        double ans = 0;
        for (int i = 0; i < ptr; i++) {
            //cerr << "--> " << v[i].st << " " << v[i].ed << " " << v[i].w << endl;
            ans += (double)(v[i].ed - v[i].st) / (double)(v[i].w);
        }
        printf("Case #%d: %.9f\n", casN, ans);
    }

    return 0;
}

