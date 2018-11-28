/*
 * Author: ZaviOr
 * Created Time:  2010/5/8 10:58:44
 * File Name: gcj3.cpp
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

const int maxn = 1100;

LL next[maxn], cost[maxn], r, k, n, num[maxn];
bool vis[maxn];

int main() {
    freopen("gcj3input.txt", "r", stdin);
    freopen("gcj3output.txt", "w", stdout);
    int test, T = 0;
    for (scanf("%d", &test); test; --test) {
        T++;
        scanf("%I64d%I64d%I64d", &r, &k, &n);
        for (int i = 0; i < n; ++i)
            scanf("%I64d", num  + i);
        memset(vis, false, sizeof(vis));
        memset(cost, 0, sizeof(cost));

        LL p = 0, start = -1, ans = 0;
        while (r > 0) {
            if (vis[p]) {
                if (start == -1) {
                    start = p;
                    LL sum = 0, path = 0;
                    do {
                        sum += cost[p];
                        p = next[p];
                        path++;
                    } while (p != start);
                    ans += sum * (r / path);
                    r = r % path;
                } else {
                    ans += cost[p];
                    p = next[p];
                    --r;
                }
            }
            else {
                vis[p] = true;
                LL tmp = p, tot = 0;
                for (int i = 0; i < n; ++i)
                    if (num[p] + tot <= k) {
                        tot += num[p];
                        p = NEXT(p + 1, n);
                    } else break;
                next[tmp] = p;
                cost[tmp] = tot;
                ans += tot;
                --r;
            }
        }
        printf("Case #%d: %I64d\n", T, ans);
    }
    return 0;
}

