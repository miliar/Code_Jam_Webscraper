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
#define maxn 17
#define Base 1000003
int m,n;
vector<int> a[maxn];
int f[maxn][1<<maxn];
int k;
int pos[20][20];

int get(int x, int y,int dirx, int diry) {
    x += dirx; y += diry;
    if (x == 0) x = m;
    if (x == m+1) x = 1;
    if (y == 0) y = n;
    if (y == n+1) y = 1;
    return pos[x][y];
}
int visit(int cur, int state) {
    if (f[cur][state] != -1) return f[cur][state];
    if (!state) return 1;
    f[cur][state] = 0;
    FR(i,a[cur].size()) {
        int j = a[cur][i];
        if (state & (1 << (j-1))) f[cur][state] = (f[cur][state] + visit(cur-1,state - (1 << (j-1)))) % Base;
    }
    return f[cur][state];
}
void solve() {
    memset(f,-1,sizeof(f));
    cout << visit(k,(1<<k)-1) << endl;
}
int main() {
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest) {
        cout << "Case #" << test << ": ";
        cin >> m >> n;
        int cnt = 0;
        k = m * n;
        FOR(i,1,m) FOR(j,1,n) {
            pos[i][j] = ++cnt;
        }
        FOR(i,1,cnt) a[i].clear();
        char kt;
        FOR(i,1,m) FOR(j,1,n) {
            cin >> kt;
            if (kt == '-') {
                a[pos[i][j]].push_back(get(i,j,0,-1));
                a[pos[i][j]].push_back(get(i,j,0,1));
            } else if (kt == '|') {
                a[pos[i][j]].push_back(get(i,j,1,0));
                a[pos[i][j]].push_back(get(i,j,-1,0)); 
            } else if (kt == 92) {
                a[pos[i][j]].push_back(get(i,j,-1,-1));
                a[pos[i][j]].push_back(get(i,j,1,1));
            } else {
                a[pos[i][j]].push_back(get(i,j,1,-1));
                a[pos[i][j]].push_back(get(i,j,-1,1));
            }
        }
        solve();
    }
    return 0;
}

