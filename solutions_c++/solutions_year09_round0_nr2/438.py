#include <iomanip>
#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
#include <cassert>
#include <bitset>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cout << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<tint> vt;
typedef vector<vt> vvt;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

#define MAXL 102

const int di[4] = {-1,0,0,1}, dj[4] = {0,-1,1,0};

int m,n,nbas,land[MAXL][MAXL],bas[MAXL][MAXL];

int paint(int i, int j) {
	if (bas[i][j] != -1) return bas[i][j];

	int bi,bj,bh = land[i][j];
	forn(d,4) {
		int ni = i + di[d], nj = j + dj[d];
		if (ni < 0 || ni >= m || nj < 0 || nj >= n || land[ni][nj] >= bh) continue;
		bi = ni; bj = nj; bh = land[ni][nj];
	}

	if (bh == land[i][j]) return bas[i][j] = nbas++;
	return bas[i][j] = paint(bi,bj);
}

void init() {
	forn(i,m) forn(j,n) bas[i][j] = -1;
	nbas = 0;
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int ncas; cin >> ncas;
	forsn(cas,1,ncas+1) {
		cin >> m >> n; init();
		forn(i,m) forn(j,n) cin >> land[i][j];

		cout << "Case #" << cas << ":" << endl;
		forn(i,m) {
			forn(j,n) {
				if (j) cout << ' ';
				cout << char('a'+paint(i,j));
			}
			cout << endl;
		}
	}
}
