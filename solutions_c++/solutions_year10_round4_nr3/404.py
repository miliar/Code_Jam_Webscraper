#include <string>
#include <string.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cassert>
using namespace std;

/*PREWRITTEN CODE BEGINS HERE*/
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define SIZE(x) ( (int)((x).size()) )
#define CS c_str()
#define EL printf("\n")

#define ALL(v) (v).begin(), (v).end()
#define REP(i,n) for(int i=0,_n=(n); i<_n; ++i)
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; --i)
#define VAR(a,b) __typeof (b) a=b
#define FORE(i,a)  for(VAR(i,(a).begin()); i!=(a).end(); ++i)

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long long> VLL; 
typedef vector<vector<int> > VVI;
typedef vector<vector<string> > VVS;
/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/

/*
int doit(set<PII> &s)
{
	set<PII> front, back;

	FORE(p, s) {
		int x = (*p).F , y = (*p).S;
		
		if(!s.count( MP(x-1, y)) && !s.count(MP(x, y-1)))
			back.insert(*p);
		if(s.count(MP(x+1, y-1) || s.count(MP(x, y+1))) )
			front.insert(*p);
	}

	set<PII> new_front, new_back;
	while( SIZE(s) ) {
		new_back.clear(); new_front.clear();
		FORE(p, back) {
			int x = (*p).F , y = (*p).S;	
			if( 
	}
} */

int tab[2000][2000], T;

int mn_x, mx_x, mn_y, mx_y;
int update_range()
{
	int n_mn_x, n_mn_y, n_mx_x, n_mx_y;
	int ret = 0;
	n_mn_x = n_mn_y = INF;
	n_mx_x = n_mx_y = -INF;
	
	FOR(y, mn_y, mx_y+1) FOR(x, mn_x, mx_x+1)
		if(tab[y][x] == T) {
			++ret;
			n_mn_x = min(n_mn_x, x); n_mx_x = max(n_mx_x, x);
			n_mn_y = min(n_mn_y, y); n_mx_y = max(n_mx_y, y);
		}
	
	mn_x = n_mn_x; mn_y = n_mn_y;
	mx_x = n_mx_x; mx_y = n_mx_y;
	return ret;
}

void deb() {
	printf(" mn_x: %d mx_x: %d mn_y: %d mx_y: %d\n", mn_x, mx_x, mn_y, mx_y);
}
void solve()
{
	int R;
	
	T++;
	set<PII> s;

	mn_x = mn_y = INF;
	mx_x = mx_y = -INF;
	scanf("%d", &R);
	REP(i, R) {
		int x0, y0, x1, y1;
		scanf("%d %d %d %d",&x0, &y0, &x1, &y1);
		if(x0 > x1) swap(x0, x1);
		if(y0 > y1) swap(y0, y1);
		
		mn_x = min(mn_x, x0); mx_x = max(mx_x, x1);
		mn_y = min(mn_y, y0); mx_y = max(mx_y, y1);
		FOR(y, y0, y1) FOR(x, x0, x1) tab[y][x] = T;
	}
	
//	FOR(y, 0, 4) { FOR(x, 0, 5) printf("%d", (tab[y][x]==T)); printf("\n"); }
//	deb();
	int cnt = 0;
	while(1) {
	 	int left = update_range();
		//printf("left: %d\n", left);
		if(left == 0) break;
		
		//FOR(y, 0, 4) { FOR(x, 0, 5) printf("%d", (tab[y][x]==T)); printf("\n"); } printf("---\n");
		FORD(y, mx_y, mn_y) FORD(x, mx_x, mn_x) {
			if(tab[y][x] == T &&  (tab[y-1][x] != T && tab[y][x-1] != T) )
				{ tab[y][x] = 0;  }
			else if(tab[y-1][x] == T && tab[y][x-1] == T)
				tab[y][x] = T;
		}

		//FOR(y, 0, 4) { FOR(x, 0, 5) printf("%d", (tab[y][x]==T)); printf("\n"); }
		++cnt;
	}
	
	printf("%d\n", cnt);
	//return doit(s);
}

int main(void)
{
	int T = RI();
	FOR(i,1,T) {
		printf("Case #%d: ", i);
        solve();
	}
	return (0);
}
