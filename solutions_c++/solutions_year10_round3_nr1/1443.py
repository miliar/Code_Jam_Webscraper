/*
 * Author: WHHeV
 * Created Time:  2010/5/23 17:04:09
 * File Name: \Users\WHHeV\Desktop\a.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#ifdef __DEBUG__
#define dp(fmt, x...) fprintf(stderr, "[%d] " fmt "\n", __LINE__, ##x)
#else
#define dp(fmt, x...)
#endif
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
#define MIN(x,y) ((x)<(y)?(x):(y))
#define MAX(x,y) ((x)>(y)?(x):(y))
#define sqr(x) ((x)*(x))
const int maxint = -1u>>1;
const double pi = acos(-1.0);
const long long maxint64 = 0x7FFFFFFFFFFFFFFFLL;
const double eps = 1e-10;
template<class T> T gcd(T a,T b){ if(a<0) return gcd(-a,b);if(b<0) return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}

int a[1010], b[1010];
int N, T;

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++) {
        scanf("%d", &N);
        for (int i = 1; i <= N; i++)
            scanf("%d %d", &a[i], &b[i]);
        int ans = 0;
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (a[i] < a[j] && b[i] > b[j])
                    ans++;
            }
        }
        printf("Case #%d: %d\n", tc, ans);
    }
    return 0;
}

