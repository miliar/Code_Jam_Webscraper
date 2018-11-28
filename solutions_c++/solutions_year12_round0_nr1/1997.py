#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
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

FILE *g_f_;
char *g_str_;
int g_s_;
#define freopen(a, b, c) (g_f_ = freopen(a, b, c))
#define scanf(...) (g_s_ = scanf(__VA_ARGS__))
#define sscanf(...) (g_s_ = sscanf(__VA_ARGS__))
#define gets(x) (g_str_ = fgets(x, sizeof(x), stdin))

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
typedef vector < int > VI;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

int n;
char s[102400];
char f[256];
char a[40][102400];

int main()
{
#ifdef ROOM_311
	time_t et_0 = clock();
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	cout << setiosflags(ios::fixed) << setprecision(10);
	
f[97]='y';
f[98]='h';
f[99]='e';
f[100]='s';
f[101]='o';
f[102]='c';
f[103]='v';
f[104]='x';
f[105]='d';
f[106]='u';
f[107]='i';
f[108]='g';
f[109]='l';
f[110]='b';
f[111]='k';
f[112]='r';
f[113]='z';
f[114]='t';
f[115]='n';
f[116]='w';
f[117]='j';
f[118]='p';
f[119]='f';
f[120]='m';
f[121]='a';
f[122]='q';

	gets(s);
	sscanf(s, "%d", &n);
	forn(i, n)
	{
		gets(a[i]);
		printf("Case #%d: ", i + 1);
		int l = strlen(a[i]);
		forn(j, l)
		{
			if (isalpha(a[i][j])) putchar(f[(int)a[i][j]]);
			else putchar(a[i][j]);
		}
	}
	
#ifdef ROOM_311
	time_t et_1 = clock();
	fprintf(stderr, "Execution time = %0.0lf ms\n", (et_1 - et_0) * 1000.0 / CLOCKS_PER_SEC);
#endif
	return 0;
}
