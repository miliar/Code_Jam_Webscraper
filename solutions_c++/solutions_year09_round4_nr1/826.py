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

int n,t;
bool a[64][64];
char ss[64];
int p[64];
int g[64];
bool u[64];


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
		scanf("%d",&n);
		clr(a);
		clr(p);
		clr(g);
		gets(ss);
		forn(i,n)
		{
			gets(ss);
			forn(j,n)
			{
				if (ss[j]=='1') a[i][j]=true;
			}
		}
		
		forn(i,n)
		{
			int k=-1;
			forn(j,n)
			{
				if (a[i][j]) k=j;
			}
			p[i]=k;
		}

		int ans=0;
		forn(i,n)
		{
			int k=0;
			for(int j=i;j<n;j++)
			{
				if (p[j]<=i)
				{
					k=j;
					break;
				}
			}
/*
			forn(j,n)
			{
				cout << p[j] << " ";
			}
			cout << endl;
			cout << i << " " << k << endl;
*/
			while (k!=i)
			{
//				cout << "!";
				swap(p[k],p[k-1]);
				k--;
				ans++;
			}
/*
			forn(j,n)
			{
				cout << p[j] << " ";
			}
			cout << endl;
*/		}
		

		printf("%d\n",ans);
	}	

	return 0;
}
