#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define bublic public
#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define pf push_front
#define mp make_pair
#define popf pop_front
#define popb pop_back
#define sz size()
#define fst first
#define snd second
#define It(x) x::iterator
#define CIt(x) x::const_iterator
#define For(i, st, en) for(int i=(st); i<=(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)

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

char ch[128][128];
int n;

bool can(int fr, int to)
{
	for (int i=to+1;i<n;i++)
	{
		if (ch[fr][i] == '1')
		{
			return false;
		}
	}

	return true;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("a.in", "rt", stdin);
    freopen("a.out", "wt", stdout);
#endif 

	cout << setiosflags(ios::fixed) << setprecision(10);

	int t;

	scanf("%d", &t);

	for (int o=0;o<t;o++)
	{
		scanf("%d", &n);
		int ans=0;

		for (int i=0;i<n;i++)
		{
			for (int j=0;j<n;j++)
			{
				cin >> ch[i][j];

			}
		}

		for (int i=0;i<n-1;i++)
		{
			if (!can(i,i))
			{
				int ind=0;

				for (int j=i+1;j<n;j++)
				{
					if (can(j,i))
					{
						ind=j;
						break;
					}
				}

				char back[128];

				for (int l=0;l<n;l++)
				{
					back[l]=ch[ind][l];
				}

				for (int j=ind;j>i;j--)
				{
					for (int l=0;l<n;l++)
					{
						ch[j][l]=ch[j-1][l];
					}
					ans++;
				}

				for (int l=0;l<n;l++)
				{
					ch[i][l]=ch[ind][l];
				}
			}
		}

		printf("Case #%d: %d\n", o+1, ans);

	}



	return 0;
}
