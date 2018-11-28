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
char st[30];
int a[30];

int main()
{
#ifdef HOME
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d",&t);
	gets(st);
	forn(tt,t)
	{
		printf("Case #%d: ",tt+1);
		gets(st);
		int n=strlen(st);
		clr(a);
		forn(i,n)
		{
			a[i]=int(st[i]-'0');
		}
		if (next_permutation(a,a+n))
		{
			forn(i,n)
			{
				cout << a[i];
			}
			cout << endl;
		} else
		{
/*
			cerr << tt << " ";
			cout << "!";
			while (next_permutation(a,a+n))
			{
				cerr << tt <<" ";
			}
			cerr << endl;
			ford(i,n)
			{
				a[i+1]=a[i];
			}
			a[1]=0;
			n++;
*/
			n++;
			a[n-1]=0;
			sort(a,a+n);
//			cout << "!";
			forn(i,n)
			{
				if (a[i]!=0) 
				{
					swap(a[i],a[0]);
					break;
				}
			}
			forn(i,n)
			{
				cout << a[i];
			}
/*			next_permutation(a,a+n);
			forn(i,n)
			{
				cout << a[i];
			}
*/			cout << endl;
		}
	}

	return 0;
}
