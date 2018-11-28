/*
 * Author: ZaviOr
 * Created Time:  2010/5/22 10:08:05
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

bool check(int a, int b) {
    if(a < b) 
        swap(a, b);
    if(a == b) 
        return false;
    if(a % b == 0) 
        return true;
    if(a / b >= 2) 
        return true;
    if(check(b, a - b)) 
        return false;
    return true;
}


int main() {
    freopen("gcj3.txt", "w", stdout);
    int T, t = 0;
    for (scanf("%d", &T); T; --T) {
        printf("Case #%d: ", ++t);
        int a1, a2, b1, b2;
        scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
        LL ans = 0;
        for (int i = a1; i <= a2; ++i)
            for (int j = b1; j <= b2; ++j) {
                //printf("%d %d\n", i, j);
                if (check(i, j))
                    ans++;
        }                    
        printf("%I64d\n", ans);
    }

    return 0;
}

