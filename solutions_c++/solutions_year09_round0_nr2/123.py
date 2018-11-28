#include <iostream>
#include <algorithm>
#include <cstdio>
#include <map>
#include <set>
#include <list>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i(a), _n(b); i<=_n; i++)
#define FR(i,b) FOR(i,0,b-1)
#define REP(i,a,b) for(int i(a), _n(b); i >= _n; i--)
#define _M(a) memset(a,0,sizeof(a))
#define IN scanf
#define OUT printf
#define sqr(q) ((q)*(q))
#define ll long long
#define ul unsigned ll
#define INF 1000000000

int KT;
char u;
int a[102][102];
char f[102][102];
int n, m;

void get(int c,int t)
{
	int i(c), j(t);
	int d, k;
	
	while (1)
	{
		d = 0;
		k = INF;
		
		if (i > 0   && k > a[i-1][j]) d = 0, k = a[i-1][j];
		if (j > 0   && k > a[i][j-1]) d = 1, k = a[i][j-1];
		if (j < m-1 && k > a[i][j+1]) d = 2, k = a[i][j+1];
		if (i < n-1 && k > a[i+1][j]) d = 3, k = a[i+1][j];
		if (k >= a[i][j]) break;
	
		if (d == 0) i--;
		if (d == 1) j--;
		if (d == 2) j++;
		if (d == 3) i++;
		
		if (f[i][j] != 0) break;
	}
	char r ;
	if (f[i][j] != 0) r = f[i][j]; else
	r = u++;
	
	i=c, j=t;

	
	while (1)
	{
		d = 0;
		k = INF;
		f[i][j] = r;
		if (i > 0   && k > a[i-1][j]) d = 0, k = a[i-1][j];
		if (j > 0   && k > a[i][j-1]) d = 1, k = a[i][j-1];
		if (j < m-1 && k > a[i][j+1]) d = 2, k = a[i][j+1];
		if (i < n-1 && k > a[i+1][j]) d = 3, k = a[i+1][j];
		
		if (k >= a[i][j]) break;
		
		if (d == 0) i--;
		if (d == 1) j--;
		if (d == 2) j++;
		if (d == 3) i++;
		
		if (f[i][j] != 0) break;
	}	
}


int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	IN("%d", &KT);
	
	FOR(test, 1, KT)
	{
		IN("%d%d", &n, &m);
		FR(i,n) FR(j,m) IN("%d", &a[i][j]);
		u = 'a';
		_M(f);
		FR(i,n) FR(j,m) if (f[i][j] == 0) get(i,j);
		OUT("Case #%d:\n", test);
		FR(i,n)
		{
			FR(j,m-1) OUT("%c ", f[i][j]);
			OUT("%c\n", f[i][m-1]);
		}
	}
	

	return 0;
}
