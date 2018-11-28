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


int p[128][32];
int a[128][128];
int n, k, tcn;

bool intersect(int i1, int i2)
{
	if (p[i1][0] > p[i2][0]) swap(i1, i2);
	for (int i = 0; i < k; ++i)
	{
		if (p[i1][i] >= p[i2][i])
			return true;
	}
	return false;
}

int res;
int num[128];
int v[128][128];

void rec(int cur, int r)
{
	if (cur == n || r >= res)
	{
		if (r < res) res = r;
		return;
	}

	for (int i = 0; i < r; ++i)
	{
	    int b = 1;
	    for (int j = 0; j < num[i]; ++j)
	    {
	    	if (!a[cur][v[i][j]]) b = 0;
	    }
	    if (b)
	    {
	    	v[i][num[i]++] = cur;
	    	rec(cur + 1, r);
	    	num[i]--;
	    }
	}

   	v[r][num[r]++] = cur;
   	rec(cur + 1, r + 1);
   	num[r]--;
}


int main()
{
	freopen("small.in", "rt", stdin);
	freopen("small.out", "wt", stdout);

	cin >> tcn;
	for (int tc = 0; tc < tcn; ++tc)
	{
		cin >> n >> k;
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < k; ++j)
			{
				cin >> p[i][j];
			}
		}

		clr(a);
	    for (int i = 0; i < n; ++i)
	    {
	    	for (int j = 0; j < n; ++j)
	    	{
	    		if (! intersect(i, j)) a[i][j] = 1;
	    	}
	    }

	    clr(num);
		res = n;
		rec(0, 0);
	
	
		cout << "Case #" << tc + 1 << ": " << res << endl;
	}


	return 0;
}
