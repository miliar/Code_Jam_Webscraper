//*****************
// LAM PHAN VIET **
// Code Jam - Problem A. RPI
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
#define Parent(i) (i - Last(i))
#define INF 500000000
#define maxN 105
using namespace std;

int n, Win[maxN], Lost[maxN];
double wp[maxN], owp[maxN], oowp[maxN];
char s[maxN][maxN];

void Solve() {
    REP (i, 1, n) {
        Win[i] = Lost[i] = 0;
        REP0 (j, n) {
            if (s[i][j]=='1') Win[i]++;
            else if (s[i][j]=='0') Lost[i]++;
        }
        if (Win[i]+Lost[i]==0) wp[i] = 0;
        else wp[i] = (double)Win[i]/double(Win[i]+Lost[i]);
    }
    REP (i, 1, n) {
        double sumall = 0, Count = (double)Win[i]+Lost[i];
        REP0 (j, n) {
            if (s[i][j]=='.' || (Win[j+1]-1 + Lost[j+1] == 0)) continue;
            if (s[i][j]=='0') sumall += (double)(Win[j+1]-1)/(double)(Win[j+1]+Lost[j+1]-1);
            else sumall += (double)Win[j+1]/(double)(Win[j+1]+Lost[j+1]-1);
        }
        owp[i] = sumall / Count;
    }
    REP (i, 1, n) {
        double sumall = 0, Count = (double)Win[i]+Lost[i];
        REP0 (j, n)
            if (s[i][j]!='.') sumall += owp[j+1];
        oowp[i] = sumall / Count;
    }
    double ans;
    REP (i, 1, n) {
        ans = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
        printf("%.12lf\n", ans);
    }
}

main() {
//    FileIn("test"); FileOut("test");
    int Case;
    scanf("%d", &Case);
    REP (kk, 1, Case) {
        scanf("%d", &n); gets(s[0]);
        REP (i, 1, n) gets(s[i]);
        printf("Case #%d:\n", kk);
        Solve();
    }
}

/* lamphanviet@gmail.com - 2011 */
