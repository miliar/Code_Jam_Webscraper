#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>
#include <bitset>
#include <queue>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

template <class T> T sqr (T x) {return x * x;}

const int nmax = 210;

long long f, m;
int n;
pair<long long, long long> a[nmax];

long long sol(long long c){
	long long now = m - c * f;
	long long res = 0;
	forn(i, n){
		long long dd = now / a[i].sc;
		dd = min(dd, min(dd / c + 2, (a[i].fs - (i == 0 ? 0 : a[i-1].fs))) * c);
		res += dd;
		now -= dd * a[i].sc;
	}
	return res;
}

void solve(){
	cin >> m >> f >> n;
	forn(i, n){
		cin >> a[i].sc >> a[i].fs;
		a[i].fs ++;
	}
	sort(a, a + n);
	{
		int nn = 1;
		for (int i = 1; i < n; i ++){
			while (nn > 0 && a[i].sc < a[nn - 1].sc)
				nn --;
			a[nn ++] = a[i];
		}
		n = nn;
	}
	long long res = 0;
//	long long Q = 1000;
//	long long step = max(1, (m / f) / Q);
//	forn(qwe, Q){
		long long l = 1, r = m / f;
		while (r - l > 100){
			long long m1 = l + (r - l) / 3;
			long long m2 = l + (r - l) * 2 / 3;
			long long r1 = sol(m1);
			long long r2 = sol(m2);
				res = max(res, max(r1, r2));
			if (r1 > r2)
				r = m2;
			else
				l = m1;
		}
//	}
//	cerr << l << " " << r << endl;
	for (long long i = l; i <= r; i ++)
		res = max(res, sol(i));
	cout << res << endl;
}

int main ()
{
//	freopen("input.txt", "rt", stdin);

	int n;
	cin >> n;
	forn(i, n){
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
