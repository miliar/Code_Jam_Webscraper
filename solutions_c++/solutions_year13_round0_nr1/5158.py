#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define x first
#define y second
#define It(x) x::iterator
#define CIt(x) x::const_iterator
#define For(i, st, en) for(__typeof(en) i=(st); i<=(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(__typeof(n) i=0; i<(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)

template <class _T> inline _T sqr(const _T& x) { return x * x; }
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }
template <class _T> inline istream& operator << (istream& is, const _T& a) { is.putback(a); return is; }

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

int T;
int n = 4;
char a[5][5];

bool check(char c)
{
	for(int i=0;i<n;i++)
	{
		bool flag = true;
		for(int j=0;j<n;j++)
		{
			if (a[i][j] != c && a[i][j] != 'T')
			{
				flag = false;
				break;
			}	
		}
		if (flag) return true;
	}

	for(int j=0;j<n;j++)
	{
		bool flag = true;
		for(int i=0;i<n;i++)
		{
			if (a[i][j] != c && a[i][j] != 'T')
			{
				flag = false;
				break;
			}	
		}
		if (flag) return true;
	}

	if ((a[0][0] == c || a[0][0] == 'T') &&
		(a[1][1] == c || a[1][1] == 'T') &&
		(a[2][2] == c || a[2][2] == 'T') &&
		(a[3][3] == c || a[3][3] == 'T')) return true;

	if ((a[0][3] == c || a[0][3] == 'T') &&
		(a[1][2] == c || a[1][2] == 'T') &&
		(a[2][1] == c || a[2][1] == 'T') &&
		(a[3][0] == c || a[3][0] == 'T')) return true;

	return false;
}

bool full()
{
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if (a[i][j] == '.') return true;
		}
	}
	return false;
}


int main()
{
#ifdef HOME
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d\n", &T);
	forn(t, T)
	{
		printf("Case #%d: ", t+1);
		for(int i=0;i<5;i++)
		{
			gets(a[i]);
		}
		
		if (check('X'))
		{
			printf("X won\n");
			continue;
		}
		if (check('O'))
		{
			printf("O won\n");
			continue;
		}
		if (!full())
		{
			printf("Draw\n");
			continue;
		}
		printf("Game has not completed\n");
	}

	return 0;
}
