#include <algorithm>
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
#include <string>
#include <vector>

using namespace std;

#define bublic public
#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define For(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)

template <class _T> inline _T sqr(const _T& x) { return x * x; }
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

typedef long double ld;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;

// Types
typedef signed   long long i64;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < ld > VD;
typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < string > VS;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

int qq;
int n, k;
char s[1024000];
char pa[256];
bool e[256];
bool g[256][256];
bool a[3256][3256];
bool u[3256];
int c[256][256];
int p[3256];
int kk;

bool find(int k)
{
	u[k] = true;
	forn(i, kk)
	{
		if (a[k][i] && (p[i] == -1 || (!u[p[i]] && find(p[i]))))
		{
			p[i] = k;
			return true;
		}
	}
	return false;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	For(i, 'a', 'z')
	{
		pa[i] = i;
	}
	pa['o'] = '0';
	pa['i'] = '1';
	pa['e'] = '3';
	pa['a'] = '4';
	pa['s'] = '5';
	pa['t'] = '7';
	pa['b'] = '8';
	pa['g'] = '9';

	scanf("%d", &qq);
	forn(ii, qq)
	{
		printf("Case #%d: ", ii+1);
		fprintf(stderr, "Case #%d:\n", ii+1);
		
		scanf("%d", &k);
		scanf("%s", s);
		n = strlen(s);
		clr(g);
		clr(e);
		forn(i, n - 1)
		{
			char c1 = s[i];
			char c2 = s[i + 1];
			e[c1] = true;
			e[c2] = true;
			e[pa[c1]] = true;
			e[pa[c2]] = true;
			g[c1][c2] = true;
			g[c1][pa[c2]] = true;
			g[pa[c1]][c2] = true;
			g[pa[c1]][pa[c2]] = true;
		}
		int ans = 0;
		kk = 0;
		forn(i, 256)
		{
			forn(j, 256)
			{
				if (g[i][j])
				{
					ans += 2;
					c[i][j] = kk++;
				}
//				ans += g[i][j];
			}
		}
		clr(a);
		forn(i, 256)
		{
			forn(j, 256)
			{
				if (!g[i][j]) continue;
				forn(k, 256)
				{
					if (!g[j][k]) continue;
					a[c[i][j]][c[j][k]] = true;
				}
			}
		}
		forn(i, kk)
		{
			a[kk][i] = true;
		}
		kk++;
		ans++;
/*		forn(i, kk)
		{
			forn(j, kk)
			{
				cerr << a[i][j] << " ";
			}
			cerr << endl;
		}*/
		memset(p, 0xff, sizeof(p));
		forn(i, kk)
		{
//			if (!e[i]) continue;
			clr(u);
			ans -= find(i);
		}
		forn(i, kk)
		{
//			cerr << p[i] << " " << endl;
		}

		printf("%d\n", ans);
		
		fflush(stdout);
	}

	return 0;
}
