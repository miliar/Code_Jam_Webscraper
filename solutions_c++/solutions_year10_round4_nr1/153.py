#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

const int maxn = 610;

int k, sum, total;
int b[maxn][maxn];
int a[maxn][maxn];
int c[maxn][maxn];
int d[maxn][maxn];
int qx[100000];
int qy[100000];

void init()
{
	total = 0;
	memset(a, 0, sizeof(a));
	memset(b, 0, sizeof(b));
	scanf("%d", &k);
	sum = (k+1)*k - k;
	for (int i=0; i<2*k - 1; i++)
	{
		int ed = i+1;
		if (i>=k)
			ed = 2 * k - i - 1;
		for (int j=0; j<ed; j++)
		{
			int x = 2 * k + k - ed + j * 2, y = 2 * k + i;
			scanf("%d", &a[y][x]);
			b[y][x] = 1;
			qx[total] = y;
			qy[total] = x;
			total++;
		}
	}
}

int solve()
{
	int ans = (2*k + 1)*k;
	for (int i= 2 * k; i< 4 * k; i++)
		for (int j= 2 * k; j < 4 * k; j++)
		{
			memset(c, 0, sizeof(c));
			memset(d, 0, sizeof(d));
			int cur = 0;
			bool flag = true;
			for (int t =0; t<total; t++)
			{
				int x = 2 * i - qx[t];
				int y = qy[t];
				if (d[x][y] == 0 && b[x][y] == 0)
				{
					d[x][y] = 1;
					c[x][y] = a[qx[t]][qy[t]];
				}
				else if (b[x][y] == 1 && a[qx[t]][qy[t]] != a[x][y])
				{
					flag = false;
					break;
				}
				else if (d[x][y] == 1 && a[qx[t]][qy[t]] != c[x][y])
				{
					flag = false;
					break;
				}

				x = qx[t];
				y = 2 * j - qy[t];
				if (d[x][y] == 0 && b[x][y] == 0)
				{
					d[x][y] = 1;
					c[x][y] = a[qx[t]][qy[t]];
				}
				else if (b[x][y] == 1 && a[qx[t]][qy[t]] != a[x][y])
				{
					flag = false;
					break;
				}
				else if (d[x][y] == 1 && a[qx[t]][qy[t]] != c[x][y])
				{
					flag = false;
					break;
				}				
			}
			int x = i-2*k, y= (j-2*k)/2;
			cur = (2*k - x);
			if (2*k-y>cur) cur = 2*k - y;
			if (x>cur) cur = x;
			if (y>cur) cur = y;

			if ((cur + 1)*cur - cur - sum < ans && flag)
				ans = (cur + 1)*cur - cur - sum;
		}
	return ans;
}

int main()
{
	int T = 0;
	scanf("%d", &T);
	for (int i=0; i<T; i++) {
		init();
		printf("Case #%d: %d\n", i+1, solve());
	}
}