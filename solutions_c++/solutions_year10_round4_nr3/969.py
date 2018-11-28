/*
 * Author: ZaviOr
 * Created Time:  2010/6/5 22:09:54
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
int dx[] = {-1,0,1,0,1,1,-1,-1};
int dy[] = {0,1,0,-1,1,-1,1,-1};
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
template <class T> inline T sqr(T x) {return x * x;}
template <class T> inline T lowbit(T n) {return (n ^ (n - 1)) & n;}
template <class T> inline int countbit(T n) {return (n == 0) ? 0 : ( 1 + countbit(n & (n - 1)));}

int mat[110][110];

void output(int x, int y) {
    for (int i = 1; i <= x; ++i) {
        for (int j = 1; j <= y; ++j)
            printf("%d", mat[i][j]);
        printf("\n");
    }
    printf("\n");
}

int main() {
    freopen("gcj2.out", "w", stdout);
    int T, t = 0;
    for (scanf("%d", &T); T; --T) {
        int n, x1, y1, x2, y2;
        memset(mat, 0, sizeof(mat));
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            for (int x = x1; x <= x2; ++x)
                for (int y = y1; y <= y2; ++y)
                    mat[x][y] = 1;
        }
        bool flag;
        int ans = 0;
        do {
            //output(5, 5);
            flag = false;
            for (int i = 100; i >= 1; --i)
                for (int j = 100; j >= 1; --j)
                    if (mat[i][j]) {
                        if (!mat[i - 1][j] && !mat[i][j - 1])
                            mat[i][j] = 0;
                        if (mat[i][j])
                            flag = true;
                    } else {
                        if (mat[i - 1][j] && mat[i][j - 1])
                            mat[i][j] = 1;
                        if (mat[i][j])
                            flag = true;
                    }
            ++ans;
            //out(ans);
            //out(flag);
        } while (flag);
        printf("Case #%d: %d\n", ++t, ans);
    }
    return 0;
}

