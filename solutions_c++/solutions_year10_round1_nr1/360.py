/*
 * Author: ZaviOr
 * Created Time:  2010/5/22 9:11:29
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

const int dx[] = {0, 1, 1, 1, 0, -1, -1, -1};
const int dy[] = {1, 1, 0, -1, -1, -1, 0, 1};

const int maxn = 51;
int n, k;
char bd[maxn][maxn];

void print() {
    cout << endl;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j)
            printf("%c", bd[i][j]);
        printf("\n");
    }
    cout << endl;
}

int main() {
    freopen("gcj1.txt", "w", stdout);
    int T, t = 0;;
    for (scanf("%d", &T); T; --T) {
        printf("Case #%d: ", ++t);
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                scanf(" %c", &bd[i][j]);
        //print();
        for (int j = n - 2; j >= 0; --j)
            for (int i = 0; i < n; ++i)
                if (bd[i][j] != '.') {
                    int p = j;
                    while (p + 1 < n && bd[i][p + 1] == '.')
                        ++p;
                    swap(bd[i][j], bd[i][p]);
                    //print();
                }
        //print();
        bool rwin = false, bwin = false;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (bd[i][j] == 'R' && !rwin) {
                    for (int d = 0; d < 8; ++d) {
                        int cnt = 0, tx = i, ty = j;
                        while (tx >= 0 && tx < n && ty >= 0 && ty < n) {
                            if (bd[tx][ty] == 'R')
                                ++cnt;
                            else
                                break;
                            tx = tx + dx[d];
                            ty = ty + dy[d];
                        }
                        if (cnt >= k) {
                            rwin = true;
                            break;
                        }
                    }
                }
                if (bd[i][j] == 'B' && !bwin) {
                    for (int d = 0; d < 8; ++d) {
                        int cnt = 0, tx = i, ty = j;
                        while (tx >= 0 && tx < n && ty >= 0 && ty < n) {
                            if (bd[tx][ty] == 'B')
                                ++cnt;
                            else
                                break;
                            tx = tx + dx[d];
                            ty = ty + dy[d];
                        }
                        if (cnt >= k) {
                            bwin = true;
                            break;
                        }
                    }
                }
                if (rwin && bwin)
                    break;
            }
            if (rwin && bwin)
                break;
        }
        if (rwin && bwin)
            printf("Both\n");
        if (rwin && !bwin)
            printf("Red\n");
        if (!rwin && bwin)
            printf("Blue\n");
        if (!rwin && !bwin)
            printf("Neither\n");
    }
    return 0;
}


