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
#include <sstream>
#include <iomanip>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)
#define ll long long
#define F first
#define S second
#define PB push_back
#define MP make_pair
using namespace std;

const double PI = acos(-1.0);

int m, n, res;
char a[10][10];
pair<int,int> to[2][10][10];

pair<int,int> refine(int u, int v) {
    pair<int,int> a = MP(u,v);
    if (a.F < 1) a.F = m;
    if (a.F > m) a.F = 1;
    if (a.S < 1) a.S = n;
    if (a.S > n) a.S = 1;
    return a;
}

int kq[10][10];
bool mark[10][10];

void update() {
    FOR(i,1,m) FOR(j,1,n) {
        memset(mark, 0, sizeof mark);
        mark[i][j] = 1;
        int u = to[kq[i][j]][i][j].F, v = to[kq[i][j]][i][j].S;
        while (!mark[u][v]) {
            mark[u][v] = 1;
            int uu = to[kq[u][v]][u][v].F, vv = to[kq[u][v]][u][v].S;
            u = uu; v = vv;
        }
        if (u != i || v != j) return ;
    }
    res++;
}

void attempt(int i, int j) {
    if (i > m || j > n) {
        update();
        return ;
    }
    FOR(now,0,1) {
        kq[i][j] = now;
        if (j < n) attempt(i,j+1);
        else attempt(i+1,1);
    }
}

int main() {
    freopen("C-small.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test; scanf("%d", &test);
    FOR(t,1,test) {
        cerr << "t = " << t << endl;
        scanf("%d %d", &m, &n);
        FOR(i,1,m) FOR(j,1,n) {
            char c = '@';
            while (c != '|' && c != '-' && c != '/' && c != '\\') cin >> c;
            if (c == '|') {
                to[0][i][j] = refine(i-1,j);
                to[1][i][j] = refine(i+1,j);
            }
            else if (c == '-') {
                to[0][i][j] = refine(i,j-1);
                to[1][i][j] = refine(i,j+1);
            }
            else if (c == '\\') {
                to[0][i][j] = refine(i-1,j-1);
                to[1][i][j] = refine(i+1,j+1);
            }
            else if (c == '/') {
                to[0][i][j] = refine(i-1,j+1);
                to[1][i][j] = refine(i+1,j-1);
            }
            else cerr << "???\n";
        }
        cerr << "inp\n";
        res = 0;
        attempt(1,1);
        printf("Case #%d: %d\n", t, res);
    }
    return 0;
}