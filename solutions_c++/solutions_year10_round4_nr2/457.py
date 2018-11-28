#define DBGLEVEL 0

#include "std.h"

char buf[1024*1024];

int maxmiss[1024];
int price[10][512];    // [round][match]

LL mem[10][512][10]; // [round][match][skippedlater]

LL go(int r, int m, int s) {
    assert(s < 10 && r < 10 && r >= 0);
    LL& ret = mem[r][m][s];
    if (ret >= 0) return ret;
    DBG(1,V(r)<<V(m)<<V(s));
    if (r == 0) {
	int t1 = 2*m, t2 = t1+1;
	if (s < maxmiss[t1] && s < maxmiss[t2]) ret = 0; // don't need this ticket
	else if (s > maxmiss[t1] || s > maxmiss[t2]) ret = 10000000000LL; // bad
	else ret = price[r][m];
    } else {
	ret = price[r][m] + go(r-1, m*2, s) + go(r-1, m*2+1, s); // if buying it
	ret <?= go(r-1, m*2, s+1) + go(r-1, m*2+1, s+1); // if not;
    }
    DBG(1,V(r)<<V(m)<<V(s) << " ==> " << ret);
    return ret;
}

int main() {
    int T;
    cin >> T; cin.getline(buf, sizeof buf);
    FOR(t, T) {
	cout << "Case #"<<(t+1)<<": ";
	DBG(1,"CASE " << (t+1));
	int p; cin >> p;
	cin.getline(buf,sizeof buf);
	int n = 1<<p;
	FOR(i, n) cin >> maxmiss[i];
	cin.getline(buf,sizeof buf);
	FOR(i, p) {
	    int m = 1<<(p-1-i);
	    assert(m <= n/2);
	    FOR(j, m) cin >> price[i][j];
	    cin.getline(buf,sizeof buf);
	}
	memset(mem, -1, sizeof mem);
	DBG(1, V(p)<<V(n));
	int ret = go(p-1, 0, 0);
	cout << ret;
	cout << endl;
    }
    return 0;
}
