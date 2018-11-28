//*****************
// LAM PHAN VIET **
// UVA
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
#define maxN 10001
using namespace std;

int a[maxN], n, L, H;

int Solve() {
    REP (i, L, H) {
        bool f = true;
        REP (j, 1, n)
            if (i%a[j]==0 || a[j]%i==0);
            else {
                f = false;
                break;
            }
        if (f) return i;
    }
    return 0;
}

main() {
//    FileIn("test"); FileOut("test");
    int Case;
    scanf("%d", &Case);
    REP (kk, 1, Case) {
        scanf("%d %d %d", &n, &L, &H);
        REP (i, 1, n) scanf("%d", &a[i]);
        printf("Case #%d: ", kk);
        int ans = Solve();
        if (ans==0) puts("NO");
        else printf("%d\n", ans);
    }
}

/* lamphanviet@gmail.com - 2011 */
