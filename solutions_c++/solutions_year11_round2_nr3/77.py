#pragma comment(linker, "/STACK:16777216")

#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define FORD(i,a,b) for (int i = (int)(a)-1; i >= (int)(b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPD(i,a) FORD(i,a,0)
#define SQR(a) (a)*(a)
#define MP make_pair
#define PB push_back
#define FILL(a) memset(a,0,sizeof(a));
#define SIZE(a) (int)((a).size())
#define ALL(a) (a).begin(),(a).end()
#define LL long long
const double PI = 2*acos(0.0);
const double EPS = 1e-12;
const int INF = 1000000000;

vector<int> v[10];
int tc, n, m, q;
int a[10], b[10];
bool g[8][8], u[8][8], issol;
int tek[10], sol[10];
bool used[10];

void finishwall (vector<int> &a){
	int tek = a[1];
	while (tek != a[0]){
		int nx = ((a[a.size()-2]+n-1)%n);
		while (!g[tek][nx]) nx = (nx+n-1)%n;
		u[tek][nx] = true;
		tek = nx;
		if (tek != a[0]) a.PB(tek);
	};
};

void check(int colors){
	memset (used, 0, sizeof (used));
	REP(i,n) used[tek[i]] = true;
	REP(i,colors) if (!used[i]) return;
	REP(i,q){
		memset (used, 0, sizeof (used));
		REP(j,v[i].size()) used[tek[v[i][j]]] = true;
		REP(i,colors) if (!used[i]) return;
	};
	issol = true;
	REP(i,n) sol[i] = tek[i];
};

void recit (int p, int colors){
	if (issol) return;
	if (p==n){
		check(colors);
		return;
	};
	REP(i,colors){
		tek[p] = i;
		recit (p+1, colors);
	};
};

bool cancolor (int colors){
	issol = false;
	recit (0, colors);
	return issol;
};

int main(){
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	cin >> tc;
	REP(ic,tc){
		cin >> n >> m;
		REP(i,m) cin >> a[i];
		REP(i,m) cin >> b[i];
		memset (u, false, sizeof (u));
		memset (g, false, sizeof (g));
		REP(i,n) g[i][(i+1)%n] = true;
		REP(i,m) g[a[i]-1][b[i]-1] = true;
		REP(i,m) g[b[i]-1][a[i]-1] = true;
		q = 0;
		REP(i,n) REP(j,n) if (i!=j && g[i][j] && !u[i][j]){
			v[q].clear();
			v[q].push_back(i);
			v[q].push_back(j);
			finishwall (v[q]);
			++q;
		};
		int mx = v[0].size();
		for (int i = 1; i < q; ++i) mx = min (mx, (int)v[i].size());
		while (!cancolor(mx)) --mx;
		printf ("Case #%d: %d\n", ic+1, mx);
		REP(i,n){ if (i) printf (" ");
			printf ("%d", sol[i]+1);
		};
		printf ("\n");
	};
	return 0;
};