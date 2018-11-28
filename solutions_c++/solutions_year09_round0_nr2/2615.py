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


int n, h, w;
int a[128][128], used[128][128], ans[128][128], otv[1000];
int nextchar;
int nnn;

int rec(int x, int y, int c)
{
	used[x][y]=1;

	ans[x][y]=nextchar;
	
	int ddx=99, dx=0, ddy=-99, dy=-1, minf=99999999;
	
	dx=0; dy=1;
	if (x+dx>=0 && x+dx<w && y+dy>=0 && y+dy<h && a[x+dx][y+dy]<=minf && a[x][y]>a[x+dx][y+dy])
	{
		minf=a[x+dx][y+dy];
		ddx=dx; ddy=dy;
	}	

	dx=1; dy=0;
	if (x+dx>=0 && x+dx<w && y+dy>=0 && y+dy<h && a[x+dx][y+dy]<=minf && a[x][y]>a[x+dx][y+dy])
	{
		minf=a[x+dx][y+dy];
		ddx=dx; ddy=dy;
	}	

	dx=-1; dy=0;
	if (x+dx>=0 && x+dx<w && y+dy>=0 && y+dy<h && a[x+dx][y+dy]<=minf && a[x][y]>a[x+dx][y+dy])
	{
		minf=a[x+dx][y+dy];
		ddx=dx; ddy=dy;
	}

	dx=0; dy=-1;
	if (x+dx>=0 && x+dx<w && y+dy>=0 && y+dy<h && a[x+dx][y+dy]<=minf && a[x][y]>a[x+dx][y+dy])
	{
		minf=a[x+dx][y+dy];
		ddx=dx; ddy=dy;
	}

//	if (x==0 && y==0) cerr << ddx << ddy << endl;


	if (ddx!=99)
	{
//		cout << x << y << x+ddx << y+ddy << used[x+ddx][y+ddy]<<"!"<<endl;
		
		if (used[x+ddx][y+ddy])
		{
			otv[nextchar]=otv[ans[x+ddx][y+ddy]];
			return 1;
		}
		rec(x+ddx,y+ddy,nextchar);
	}

	if (ddx==99)
	{
	   otv[nextchar]=nnn;
	   nnn++;
//	   cerr << "%"<<x<<y<<"%";
	}

	return 0;
	
}


int main()
{
	freopen("q.in", "rt", stdin);
	freopen("q.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d\n",&n);

	for (int q=0; q<n; q++)
	{
		scanf("%d %d\n",&h,&w);
			for (int i=0; i<h; i++)
			for (int j=0; j<w; j++)
				scanf("%d",&a[j][i]);
		
		clr(used);
		clr(ans);
		clr(otv);
		nextchar=0;
		nnn='a';

		for (int j=0; j<h; j++)
		for (int i=0; i<w; i++)
		if (!used[i][j])	
		{
			rec(i,j,nextchar);
			nextchar++;
		}

		printf("Case #%d:\n",q+1);
		for (int j=0; j<h; j++)
		{
			for (int i=0; i<w; i++) printf("%c ",otv[ans[i][j]]);
			printf("\n");
		}
        

/*        for (int j=0; j<h; j++)
        {
        	for (int i=0; i<w; i++)	cout << ans[i][j] << " "; cout << endl;
        }

        cout << endl;

        for (int i=0; i<nextchar; i++) cout << otv[i] <<" ";
        
        cout << endl;
*/	}

	
	return 0;
}
