#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <vector>

using namespace std;

#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define sz size()
#define It(x) x::iterator
#define clr(x) memset((x), 0, sizeof(x))
#define For(i, l, r) for (int i = int(l); i <= int(r); i++)
#define Ford(i, l, r) for (int i = int(l); i >= int(r); i--)
#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = (int(n) - 1); i >= 0; i--)
#define fori(t, i, x) for (t i = x.begin(); i != x.end(); i++)

typedef long double ld;
typedef signed   long long i64;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < ld > VD;
typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < string > VS;
typedef pair < int, int > PII;
typedef map < string, int > MSI;

const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

template <class T> inline T sqr(const T& x) { return x * x; }
template <class T> string toStr(T x) { ostringstream os(""); os << x; return os.str(); }

#define MAX_WORDS 5096

int l, n, m;
char buf[128000];
string a[MAX_WORDS];

int main()
{
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	cout << fixed << setprecision(12);

	scanf("%d %d %d", &l, &n, &m);
	assert(l <= 15);
	assert(n <= MAX_WORDS);
	assert(m <= 500);
	forn(i, n)
	{
		scanf("%s", buf);
		a[i] = buf;
		assert((int)a[i].sz == l);
	}
	forn(i, m)
	{
		scanf("%s", buf);

		VS v;
		for (char* p = buf; *p; ++p)
		{
			string s;
			if (*p != '(')
			{
				s += *p;
			}
			else
			{
				++p;
				while (*p != ')')
				{
					s += *p;
					++p;
				}
			}
			v.pb(s);
		}
//		cerr << buf << endl;
		assert((int)v.sz == l);

		int ans = 0;
		forn(j, n)
		{
			const string& s = a[j];
			bool ok = true;
			forn(k, s.sz)
			{
				if (v[k].find(s[k]) == string::npos)
				{
					ok = false;
					break;
				}
			}
			ans += ok;
		}

		printf("Case #%d: %d", i + 1, ans);
		if (i < m - 1) puts("");
	}

	return 0;
}
