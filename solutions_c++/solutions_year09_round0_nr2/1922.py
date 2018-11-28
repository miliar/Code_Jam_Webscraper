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

int w,h;
int atl[102][102];
bool a[102*102][102*102];
int col[102*102];
bool use[102*102];

bool can(int x, int y)
{
	return (( x>=0 && x<h) && (y>=0 && y<w));
}

int nom(int h, int w, int x, int y)
{
	return ((x)*w + y);
}

int q[128*128];

void bfs(int x, int color)
{
	int qs=0;
	int qe=1;
	q[0]=x;
	use[x]=true;
	col[x]=color;

	while (qs<qe)
	{
		int cur=q[qs];

		for (int i=0;i<h*w;i++)
		{
			if (!use[i] && a[cur][i])
			{
				use[i]=true;
				col[i]=color;
				q[qe++]=i;
			}
		}
		qs++;
	}
	return;
}

int main()
{
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	int t;

	scanf("%d", &t);

	for (int o=0;o<t;o++)
	{
		
		scanf("%d%d",&h,&w);

		clr(atl);
		clr(a);

		for (int i=0;i<h;i++)
		{
			for (int j=0;j<w;j++)
			{
				scanf("%d", &atl[i][j]);
			}
		}

		for (int i=0;i<h;i++)
		{
			for (int j=0;j<w;j++)
			{
				int mn=atl[i][j];

				if (can(i-1,j))
				{
					mn=min(mn,atl[i-1][j]);
				}
				if (can(i,j-1))
				{
					mn=min(mn,atl[i][j-1]);
				}
				if (can(i,j+1))
				{
					mn=min(mn,atl[i][j+1]);
				}
				if (can(i+1,j))
				{
					mn=min(mn,atl[i+1][j]);
				}

				if (can(i-1,j) && atl[i-1][j]<atl[i][j] && mn==atl[i-1][j])
				{
					a[nom(h,w,i,j)][nom(h,w,i-1,j)]=a[nom(h,w,i-1,j)][nom(h,w,i,j)]=1;
					continue;
				}

				if (can(i,j-1) && atl[i][j-1]<atl[i][j] && mn==atl[i][j-1])
				{
					a[nom(h,w,i,j)][nom(h,w,i,j-1)]=a[nom(h,w,i,j-1)][nom(h,w,i,j)]=1;
					continue;
				}

				if (can(i,j+1) && atl[i][j+1]<atl[i][j] && mn==atl[i][j+1])
				{
					a[nom(h,w,i,j)][nom(h,w,i,j+1)]=a[nom(h,w,i,j+1)][nom(h,w,i,j)]=1;
					continue;
				}

				if (can(i+1,j) && atl[i+1][j]<atl[i][j] && mn==atl[i+1][j])
				{
					a[nom(h,w,i,j)][nom(h,w,i+1,j)]=a[nom(h,w,i+1,j)][nom(h,w,i,j)]=1;
					continue;
				}
			}
		}

		int kol=w*h;

		clr(use);
		clr(col);
		int color=0;
/*
		for (int i=0;i<kol;i++)
		{
			for (int j=0;j<kol;j++)
			{
				cout << a[i][j] << " ";
			}
			cout << endl;
		}
*/
		for (int i=0;i<kol;i++)
		{
			if (!use[i])
			{
				bfs(i,color);
				color++;
			}
		}

		printf("Case #%d:\n", o+1);
		for (int i=0;i<h;i++)
		{
			for (int j=0;j<w;j++)
			{
				printf("%c ", 'a'+col[nom(h,w,i,j)]);
			}
			printf("\n");
		}
	}
	

	return 0;
}
