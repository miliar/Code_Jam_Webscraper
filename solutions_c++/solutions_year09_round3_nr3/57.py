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

int b[1 << 7];
int d[1 << 7][1 << 7];

int main()
{
	freopen("small.in", "rt", stdin);
	freopen("small.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);


	int tcn, p , q;
	cin >> tcn;
	for (int tc = 0; tc < tcn; ++tc)
	{
		cin >> p >> q;
		for (int i = 0; i < q; ++i)
		{
			cin >> b[i + 1];
		}
		b[0] = 0;
		b[q + 1] = p + 1;
		q += 2;
		clr(d);
		for (int i = 0; i + 2 < q; ++i)
		{
			d[i][i + 2] = b[i + 2] - b[i] - 2;
		}

		for (int k = 3; k < q; ++k)
		{
			for (int i = 0; i + k < q; ++i)
			{
				d[i][i + k] = d[i][i + 1] + d[i + 1][i + k];
				for (int j = i + 2; j < i + k; ++j)
				{
					d[i][i + k] <?= d[i][j] + d[j][i + k];
				}
				d[i][i + k] += b[i + k] - b[i] - 2;
			}
		}

/*		for (int i = 0; i < q; ++i)
		{
			for (int j = 0; j < q; ++j)
			{
				cout << d[i][j] << " ";
			}
			cout << endl;
		}*/

		cout << "Case #" << tc + 1 << ": " << d[0][q - 1] << endl;
	}


	return 0;
}
