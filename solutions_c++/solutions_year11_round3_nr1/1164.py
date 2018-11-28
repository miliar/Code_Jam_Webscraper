//*****************
// LAM PHAN VIET **
// Code Jam - Problem A. Square Tiles
// Time limit:
//********************************
#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <string>
#include <vector>

#define FileIn(file) freopen(file".inp", "r", stdin)
#define FileOut(file) freopen(file".out", "w", stdout)
#define REP(i, a, b) for (int i=a; i<=b; i++)
#define REP0(i, n) for (int i=0; i<n; i++)
#define Fill(ar, val) memset(ar, val, sizeof(ar))
#define PI 3.1415926535897932385
#define uint64 unsigned long long
#define int64 long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define bit(n) (1<<(n))
#define Last(i) (i & -i)
#define INF 500000000
#define maxN 100
using namespace std;

int n, m;
char s[maxN][maxN];

bool isOK(int x, int y) {
    return (x>=0 && x<n && y>=0 && y<m);
}

bool FillRed(int i, int j) {
    s[i][j] = '/';
    if (isOK(i, j+1) && s[i][j+1]=='#') s[i][j+1] = '\\';
    else return false;
    if (isOK(i+1, j) && s[i+1][j]=='#') s[i+1][j] = '\\';
    else return false;
    if (isOK(i+1, j+1) && s[i+1][j+1]=='#') s[i+1][j+1] = '/';
    else return false;
    return true;
}

bool Solve() {
    REP0 (i, n) {
        REP0 (j, m)
            if (s[i][j]=='#') {
                int k = FillRed(i, j);
                if (!k) return false;
            }
    }
    return true;
}

main() {
//    FileIn("test"); FileOut("test");
    int Case;
    scanf("%d", &Case);
    REP (kk, 1, Case) {
        scanf("%d %d", &n, &m); gets(s[0]);
        REP0 (i, n) gets(s[i]);
        bool ans = Solve();
        printf("Case #%d:\n", kk);
        if (!ans) puts("Impossible");
        else {
            REP0 (i, n) puts(s[i]);
        }
    }
}

/* lamphanviet@gmail.com - 2011 */
