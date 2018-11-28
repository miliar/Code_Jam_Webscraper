#include <ctime>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include <map>
#include <set>
#include <fstream>
#include <queue>
#include <bitset>
#include <numeric>
#include <iterator>
#include <complex>


using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); ++i)
#define repd(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define forn(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)
#define fornd(i, a, b) for (int i = (int)(b); i >= (int)(a); --i)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define fill(a, x) memset(a, x, sizeof(a))
#define pb push_back
#define mp make_pair
#define log(a, x) cout << a << " : " << x << endl;

typedef unsigned int uint;
typedef double dbl;
typedef long long ll;
typedef unsigned long long ull;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <string> vs;
typedef pair <int, int> pii;
typedef pair <dbl, dbl> pdd;
typedef unsigned char byte;
typedef complex<double> base;

template <class T> T inline sqr(T x) { return x * x; }
template <class T> inline T myAbs( T a ) { return a > 0 ? a : -a; }

#ifndef ONLINE_JUDGE
#include "prettyprint.cpp"
#endif

int f[110][40];
vi v;
int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int n,s,p;
	int T = 0;
	cin >> T;
	int k;
	rep(test, T) {
		zero(f);
		cin >> n >> s >> p;
		v.clear();
		v.resize(n);
		rep(i,n) {
			scanf("%d",&v[i]);
		}
		for(int i=1;i<=n;++i) {
			f[i][0] = f[i-1][0];
			if (v[i-1] % 3 == 0 && v[i-1] / 3 >= p)
				++f[i][0];
			if (v[i-1] % 3 != 0 && v[i-1] / 3 + 1 >= p)
				++f[i][0];
		}
		for(int j=1;j<=s;++j) {
			for(int i=1;i<=n;++i) {
				if (v[i-1] < 3 || v[i-1] > 28) {
					f[i][j] = f[i-1][j];
					if (v[i-1] % 3 == 0 && v[i-1] / 3 >= p)
						++f[i][j];
					if (v[i-1] % 3 != 0 && v[i-1] / 3 + 1 >= p)
						++f[i][j];
					continue;
				}
				f[i][j] = f[i-1][j];
				if (v[i-1] % 3 == 0 && v[i-1] / 3 >= p)
					++f[i][j];
				if (v[i-1] % 3 != 0 && v[i-1] / 3 + 1 >= p)
					++f[i][j];
				if (v[i-1] % 3 != 2) {
					k = f[i-1][j-1];
					if (v[i-1] / 3 + 1 >= p)
						++k;
					f[i][j] = max(f[i][j], k);
				}
				if (v[i-1] % 3 == 2) {
					k = f[i-1][j-1];
					if (v[i-1] / 3 + 2 >= p)
						++k;
					f[i][j] = max(f[i][j], k);
				}
			}
		}
		
		cout << "Case #" << test + 1 << ": " << f[n][s] << endl;
	}
	
    return 0;
}
