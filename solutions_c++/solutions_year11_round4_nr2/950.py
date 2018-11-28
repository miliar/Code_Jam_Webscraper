#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <memory>
#include <cctype>
#include <vector>
#include <string>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;  
#ifdef LOCAL_MASHINE
typedef __int64 long long;
#endif
typedef long long INT64;
#define min(a,b) ((a)<(b)?a:b)
#define max(a,b) ((a)>(b)?a:b)
#define sz(a) int((a).size())
#define INF 2000000000

int t,T;
char s[505][505];
int a[505][505];
int m[505][505];
double zx[505][505];
double zy[505][505];
double px, py;
int sm;

int n;
int c,r,d;
int i,j;
int k;

double cent(int m1, double p1, int m2, double p2)
{
	return (p1*m1+p2*m2)/(m1+m2);
}

void solve()
{
	for(k=min(c,r); k>=3; k--)
	{
		for(i=r-k+1; i>0; i--)
		{
			for (j=c-k+1; j>0; j--)
			{
				px = zx[i+k-1][j+k-1];
				py = zy[i+k-1][j+k-1];
				sm = m[i+k-1][j+k-1];
				px = cent(sm, px, -m[i-1][j+k-1], zx[i-1][j+k-1]);
				py = cent(sm, py, -m[i-1][j+k-1], zy[i-1][j+k-1]);
				sm -= m[i-1][j+k-1];
				px = cent(sm, px, -m[i+k-1][j-1], zx[i+k-1][j-1]);
				py = cent(sm, py, -m[i+k-1][j-1], zy[i+k-1][j-1]);
				sm -= m[i+k-1][j-1];
				px = cent(sm, px, m[i-1][j-1], zx[i-1][j-1]);
				py = cent(sm, py, m[i-1][j-1], zy[i-1][j-1]);
				sm += m[i-1][j-1];

				px = cent(sm, px, -a[i][j], j);
				py = cent(sm, py, -a[i][j], i);
				sm -= a[i][j];

				px = cent(sm, px, -a[i+k-1][j], j);
				py = cent(sm, py, -a[i+k-1][j], i+k-1);
				sm -= a[i+k-1][j];

				px = cent(sm, px, -a[i][j+k-1], j+k-1);
				py = cent(sm, py, -a[i][j+k-1], i);
				sm -= a[i][j+k-1];

				px = cent(sm, px, -a[i+k-1][j+k-1], j+k-1);
				py = cent(sm, py, -a[i+k-1][j+k-1], i+k-1);
				sm -= a[i+k-1][j+k-1];
				
				if (abs(px-(j+(k-1)/2.0))<1e-7 &&
					abs(py-(i+(k-1)/2.0))<1e-7)
				{
					printf("Case #%d: %d\n", t, k);
					return;
				}
			}
		}
	}

	printf("Case #%d: IMPOSSIBLE\n", t);
}

int main()
{
	freopen("B-small-attempt3.in", "r", stdin);
	freopen("B-small-attempt3.out", "w", stdout);

	scanf("%d", &T);
	for (t=1; t<=T; t++)
	{
		memset(m,0,sizeof(m));
		memset(zx,0,sizeof(zx));
		memset(zy,0,sizeof(zy));

		scanf("%d%d%d", &r,&c,&d);
		for(i=0; i<r; i++)
		{
			scanf("%s", s[i]);
			for(j=0; j<c; j++)
			{
				a[i+1][j+1]=s[i][j]-'0'+d;
			}
		}

		
		for(i=1; i<=r; i++)
		{
			for (j=1; j<=c; j++)
			{
				px = j;
				py = i;
				sm=a[i][j];

				px = cent(sm, px, m[i][j-1], zx[i][j-1]);
				py = cent(sm, py, m[i][j-1], zy[i][j-1]);
				sm+=m[i][j-1];

				px = cent(sm, px, m[i-1][j], zx[i-1][j]);
				py = cent(sm, py, m[i-1][j], zy[i-1][j]);
				sm+=m[i-1][j];

				px = cent(sm, px, -m[i-1][j-1], zx[i-1][j-1]);
				py = cent(sm, py, -m[i-1][j-1], zy[i-1][j-1]);
				sm-=m[i-1][j-1];
				
				m[i][j]=sm;
				zx[i][j]=px;
				zy[i][j]=py;
			}
		}

		solve();

	}

	return 0;
}
/*
1
3 3 1
111
111
111
*/
