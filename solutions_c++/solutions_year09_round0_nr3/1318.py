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

const char* PATTERN = "welcome to code jam";
const int MODULO = 10000;

const int MAX_LEN = 512;

int d[MAX_LEN][50];
char s[MAX_LEN];

int main()
{
	freopen("c-large.in", "rt", stdin);
	freopen("c.out", "wt", stdout);
	cout << fixed << setprecision(12);

	int tc;
	scanf("%d\n", &tc);
	forn(tn, tc)
	{
		gets(s);

		for (int i = 0; s[i]; ++i)
		{
			d[i][0] = 1;
		}
		for (int i = 0; s[i]; ++i)
		{
			for (int j = 0; PATTERN[j]; ++j)
			{
				d[i + 1][j + 1] = d[i][j + 1];

				if (s[i] == PATTERN[j])
				{
//					cout << i << " " << j << endl;
					d[i + 1][j + 1] = (d[i + 1][j + 1] + d[i][j]) % MODULO;
				}
			}
		}
/*		cout << s << endl;
		for (int i = 0; s[i]; ++i)
		{
			for (int j = 0; PATTERN[j]; ++j)
			{
				cout << setw(4) << d[i + 1][j + 1];
			}
			cout << endl;
		}*/

		printf("Case #%d: %04d\n", tn + 1, d[strlen(s)][strlen(PATTERN)]);
	}

	return 0;
}
