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

tint gcd(int a, int b){return (b==0)?a:gcd(b,a%b);}

tint c,n,t[1024];
const tint INF = 1000000000LL;

int main () {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	cin >> c;
	forn(rep,c) {
		cin >> n; forn(i,n) cin >> t[i];
		sort(t,t+n);
		tint res, mod;
		if (n==3) {
			if (t[1] == t[2]) n--;
			else if (t[0] == t[1]) {
				n--;
				t[1] = t[2];
			} else {
				mod = gcd(t[2]-t[1],t[1]-t[0]);
				res = (-t[0]+INF*mod)%mod;
			}
		}
		if (n==2) {
			if (t[1] == t[0]) res = 0;
			else {
				mod = t[1]-t[0];
				res = (-t[0]+INF*mod)%mod;
//				cout << mod << endl;
			}
		}


		cout << "Case #" << rep+1 << ": " << res << endl;

	}
	return 0;
}
