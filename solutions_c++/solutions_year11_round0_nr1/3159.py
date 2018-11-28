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

#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define fst first
#define snd second
#define It(x) __typeof((x).begin())
#define For(i, st, en) for(__typeof(en) i=(st); i<=(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(__typeof(n) i=0; i<(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)

template <class _T> inline _T sqr(const _T& x) { return x * x; }
template <class _T> inline _T sgn(const _T& x) { return x > 0 ? 1 : (x < 0 ? -1 : 0); }
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

const int MAX_COMMANDS = 128;
const int INF = 0x7F7F7F7F;

int n;
PII commands[MAX_COMMANDS];

int findNext(int j, int prev)
{
	For(i, prev + 1, n - 1)
	{
		if (commands[i].fst == j)
		{
			return i;
		}
	}
	return -1;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	int testsCount;
	scanf("%d", &testsCount);
	forn(testNumber, testsCount)
	{
		scanf("%d", &n);
		forn(i, n)
		{
			char c[2];
			int p;
			scanf("%s %d", c, &p);
			commands[i] = mp(c[0] == 'O' ? 0 : 1, p);
		}
		
		int timeLeft[2] = {INF, INF};
		forn(i, 2)
		{
			int nx = findNext(i, -1);
			if (nx != -1)
			{
				timeLeft[i] = abs(1 - commands[nx].second) + 1;
			}
		}
		
		int ans = 0;
		forn(i, n)
		{
			int j = commands[i].first;
			int time = timeLeft[j];
			ans += time;

			timeLeft[1 - j] = max(timeLeft[1 - j] - time, 1);
			
			int nx = findNext(j, i);
			if (nx != -1)
			{
				timeLeft[j] = abs(commands[i].second - commands[nx].second) + 1;
			}
		}
		
		printf("Case #%d: ", testNumber + 1);
		printf("%d\n", ans);
	}

	return 0;
}
