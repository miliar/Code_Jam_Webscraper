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

int t;
string st;
int a[100];
bool u[100];

int main()
{
#ifdef HOME
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d",&t);
	forn(tt,t)
	{
		printf("Case #%d: ",tt+1);
		cin >> st;
		int n=st.sz;
		clr(u);
		clr(a);
		forn(i,n)
		{
			if (st[i]==st[0])
			{
				a[i]=1;
				u[i]=true;
			}
		}
		int cur=0;
		for (int i=1;i<n;i++)
		{
			if (!u[i])
			{
				forn(j,n)
				{
					if (st[i]==st[j])
					{
						a[j]=cur;
						u[j]=true;
					}
				}
				if (cur==0)
				{
					cur=2;
				} else cur++;
			}
		}
		if (cur==0) cur=2;
/*		cerr << cur << endl;
		forn(i,n)
		{
			cout << a[i] << " ";
		}
		cout << endl;
*/
//		for(int j=cur;j<36;j++)
//		{
			u64 mm;
			i64 j=cur;
			u64 ans=0;
			i64 ss=1;
			ford(i,n)
			{
				ans+=ss*a[i];
				ss*=j;
			}
		    mm=ans;
//	    }
		cout << mm << endl;
	}

	return 0;
}
