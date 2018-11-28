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

ld x[64];
ld y[64];
ld r[64];
int n;

ld dist(int i, int j)
{
	return sqrt(sqr(x[i] - x[j]) + sqr(y[i] - y[j]));
}

int main()
{
	freopen("small.in", "rt", stdin);
	freopen("small.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(8);

	int tcn;
	cin >> tcn;
	for (int tc = 0; tc < tcn; ++tc)
	{
		cin >> n;
		for (int i = 0; i < n; ++i)
		{
			cin >> x[i] >> y[i] >> r[i];
		}

		ld res = 0.0;
		if (n == 1)
			res = r[0];
		else if (n == 2)
			res = max(r[0], r[1]);
		else if (n == 3)
		{
			res   = max((dist(0, 1) + r[0] + r[1]) / 2.0, r[2]);
			res <?= max((dist(0, 2) + r[0] + r[2]) / 2.0, r[1]);
			res <?= max((dist(1, 2) + r[1] + r[2]) / 2.0, r[0]);
		}

		cout << "Case #" << tc + 1 << ": " << res << endl;
	}


	return 0;
}
