#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

const int maxn = 610;

int a[maxn][maxn];
int n;

void init()
{
	memset(a, 0,sizeof(a));
	scanf("%d", &n);
	for (int i=0; i<n; i++)
	{
		int x1, y1, x2, y2;
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		for (int x=x1; x<=x2; x++)
			for (int y = y1; y<=y2; y++)
				a[x][y] = 1;
	}
}

int solve()
{
	int ans = 0;
	while (true)
	{
		int total = 0;
		for (int i=0; i<110; i++)
			for (int j=0; j<110; j++)
				total+=a[i][j];
		if (total==0)
			break;

		for (int i=110; i>0; i--)
			for (int j=110; j>0; j--)
				if (i==0||j==0)
					a[i][j] = 0;
				else
				{
					if (a[i-1][j]==1&&a[i][j-1]==1)
						a[i][j] =1;
					else if (a[i-1][j]==0&&a[i][j-1]==0)
						a[i][j] = 0;
				}
		ans++;
	}
	return ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T = 0;
	scanf("%d", &T);
	for (int i=0; i<T; i++) {
		init();
		printf("Case #%d: %d\n", i+1, solve());
	}
}