//#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <stdio.h>
#include <cstring>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <sstream>
#include <queue>
#include <stack>
#define FOR(i,a,b) for(int i = (a); i <= (b); i++) 
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define FR(i,a) for(int i = 0; i < (a); i++)
#define DR(i,a) for(int i = (a)-1; i >= 0; i--)
#define REP(i,a) for(int i = 0; i < (a); i++)
#define Rep(i,a) for(int i = 0; i < (a); i++)
#define For(i,a,b) for(int i = (a); i <= (b); i++)

#define sqr(x) ((x)*(x))
#define dout debug && cout 
#define ll long long
#define sz size()
#define ull unsigned long long
#define pb push_back
#define oo 1000000009
/* DEBUGGING */
bool debug = false;
/* MAIN PROGRAM */

using namespace std;

/*************************TEMPLATE**********************************/
long long convertToNum(string s)
{
    long long val = 0; FR(i,s.size()) val = val * 10 + s[i] - '0';
    return val;
}
string convertToString(long long a) {
    string res = ""; if (!a) return "0";
    while (a) { res = (char)(a % 10 + 48) + res;  a /= 10; }
    return res;
}
long long GCD(long long x,long long y)  {
    if (!x) return y; if (!y) return x;
    if (x == y) return x; if (x < y) return GCD(x,y%x); else return GCD(x%y,y);
}
long long POW(long long x,long long y,long long Base){
    if (!y) return 1; long long u = POW(x,y/2,Base);
    u = (u * u) % Base;
    if (y & 1) return (u * x) % Base; else return u;
}

//newstate = (newstate-1) & oldstate
/**************************CODE HERE*****************************/
#define maxn 510
int m,n,D;
int a[maxn][maxn];
int s[maxn][maxn];

int get(int i1, int j1, int i2, int j2) {
    return s[i2][j2] - s[i1-1][j2] - s[i2][j1-1] + s[i1-1][j1-1];
}
int res = -1;

bool checkOdd(int curX, int curY, int len) {
    int sumx = 0, sumy = 0;
    FOR(i,curX-len,curX+len)
    FOR(j,curY-len,curY+len) {
        if (i == curX - len && j == curY - len) continue;
        if (i == curX - len && j == curY + len) continue;
        if (i == curX + len && j == curY - len) continue;
        if (i == curX + len && j == curY + len) continue;
        sumx += (curX - i) * a[i][j];
        sumy += (curY - j) * a[i][j];        
    }
    return (sumx == 0 && sumy == 0);
}

void solveOdd() {
    FOR(i,1,m) FOR(j,1,n) {
        int first = 1, last ,mid;
        last = min( min(i-1,m-i), min(j-1,n-j));
        if (first > last) continue;
        
        DOWN(len,last,1)
        if (checkOdd(i,j,len)) {
            res = max(res, len * 2 + 1);
            break;
        }
    }    
}

bool checkEven(int curX, int curY, int len) {
    int sumx = 0, sumy = 0;
    FOR(i,curX-len+1,curX+len)
    FOR(j,curY-len+1,curY+len) {
        if (i == curX - len+1 && j == curY - len+1) continue;
        if (i == curX - len+1 && j == curY + len   ) continue;
        if (i == curX + len   && j == curY - len+1) continue;
        if (i == curX + len   && j == curY + len  ) continue;
        if (i <= curX) sumx += (curX-i+1) * a[i][j];
        else sumx += (curX-i) * a[i][j];
        if (j <= curY) sumy += (curY-j+1) * a[i][j];
        else sumy += (curY-j) * a[i][j];     
    }
    return (sumx == 0 && sumy == 0);
}

void solveEven() {
    FOR(i,1,m) FOR(j,1,n) {
        int first = 1, last ,mid;
        last = min( min(i,m-i), min(j,n-j));
        if (first > last) continue;
        
        DOWN(len,last,2)
        if (checkEven(i,j,len)) {
            res = max(res, len * 2);
            break;
        }
    } 
}
int main() {
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest) {
        cout << "Case #" << test << ": ";
        cin >> m >> n >> D;
        char kt;
        FOR(i,1,m) FOR(j,1,n) {
            cin >> kt;
            a[i][j] = kt - '0';
            s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i][j];
        }
        res = -1;
        solveOdd();
        solveEven();
        if (res == -1) cout << "IMPOSSIBLE" << endl;
        else cout << res << endl;
    }
//    system("pause");
    return 0;
}

