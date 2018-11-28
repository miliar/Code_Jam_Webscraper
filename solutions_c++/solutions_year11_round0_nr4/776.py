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

typedef double tipo;

#define MAXN 1024

tipo f[MAXN][MAXN], e[MAXN];

int n, t;

tipo _e(int m) {
	if (m == 0) return 0.0;
	if (e[m]>-0.5) return e[m];
	tipo res = 1.0;
	forsn(k,1,m) res+= f[m][k]*_e(m-k);
	res/= (1.0-f[m][0]);
	return e[m] = res;
}

void calcular() {
	forn(i,MAXN) forn(j,MAXN) f[i][j] = 0.0;
	
	f[0][0] = 1.0;
	f[1][0] = 0.0;
	f[1][1] = 1.0;
	
	forsn(m,2,MAXN) forn(k,m+1) {
		if (k>0) f[m][k]+= f[m-1][k-1];
		forsn(j,2,m-k+1) f[m][k] += f[m-j][k];
		f[m][k]*=(1.0/(tipo)m);
	}	
}

int main () {
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	
	forn(i,MAXN) e[i] = -1;
	e[1] = e[0] = 0.0;
	calcular();
//	forn(i,10) {forn(j,10) cout << f[i][j] << " "; cout << endl;} cout << endl;

//	cout << _e(1) << " " << _e(2) << " " << _e(3) << endl;
	
	
	cin >> t;
	forn(caso,t) {
		cin >> n;	
		int pfijos = 0;
		forn(i,n) {
			int tmp; cin >> tmp;
			if (tmp-1 == i) pfijos++;
		}
		n-=pfijos;
	//	cout << n << endl;
		tipo ans = _e(n);
		cout << "Case #" << caso+1 << ": ";
		printf("%.6f\n", ans);
	}
	
	return 0;
}
