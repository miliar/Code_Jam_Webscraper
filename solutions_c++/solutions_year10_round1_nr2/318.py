/*
 * Author: ZaviOr
 * Created Time:  2010/5/22 10:52:07
 * File Name: gcj2.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(X) cerr << #X << ": " << (X) << endl
#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
#define MP(X,Y) make_pair(X,Y)
#define PB push_back
#define NEXT(X, N) ((X) == (N)? 0 : (X))
#define ALL(X) (X).begin(), (X).end()
typedef long long LL;
typedef unsigned long long ULL;
#define two(X) (1<<(X))
#define twoL(X) (((LL)(1))<<(X))
#define contain(S,X) ((S)&two(X))
#define containL(S,X) ((S)&twoL(X))
const int maxint = -1u>>1;
const double pi = acos(-1.0);
const double eps = 1e-8;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
template <class T> inline T sqr(T x) {return x * x;}
template <class T> inline T lowbit(T n) {return (n ^ (n - 1)) & n;}
template <class T> inline int countbit(T n) {return (n == 0) ? 0 : ( 1 + countbit(n & (n - 1)));}

int f[101][510];
int v[101];

int abs(int a) {
    return (a > 0) ? a : -a;
}

int main() {
    int T, t = 0;
    for (scanf("%d", &T); T; --T) {
        printf("Case #%d: ", ++t);
        int D, I, m, n;
        scanf("%d%d%d%d", &D, &I, &m, &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d", v + i + 2);
            v[i + 2] += 255;
            out(v[i + 2]);
        }
        memset(f, 0, sizeof(f));
        for (int i = 2; i < n + 2; ++i)
            for (int j = 0; j <= 510; ++j) {
                if (i == 2)
                    f[i][j] = abs(v[i] - j);
                else {
                    f[i][j] = maxint;
                    for (int k = 0; k <= 510; ++k) {
                        if (abs(k - j) <= m)
                            get_min(f[i][j], f[i - 2][k] + abs(j - v[i]) + D);
                        if (abs(k - j) <= m + m)
                            get_min(f[i][j], f[i - 1][k] + abs(j - v[i]) + I);
                    }
                }
            }
        int ans = maxint;
        for (int i = 0; i <= 510; ++i)
            get_min(ans, f[n + 1][i]);
        printf("%d\n", ans);
    }
    return 0;
}

