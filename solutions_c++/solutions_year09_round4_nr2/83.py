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

int tcn, n, m, f, res;
string a[64];

vector<VI> w[64][64];

bool operator ==(VI &a, VI &b)
{
	if (a.sz != b.sz) return false;
	for (int i = 0; i < (int)a.sz; ++i)
	{
		if (a[i] != b[i]) return false;
	}
	return true;
}

void rec(int ii, int jj, VI vi)
{
	if (res <= (int)vi.sz) return;
	if (ii == n - 1)
	{
		if (res > (int)vi.sz)
			res = (int)vi.sz;

/*		for (int i = 0; i < (int)vi.sz; ++i)
		{
			cout << vi[i] << " ";
		}
		cout << endl;*/
		return;
	}

	for (int i = 0; i < (int)w[ii][jj].sz; ++i)
	{
		if (vi == w[ii][jj][i]) return;
	}
	w[ii][jj].pb(vi);


	if (jj && a[ii][jj - 1] == '.')
	{
		int i = ii;
		while (i + 1 != n && a[i + 1][jj - 1] == '.') i++;
		if (i - ii <= f)
			rec(i, jj - 1, vi);
	}
	if (jj + 1 < m && a[ii][jj + 1] == '.')
	{
		int i = ii;
		while (i + 1 != n && a[i + 1][jj + 1] == '.') i++;
		if (i - ii <= f)
			rec(i, jj + 1, vi);
	}

	if (jj && a[ii][jj - 1] == '.' && a[ii + 1][jj - 1] != '.')
	{
		a[ii + 1][jj - 1] = '.';
		vi.pb((ii + 1) * m + jj - 1);
		rec(ii, jj, vi);
		vi.erase(vi.end() - 1);
		a[ii + 1][jj - 1] = '#';
	}

	if (jj + 1 < m && a[ii][jj + 1] == '.' && a[ii + 1][jj + 1] != '.')
	{
		a[ii + 1][jj + 1] = '.';
		vi.pb((ii + 1) * m + jj + 1);
		rec(ii, jj, vi);
		vi.erase(vi.end() - 1);
		a[ii + 1][jj + 1] = '#';
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
		cerr << tc << endl;
		cin >> n >> m >> f;
		for (int i = 0; i < n; ++i)
		{
			cin >> a[i];
			for (int j = 0; j < m; ++j)
			{
				w[i][j].clear();
			}
		}
	    res = n * m;
	    VI vi;
	    rec(0, 0, vi);
	
		cout << "Case #" << tc + 1 << ": ";
		if (res == n * m)
			cout << "No" << endl;
		else
			cout << "Yes " << res << endl;
	}

	return 0;
}
