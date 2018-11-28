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
#include <cstring>
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


#define MAXN 128

tint c,n,b,t,x[MAXN], v[MAXN],k;
bool is[MAXN];


int main () {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	cin >> c;
	forn(rep,c) {
		cin >> n >> k >> b >> t;
		forn(i,n) cin >> x[i];
		forn(i,n) cin >> v[i];

		int cant = 0;
		forn(i,n) if (x[i]+t*v[i] >= b) {
			is[i] = true;
			cant++;
		} else is[i] = false;

		cout << "Case #" << rep+1 << ": ";
		if (cant<k) cout << "IMPOSSIBLE" << endl;
		else {
			tint ans = 0, go = 0, malos = 0;
			for(int i = n-1; i>=0 && go<k; i--) {
				if (!is[i]) malos++;
				else {
					ans += malos;
					go++;
				}
			}
			cout << ans << endl;
		}
	}

	return 0;
}
