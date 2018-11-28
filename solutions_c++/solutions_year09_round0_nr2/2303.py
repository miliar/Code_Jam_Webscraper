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

int n,m,t;
int a[128][128];
char b[128][128];
char cur='a';

char dfs(int x,int y)
{
//	cerr << x << " " << y<< endl;

	if (b[x][y]>='a' && b[x][y]<='z') return b[x][y];
	
	int mm=999999;
	if (x>0 && a[x-1][y]<a[x][y]) mm=min(mm,a[x-1][y]);
	if (x<n-1 && a[x+1][y]<a[x][y]) mm=min(mm,a[x+1][y]);
	if (y>0 && a[x][y-1]<a[x][y]) mm=min(mm,a[x][y-1]);
	if (y<m-1 && a[x][y+1]<a[x][y]) mm=min(mm,a[x][y+1]);

	if (mm==999999) 
	{
//		cerr << x << " " << y << endl;
		b[x][y]=cur;
		cur++;
	} else
	if (x>0 && mm==a[x-1][y])
	{
		b[x][y]=dfs(x-1,y);
	} else
	if (y>0 && mm==a[x][y-1])
	{
		b[x][y]=dfs(x,y-1);
	} else
	if (y<m-1 && mm==a[x][y+1])
	{
		b[x][y]=dfs(x,y+1);
	} else
	if (x<n-1 && mm==a[x+1][y])
	{
		b[x][y]=dfs(x+1,y);
	}
	return b[x][y];
}

int main()
{
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d",&t);
	forn(tt,t)
	{
		scanf("%d%d",&n,&m);
		clr(a);
		forn(i,n)
		{
			forn(j,m)
			{
				int x;
				scanf("%d",&x);
				a[i][j]=x;
			}
		}
/*
		forn(i,n)
		{
			forn(j,m)
			{
				cout << a[i][j] << " ";
			}
			cout << endl;
		}
*/		
		cur='a';
		clr(b);
		forn(i,n)
		forn(j,m)
		{
			if (b[i][j]<'a' || b[i][j]>'z') 
			{
				b[i][j]=dfs(i,j);
			}
		}
    
		printf("Case #%d:\n",tt+1);
		forn(i,n)
		{
			forn(j,m)
			{
				printf("%c ",b[i][j]);
			}
			printf("\n");
		}

	}


	return 0;
}
