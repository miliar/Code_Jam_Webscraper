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



int main()
{
	freopen("small.in", "rt", stdin);
	freopen("small.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	int tcn, n;
	string a[64];
	int z[64];
	cin >> tcn;
	for (int tc = 0; tc < tcn; ++tc)
	{
		clr(z);
		cin >> n;
		for (int i = 0; i < n; ++i)
		{
			cin >> a[i];
		}

		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				if (a[i][j] == '1') z[i] = j;
			}
		}

		int k = 0;
		for (int i = 0; i < n; ++i)
		{
			if (z[i] <= i) continue;
			int t = i;
			for (int j = i + 1; j < n; ++j)
			{
				if (z[j] <= i)
				{
					t = j;
					break;
				}
			}
			while (t > i)
			{
				swap(z[t], z[t - 1]);
				k++;
				t--;
			}
		}

		cout << "Case #" << tc + 1 << ": " << k << endl;
	}


	return 0;
}
