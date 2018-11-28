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

int n,m,t;
int a[10];
bool u[128];

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

		scanf("%d%d",&n,&m);
		forn(i,m)
		{
			scanf("%d",&a[i]);
			a[i]--;
		}
		int mm=999999999;
		do
		{
			clr(u);
			int ans=0;
/*				cerr << tt << endl;
				forn(j,m)
				{
					cerr << a[j] << " ";
				}
				cerr << endl;
			forn(i,n)
			{
				cerr << u[i] << " ";
			}
			cerr << endl;
*/			forn(i,m)
			{
				u[a[i]]=true;
				int j=a[i]-1;

//if (tt==1)			cerr << ans<< endl;
				while (j>=0 && !u[j])
				{
//					cerr << j << endl;
					ans++;
					j--;
				}
				j=a[i]+1;
//if (tt==1)			cerr << ans<< endl;
				while (j<n && !u[j])
				{
//					cerr << j << endl;
					ans++;
					j++;
				}
//				return 0;
//if (tt==1)			cerr << ans<< endl<< endl;

			}
			mm=min(mm,ans);
//			cerr << ans<< endl;
//if (tt==1) return 0;
		} while (next_permutation(a,a+m));

		cout << mm << endl;
	}

	return 0;
}
