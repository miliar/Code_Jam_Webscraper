#include<algorithm>
#include<cassert>
#include<complex>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<string>
#include<vector>
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,n) for(int i=0;i<(n);++i)
#define fup FOR
#define fdo FORD
#define VAR(v,i) __typeof(i) v=(i)
#define FORE(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define ALL(x) (x).begin(),(x).end()
#define SIZE(x) ((int)(x).size())
#define siz SIZE
#define CLR memset((x),0,sizeof (x))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define SQR(a) ((a)*(a))

#define DEBUG 1
#define debug(x) {if(DEBUG) cerr << #x << " = " << x << endl;}
#define debugv(x) {if(DEBUG) {cerr << #x << " = "; FORE(it,(x)) cerr << *it << " . "; cerr  <<endl;}}

using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef VI vi;
typedef LL lli;

const int inf = 1000000000;

int tab[600][600];
int xx[600][600];
int yy[600][600];
int ss[600][600];
int x[600][600];
int y[600][600];
int s[600][600];

void solve(int tcase) {
    printf("Case #%d: ", tcase);
    int r,c,d;
    scanf("%d%d%d", &r, &c, &d);
    char ch = getchar();
    REP(i, r) {
        while (ch < '0' || ch > '9') ch = getchar();
        REP(j, c) {
            tab[i][j] = ch - '0';
            x[i][j] = y[i][j] = 0;
            ch = getchar();
            xx[i][j] = tab[i][j]*i;
            yy[i][j] = tab[i][j]*j;
            ss[i][j] = tab[i][j];
        }
    }
    REP(i, r+5) REP(j, c+5) x[i][j]=y[i][j] = 0;
    FOR(i,1, r) FOR(j ,1, c) {
        x[i][j] = x[i-1][j];
        y[i][j] = y[i-1][j];
        s[i][j] = s[i-1][j];
        x[i][j] += (i-1)*tab[i-1][j-1];
        y[i][j] += (j-1)*tab[i-1][j-1];
        s[i][j] += tab[i-1][j-1];
    }
    FOR(i,1, r) FOR(j ,1, c) {
        x[i][j] += x[i][j-1];
        y[i][j] += y[i][j-1];
        s[i][j] += s[i][j-1];
    }
  /*  REP(i, r+1) {
        REP(j, c+1) {
            printf("%.3d ", s[i][j]);
        }
        printf("\n");

    }*/
    int cnt = 0;
    int m = min(r,c);
    FORD(k, m, 3) {
        FOR(i, 0, r-k) FOR(j, 0, c-k) {
            int X = x[i+k][j+k]+x[i][j]-x[i+k][j] - x[i][j+k] - xx[i][j] - xx[i+k-1][j] - xx[i][j+k-1]-xx[i+k-1][j+k-1];
            int Y = y[i+k][j+k]+y[i][j]-y[i+k][j] - y[i][j+k] - yy[i][j] - yy[i+k-1][j] - yy[i][j+k-1]-yy[i+k-1][j+k-1];
            int S = s[i+k][j+k]+s[i][j]-s[i+k][j] - s[i][j+k] - ss[i][j] - ss[i+k-1][j] - ss[i][j+k-1]-ss[i+k-1][j+k-1];
                ++cnt;
            if (2*X == S*(2*i+k-1) && 2*Y ==  S*(2*j+k-1)) {
                ++cnt;
                printf("%d\n", k);
                return;
            }


        }
    }
   // printf("%d\n", cnt);
    printf("IMPOSSIBLE\n");
    return;

}

int main() {
    int t;
    scanf("%d", &t);
    REP(i, t) solve(i+1);
    return 0;
}
