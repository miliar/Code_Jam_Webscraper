#include <sstream>
#include <iomanip>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <deque>
#include <complex>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)
#define FORN(i,a,b) for(int i=(a),_b=(b);i<_b;i++)
#define DOWN(i,a,b) for(int i=a,_b=(b);i>=_b;i--)
#define SET(a,v) memset(a,v,sizeof(a))
#define sqr(x) ((x)*(x))
#define ll long long
#define F first
#define S second
#define PB push_back
#define MP make_pair

#define DEBUG(x) cout << #x << " = "; cout << x << endl;
#define PR(a,n) cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl;
#define PR0(a,n) cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl;
using namespace std;

//Buffer reading
int INP,AM,REACHEOF;
#define BUFSIZE (1<<12)
char BUF[BUFSIZE+1], *inp=BUF;
#define GETCHAR(INP) { \
    if(!*inp) { \
        if (REACHEOF) return 0;\
        memset(BUF,0,sizeof BUF);\
        int inpzzz = fread(BUF,1,BUFSIZE,stdin);\
        if (inpzzz != BUFSIZE) REACHEOF = true;\
        inp=BUF; \
    } \
    INP=*inp++; \
}
#define DIG(a) (((a)>='0')&&((a)<='9'))
#define GN(j) { \
    AM=0;\
    GETCHAR(INP); while(!DIG(INP) && INP!='-') GETCHAR(INP);\
    if (INP=='-') {AM=1;GETCHAR(INP);} \
    j=INP-'0'; GETCHAR(INP); \
    while(DIG(INP)){j=10*j+(INP-'0');GETCHAR(INP);} \
    if (AM) j=-j;\
}
//End of buffer reading

const long double PI = acos((long double) -1.0);

char a[11][11];

bool full() {
    FOR(i,1,4) FOR(j,1,4) if (a[i][j] == '.') return false;
    return true;
}

bool good(char a, char b, char c, char d, char need) {
    int cntT = 0, cntGood = 0;
    if (a == 'T') ++cntT; else if (a == need) ++cntGood;
    if (b == 'T') ++cntT; else if (b == need) ++cntGood;
    if (c == 'T') ++cntT; else if (c == need) ++cntGood;
    if (d == 'T') ++cntT; else if (d == need) ++cntGood;

    if (cntT + cntGood == 4) return true;
    else return false;
}

bool check(char c) {
    FOR(i,1,4) {
        if (good(a[i][1], a[i][2], a[i][3], a[i][4], c)) return true;
        if (good(a[1][i], a[2][i], a[3][i], a[4][i], c)) return true;
    }
    if (good(a[1][1], a[2][2], a[3][3], a[4][4], c)) return true;
    if (good(a[4][1], a[3][2], a[2][3], a[1][4], c)) return true;
    return false;
}

int main() {
    int ntest; scanf("%d\n", &ntest);
    FOR(test,1,ntest) {
        FOR(i,1,4) scanf("%s\n", &a[i][1]);

        printf("Case #%d: ", test);

        if (check('X')) puts("X won");
        else if (check('O')) puts("O won");
        else if (full()) puts("Draw");
        else puts("Game has not completed");
    }
    return 0;
}

