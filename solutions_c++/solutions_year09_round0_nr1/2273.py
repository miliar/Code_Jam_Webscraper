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
#define mp make_pair
#define sz size()
#define fst first
#define snd second
#define It(x) x::iterator
#define CIt(x) x::const_iterator
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

int l,d,n;;
char s[10000];
string a,st;
int f[20];
int words[5100][20];

int main()
{
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	cin >> l >> d >> n;
	gets(s);
	clr(words);
	forn(i,d)
	{
		gets(s);
		a=s;
		forn(j,l)
		{
			words[i][j]= (1 << (int(a[j]-'a'))) ;
		}
	}

	for(int tt=1;tt<=n;tt++)
	{
		gets(s);
		string st=s;
		int m=st.sz;
		int i=0;
		int k=0;
		clr(f);
		while (i<m)
		{
			if (st[i]=='(')
			{
				i++;
				while (st[i]!=')')
				{
					f[k]|=(1 << (int(st[i]-'a')));
					i++;
				}
				k++;
			} else
			{
				f[k]|=(1 << (int(st[i]-'a')));
				k++;
			}
			i++;
		}

		int ans=0;
		forn(i,d)
		{
			bool flag=true;
			forn(j,l)
			{
				if (!(words[i][j] & f[j]))
				{
					flag=false;
					break;
				}
			}
			if (flag) ans++;
		}
		printf("Case #%d: %d\n",tt,ans);
	}


	return 0;
}
