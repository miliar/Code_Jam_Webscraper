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

int s[20], p[20];
vi w;

int main()
{
   freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
   int it, pref, t, q, ans, i, a, b, z, j, k, c;
	cin >> t;
	w.reserve(20);
	forn (it, t)
	{
		cin >> a >> b;
		ans = 0;
		for (i = a; i <= b; i++)
		{
			c = i;
			q = 0;
			w.clear();
			while (c > 0)
			{
				p[q] = c % 10;
				q++;
				c /= 10;
			}
			forn(j, q >> 1)
				swap(p[j], p[q - j - 1]);
			z = 1;
			s[q + 1] = 0;
			for (j = q; j >= 1; j--)
			{
				s[j] = s[j + 1] + z * p[j - 1];
				z *= 10;
			}

			pref = 0;
			z = 1;
			for (j = 1; j < q; j++)
			{
				z *= 10;
				pref = pref * 10 + p[j - 1];
				w.pb(s[j + 1] * z + pref);
			}
			sort(w.begin(), w.end());
			w.resize(unique(w.begin(), w.end()) - w.begin());
			ans += upper_bound(w.begin(), w.end(), b) - lower_bound(w.begin(), w.end(), i + 1);
		}

		cout << "Case #" << it + 1 << ": " << ans << endl;
	}
	return 0;
}
