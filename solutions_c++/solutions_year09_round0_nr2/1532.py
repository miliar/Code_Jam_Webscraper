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

int h,w,t;
int mapa[128][128];

bool valid(int u, int v) { return ( (u>=0) && (v>=0) && (u<h) && (v<w) ); }

int mover(int u, int v) {
	int ans = -1, minimo = 100000000,valtmp;

	if (valid(u-1,v)) {
		valtmp = mapa[u-1][v];
		if ( (valtmp< mapa[u][v]) && (valtmp < minimo) ) {
		minimo = valtmp;	
		ans = 0;
		}
	}	
	
	if (valid(u,v-1) ) {
		valtmp = mapa[u][v-1];
		if ( (valtmp< mapa[u][v]) && (valtmp < minimo) ) {
		minimo = valtmp;	
		ans = 1;
		}
	}
	
	if (valid(u,v+1) ) {
		valtmp = mapa[u][v+1];
		if ( (valtmp< mapa[u][v]) && (valtmp < minimo) ) {
		minimo = valtmp;	
		ans = 2;
		}
	}
	
	if (valid(u+1,v) ) { 
		valtmp = mapa[u+1][v];
		if ( (valtmp< mapa[u][v]) && (valtmp < minimo) ) {
		minimo = valtmp;	
		ans = 3;
		}
	}
	return ans;
}

int main () {
	cin >> t;
	forn (rep,t) {
		int label[128][128];
		cin >> h >> w;
		int tmp1, tmp2;
		forn(i,h) forn (j,w) {
			cin >> tmp1;		
			mapa[i][j] = tmp1; 
			label[i][j] = -1;
		}
		
		vector<int> x,y;
		int ind = 0,lab = 0;
		forn(i,h) forn(j,w) if (label[i][j] == -1){
			int u = i, v = j;
			int mov = mover(u,v);
			while (mov>=0) {
				x.pb(u); y.pb(v);	
				if (mov == 0) u--;
				else if (mov == 1) v--;
				else if (mov == 2) v++;
				else if (mov == 3) u++;
				if (label[u][v] >=0) break;
				mov = mover(u,v);
			}
			int labtmp;
			if (label[u][v]>=0) labtmp = label[u][v];
			else labtmp = lab++;
			label[u][v] = labtmp;
			forn(k,x.size()) {	label[x[k]][y[k]] = labtmp;}
			x.clear(); y.clear();			
		}
	
		cout << "Case #" << rep+1 << ": " << endl;
		forn(i,h) { forn(j,w) cout <<(char)('a' + label[i][j]) << " "; cout << endl; }
	//	forn(i,h) { forn(j,w) cout << label[i][j] << " "; cout << endl; }
		
	}
	return 0;
}
