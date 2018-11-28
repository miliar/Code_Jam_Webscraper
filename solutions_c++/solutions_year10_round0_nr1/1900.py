/*
 * Author: ZaviOr
 * Created Time:  2010/5/8 23:25:14
 * File Name: gcj1.cpp
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

int n, k;

int main() {
    freopen("gcj1input.txt", "r", stdin);
    freopen("gcj1output.txt", "w", stdout);
    int test, T = 0;
    for (scanf("%d", &test); test; --test) {
        ++T;
        scanf("%d%d", &n, &k);
        int i;
        for (i = 0; i < n; ++i) {
            //cout << i << " " << (1 << i) << endl;
            if ((k / (1 << i)) % 2 == 0)
                break;
        }
        if (i == n)
            printf("Case #%d: ON\n", T);
        else
            printf("Case #%d: OFF\n", T);
    }
    return 0;
}

