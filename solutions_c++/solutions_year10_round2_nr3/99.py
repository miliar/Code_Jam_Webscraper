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

#define MAXN 512
#define mod 100003

tint comb[MAXN][MAXN],t,n, f[MAXN][MAXN];

tint _comb(int n, int k) {
	if (comb[n][k]!=-1) return comb[n][k];
	if (n==k || k==0) return comb[n][k] = 1;
	return comb[n][k] = ( _comb(n-1,k) + _comb(n-1,k-1) )%mod;
}

tint _f(int n, int k) {
	if (f[n][k]!=-1) return f[n][k];
	if (k == n-1 || k == 1) return f[n][k] = 1;
	tint ans = 0;
	forsn(j,max(1,2*k-n),k) {
		ans+= (_f(k,j)*_comb(n-k-1,k-j-1))%mod;
		ans%= mod;
	}
	return f[n][k] = ans%mod;
}

int main () {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);

	memset(comb,-1,sizeof(comb));
//	cout << _comb(4,2) << " " << _comb(8,4) << " "<< _comb(3,2) << " " << _comb(50,2) << endl;
	cin >> t;
	forn(rep,t) {
		cin >> n;
		memset(f,-1,sizeof(f));
		tint ans = 0;
		forsn(k,1,n) {
			ans+= _f(n,k);
			ans%= mod;
		}
		cout << "Case #" << rep+1  << ": " << ans%mod << endl;
	}
	return 0;
}
