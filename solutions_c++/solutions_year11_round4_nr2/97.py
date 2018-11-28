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
#include <cstring>
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

#define MAXN 512

int T,r,c,d, w[MAXN][MAXN], wx[MAXN][MAXN], wy[MAXN][MAXN], spw[MAXN][MAXN], spwx[MAXN][MAXN], spwy[MAXN][MAXN];


bool check(int x, int y, int k) {
	unsigned int sum = 0, mx = 0, my = 0;
	sum = spw[x+k][y+k] - spw[x][y+k] - spw[x+k][y] + spw[x][y];
	mx = spwx[x+k][y+k] - spwx[x][y+k] - spwx[x+k][y] + spwx[x][y];
	my = spwy[x+k][y+k] - spwy[x][y+k] - spwy[x+k][y] + spwy[x][y];
	
	sum -= (w[x][y] + w[x+k-1][y+k-1] + w[x][y+k-1] + w[x+k-1][y]);
	mx -= (x*w[x][y] + (x+k-1)*w[x+k-1][y+k-1] + x*w[x][y+k-1] + (x+k-1)*w[x+k-1][y]);
	my -= (y*w[x][y] + (y+k-1)*w[x+k-1][y+k-1] + (y+k-1)*w[x][y+k-1] + y*w[x+k-1][y]);
	
	unsigned int p = sum*(x+x+k-1), q = sum*(y+y+k-1);
	if (p == 2*mx && q == 2*my) {
//		cout << "ganeee " << x << " " << y << " " << k << endl;
		 return true;	
	}
	return false;
}


bool vale(int k) {
	for(int x = 0; x+k<=r ; x++) for(int y=0; y+k<=c; y++) if (check(x,y,k)) return true;
	return false;	
}


void init() {
	forn(i,r) forn(j,c) {
		wx[i][j] = i*w[i][j];
		wy[i][j] = j*w[i][j];
	}
	
	forn(i,r+1) {
		spwx[i][0] = spwy[i][0] = spw[i][0] = 0;	
	}
	forn(j,c+1) {
		spwx[0][j] = spwy[0][j] = spw[0][j] = 0;	
	}
	
	forsn(i,1,r+1) forsn(j,1,c+1) {
		spw[i][j] = w[i-1][j-1] + spw[i-1][j] + spw[i][j-1] - spw[i-1][j-1];	
		spwx[i][j] = wx[i-1][j-1] + spwx[i-1][j] + spwx[i][j-1] - spwx[i-1][j-1];
		spwy[i][j] = wy[i-1][j-1] + spwy[i-1][j] + spwy[i][j-1] - spwy[i-1][j-1];
	}
}

int main () {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);

	cin >> T;
	forn(rep,T) {
		cin >> r >> c >> d;
		forn(i,r) {
			string s; cin >> s;
			forn(j,c) {
				w[i][j] = s[j]-'0';
			}
		}	
	/*	forn(i,r) {
			forn(j,c) cout << w[i][j] << " "; cout << endl;	
		}
		cout << endl;*/
		
		init();
		
		bool found = false;
		for(int k = min(r,c); k>=3; k--) {
		//	cout << k << endl;
			if (vale(k)) {
				found = true;	
				cout << "Case #" << rep+1 << ": " << k << endl;
				break;
			}
		}
		if (!found) cout << "Case #" << rep+1 << ": IMPOSSIBLE" << endl;
	}

	return 0;
}
