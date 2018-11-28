#pragma comment(linker, "/STACK:10000000")
#define _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_DEPRECATE

#include <cassert>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <numeric>
#include <bitset>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstdlib>
#include <functional>
#include <cstring>
#include <ctime>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
template <class T> T inline sqr(T x) { return x * x; }
template <class T> string str( T i ) { stringstream ss; ss << i; return ss.str(); }
int toint(string a) {istringstream is(a); int p; is>>p; return p;}
long long toll(string a){istringstream is(a);long long p;is>>p;return p;}

#define pb push_back
#define mp make_pair
#define e1 first
#define e2 second
#define sz size

#if ( _WIN32 || __WIN32__ )
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif
#define forn(i, n) for (i = 0; i < int(n); i++)
#define setval(a,v) memset(a, v, sizeof(a))
const ld pi = 3.1415926535897932384626433832795, eps = 1e-8;

const int maxn = 110;
int a[maxn], b[maxn], c[maxn];


inline int norm(int x)
{
	int res;
	res = ((x + 2) / 3);
	return res;
}

inline int surp(int x)
{
	if (x == 0)
		return 0;
	if (x >= 29)
		return 10;

	int res;
	res = ((x + 4)/ 3) ;
	return res;
}

int main()
{
   freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
   int t, it, i;
	int n, s, p, ans, u;
	cin >> t;
	for (it = 1; it <= t; it++)
	{
		if (it == 28)
			it = it;
		ans = 0;
		cin >> n >> s >> p;
		forn (i, n)
			cin >> a[i];
		sort(a, a + n, greater<int> ());
		forn (i, n)
			b[i] = norm(a[i]);
		b[n] = -1;
		forn (i, n)
			c[i] = surp(a[i]);
		forn (i, n + 1)
			if (b[i] < p)
			{
				u = i;
				break;
			}
		ans = u;
		c[u + s] = c[n] = -1;
		for (i = u; i <= u + s && i <= n; i++)
			if (c[i] < p)
			{
				ans += i - u;
				break;
			}
		cout << "Case #" << it << ": " << ans << endl;
	}
	return 0;
}
