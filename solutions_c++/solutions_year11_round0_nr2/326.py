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
int n;
bool op[26][26];
int a[26][26];
char s[1024];
int t[1024];
int tt;

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d", &qq);
	forn(ii, qq)
	{
		printf("Case #%d: ", ii+1);
		fprintf(stderr, "Case #%d:\n", ii+1);

		memset(a, 0xff, sizeof(a));
		clr(op);
		int k;
		scanf("%d", &k);
		forn(i, k)
		{
			scanf("%s", s);
			a[s[0] - 'A'][s[1] - 'A'] = a[s[1] - 'A'][s[0] - 'A'] = s[2] - 'A';
		}
		scanf("%d", &k);
		forn(i, k)
		{
			scanf("%s", s);
			op[s[0] - 'A'][s[1] - 'A'] = op[s[1] - 'A'][s[0] - 'A'] = true;
		}
		scanf("%d", &n);
		scanf("%s", s);
		
	    tt = 0;
		forn(i, n)
		{
			t[tt++] = s[i] - 'A';
			while (tt >= 2 && a[t[tt-2]][t[tt-1]] != -1)
			{
				tt--;
				t[tt-1] = a[t[tt-1]][t[tt]];
			}
			forn(i, tt)
			{
				if (op[t[i]][t[tt-1]]) tt = 0;
			}
		}
		printf("[");
		forn(i, tt)
		{
			if (i) printf(", ");
			printf("%c", 'A' + t[i]);
		}
		printf("]\n");

		fflush(stdout);
	}

	return 0;
}
