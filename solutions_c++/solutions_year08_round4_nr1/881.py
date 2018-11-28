#define DBGLEVEL 1

#include "std.h"

char buf[1024*1024];
#define N 10000
int type[N+2];
int chg[N+2];
int val[N+2];
int m;
int leaf;

int mem[N+2][2];

int go(int n, int v) {
    if (mem[n][v] >= 0) return mem[n][v];
    if (n >= leaf) return mem[n][v] = (val[n] == v ? 0 : 99999);
    int c1 = 2*(n+1)-1, c2 = c1+1;
    int r1 = go(c1, v), r2 = go(c2, v);
    int r = 99999;
    

    int orr, andr;

    if (v == 0) {
	orr = go(c1,0) + go(c2,0);
	andr = go(c1,0) <? go(c2,0);
    } else {
	orr = go(c1,1) <? go(c2,1);
	andr = go(c1,1)+go(c2,1);
    }
    if (type[n] == 0) r = orr; else r = andr;
    if (chg[n]) r <?= 1 + (type[n] ? orr : andr);
    return mem[n][v] = r;
}


int main() {
    int T;
    cin >> T; cin.getline(buf, sizeof buf);
    FOR(t, T) {
	memset(mem, -1, sizeof mem);
	cout << "Case #"<<(t+1)<<": ";
	//DBG(1,"CASE " << (t+1));
	cin >> m;
	int v; cin >> v;
	cin.getline(buf,sizeof buf);
	leaf = (m-1)/2;
	FOR(i,m) {
	    if (i<leaf) cin>> type[i] >> chg[i];
	    else cin >> val[i];
	    cin.getline(buf,sizeof buf);
	}
	int r = go(0, v);
	if (r >= 99999) cout << "IMPOSSIBLE";
	else cout << r;

	cout << endl;
    }
    return 0;
}
