#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <assert.h>
using namespace std;

typedef long long LL;
typedef vector <string> vs;
typedef vector <int> vi;
typedef vector <LL> vll;
typedef vector <double> vd;
typedef pair <int,int> pii;

//////////////////

int tc, ntc;
int n;

int getlen(int n, int r)
{
	if (r < n) return r+1;
	return n+n-1-r;
}

int get_size(int n)
{
	return n*n;
}

int ar[400][400];
int xar[400][400];

inline bool same(int a, int b)
{
	if (a==-1 || b==-1) return true;
	return a == b;
}

int getx(int siz, int y, int x)
{
	if (y >= siz) y = siz+siz-2-y;
	int num = getlen( siz, y );

	if (num % 2 == 1)
	{
		x -= num / 2;
		return x * 2;
	}
	else
	{
		x *= 2;
		return x - (num - 1);
	}
}

int getid(int siz, int y, int x)
{
	if (y >= siz) y = siz+siz-2-y;
	int num = getlen( siz, y );

	if (num % 2 == 1)
	{
		x /= 2;
		return x + num / 2;
	}
	else
	{
		x += num - 1;
		return x / 2;
	}
}

bool symmetric(int siz, int i, int j)
{
	if (!same(xar[i][j], xar[i][ getlen(siz,i)-1-j ])) return false;
	if (!same(xar[i][j], xar[siz+siz-2-i][j])) return false;
	return true;
}

int overflow(int siz, int sy, int sx)
{
	int i, j;
	int cx = getx(siz, sy, sx);	
	for (i=0; i<n+n-1; i++)
		for (j=0; j<getlen(n, i); j++)
		{
			int tx = getx(n, i, j);
			int nx = getid(siz, sy+i, cx + tx);
			if (nx < 0) return 1;
			if (nx >= getlen(siz, sy+i)) return 2;
		}
	return 0;
}

bool ok1(int siz, int sy, int sx)
{
	int i, j;
	int cx = getx(siz, sy, sx);	
	for (i=0; i<n+n-1; i++)
	{
		int len = getlen(n, i);
		for (j=0; j<len; j++)
		{
			int tx = getx(n, i, j);
			int nx = getid(siz, sy+i, cx + tx);
			xar[sy+i][nx] = ar[i][j];
			if (!symmetric(siz,sy+i,nx)) goto ff;
		}
	}

	return true;	


ff:;
	for (i=0; i<n+n-1; i++)
		for (j=0; j<getlen(n, i); j++)
		{
			int tx = getx(n, i, j);
			int nx = getid(siz, sy+i, cx + tx);
			xar[sy+i][nx] = -1;
		}
	return false;

}

bool ok(int siz)
{
	int i, j;
	
	memset(xar, -1, sizeof(xar));

	for (i=0;i<siz+siz-1;i++)
	{
		if (i + n + n - 2 >= siz + siz - 1) break;

		for (j=0;j<getlen(siz,i);j++)
		{			
			int stat = overflow(siz,i,j);
			if (stat == 1) continue;
			if (stat == 2) break;

			if (ok1(siz,i,j)) return true;
		}
	}

	return false;
}

int main()
{
	FILE* fi = fopen("A-large.in", "r");
	FILE* fo = fopen("A-large.out", "w");

	fscanf(fi, "%d", &ntc);
	int i, j;
	for (tc = 1; tc <= ntc; tc++)
	{
		fscanf(fi, "%d", &n);
		for (i=0; i<n+n-1; i++)
			for (j=0; j<getlen(n, i); j++) fscanf(fi, "%d", &ar[i][j]);		

		int siz;
		for (siz=n;;siz++)
		{
			printf("%d\n", siz);
			if (ok(siz)) break;
		}
		
		int res = get_size(siz) - get_size(n);
		fprintf(fo, "Case #%d: %d\n", tc, res);
		printf("Case #%d: %d\n", tc, res);
	}
	return 0;
}