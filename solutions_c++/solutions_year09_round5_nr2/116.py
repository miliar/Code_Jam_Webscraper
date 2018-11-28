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

int tcn, n, k;
int a[26];
int sum[16];
string s[64];
string ss;

void rec(int x)
{
	int z = 1;
	for (int i = 0; i < (int)ss.sz; ++i)
	{
		if (ss[i] == '+')
		{
			sum[x] += z;
			z = 1;
		}
		else
			z *= a[ss[i] - 'a'];
	}
	sum[x] = (sum[x] + z) % 10009;

	if (x == k) return;

	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < (int)s[i].sz; ++j)
		{
			a[s[i][j] - 'a']++;
		}
		rec(x + 1);
		for (int j = 0; j < (int)s[i].sz; ++j)
		{
			a[s[i][j] - 'a']--;
		}
	}
	
}

int main()
{
	freopen("small.in", "rt", stdin);
	freopen("small.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	cin >> tcn;
	for (int tc = 0; tc < tcn; ++tc)
	{
		cin >> ss >> k >> n;
		for (int i = 0; i < n; ++i)
		{
			cin >> s[i];
		}

		clr(a);
		clr(sum);
		rec(0);

		cout << "Case #" << tc + 1 << ":";
		for (int i = 0; i < k; ++i)
		{
			cout << " " << sum[i + 1];
		}
		cout << endl;
		cerr << tc << endl;
	}

	return 0;
}
