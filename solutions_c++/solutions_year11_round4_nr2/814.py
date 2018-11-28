#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 20;
char g[N][N];

int r, c, d;

bool check1(int x, int y, int len)
{
	int sum = 0;
	int sx = 0, sy = 0;
	for (int i = x-len; i <= x+len; i++)
		for (int j = y-len; j <= y+len; j++)
		{
			if ((i == x-len || i == x+len) && (j == y-len || j == y+len)) continue;
			int dx = i-x;
			int dy = j-y;
			sx += dx * ((g[i][j]-'0') + d);
			sy += dy * ((g[i][j]-'0') + d);
			sum += (g[i][j]-'0');
		}
	
	return sx == 0 && sy == 0;
}
bool check2(int x1, int x2, int y1, int y2, double cx, double cy)
{
	int sum = 0;
	double sx = 0, sy = 0;
	for (int i = x1; i <= x2; i++)
		for (int j = y1; j <= y2; j++)
		{
			if ((i == x1 || i == x2) && (j == y1 || j == y2)) continue;
			double dx = i-cx;
			double dy = j-cy;
			sx += dx * ((g[i][j]-'0') + d);
			sy += dy * ((g[i][j]-'0') + d);
			sum += (g[i][j]-'0');
		}
	double eps = 1e-9;
	return fabs(sx) < eps  && fabs(sy) < eps;
}
int work()
{
	scanf("%d%d%d", &r, &c, &d);
	for (int i = 0; i < r; i++)
		scanf("%s", &g[i]);

	int ret = -1;

	//printf("%d\n", check(3,3,1));
	//printf("%d\n", check(3,3,2));

	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
		{
			int l1 = min(i, r-i-1);
			int l2 = min(j, c-j-1);
			int maxl = min(l1, l2);
			for (int len = 1; len <= maxl; len++)
				if (check1(i, j, len))
						ret = max(ret, len * 2 + 1);
		}
	for (int i = 0; i < r+1; i++)
		for (int j = 0; j < c-1; j++)
		{
			double ii = 0.5+i;
			double jj = 0.5+j;
			int len1 = min(i+1, r-i-1);
			int len2 = min(j+1, c-j-1);
			int maxl = min(len1, len2);
			for (int len = 2; len <= maxl; len++)
				if (check2(i-len+1, i+len, j-len+1, j+len, ii, jj))
					ret = max(ret, len*2);
		}


	return ret;
}

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int testcase = 1; testcase <= T; testcase++)
	{
		int ret = work();
		printf("Case #%d: ", testcase);
		if (ret == -1)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%d\n", ret);
		}
	}
}