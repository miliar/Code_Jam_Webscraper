#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <map>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

#define inf 2000000001
#define ll long long
#define minim(a, b) ((a < b) ? a : b)
#define maxim(a, b) ((a > b) ? a : b)
#define pii pair<int, int>
#define pdd pair<double, double>
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define eps 1e-6

int R, C, D, bst;
char w[505][505];
int val[505][505];
ll sum[3][505][505];

inline int cmp(double a, double b)
{
	if (a + eps < b) return -1;
	if (b + eps < a) return +1;
	return 0;
}

double get_area(ll idx, int x1, int y1, int x2, int y2)
{
	return sum[idx][x2][y2] - sum[idx][x2][y1-1] - sum[idx][x1-1][y2] + sum[idx][x1-1][y1-1];
}

pdd center(int i, int j, int k)
{
	double sum = get_area(0, i-k+1, j-k+1, i, j);
	double sumx = get_area(1, i-k+1, j-k+1, i, j);
	double sumy = get_area(2, i-k+1, j-k+1, i, j);
	sum -= val[i-k+1][j-k+1] + val[i-k+1][j] + val[i][j-k+1] + val[i][j];
	sumx -= (ll)(i-k) * val[i-k+1][j-k+1] + (ll)(i-k) * val[i-k+1][j] + 
			(ll)(i-1) * val[i][j-k+1] + (ll)(i-1) * val[i][j];
	sumy -= (ll)(R-j+k-1) * val[i-k+1][j-k+1] + (ll)(R-j) * val[i-k+1][j] + 
			(ll)(R-j+k-1) * val[i][j-k+1] + (ll)(R-j) * val[i][j];
	
	return mp((sumx + 0.5 * sum) / sum, (sumy + 0.5 * sum) / sum);
}

pdd real_c(int i, int j, int k)
{
	if (k & 1)
		return mp(i-k + (k/2)+0.5, R-j + (k/2)+0.5);
	return mp(i-k + k/2, R-j + k/2);
}

int main()
{
	int T, tst;
	int i, j, k;
	
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	scanf("%d", &T);
	for (tst = 1; tst <= T; ++tst)
	{
		memset(w, 0, sizeof(w));
		
		scanf("%d %d %d", &R, &C, &D);
		for (i = 0; i < R; ++i)
			scanf("%s", w[i]);
		
		for (i = 0; i < R; ++i)
			for (j = 0; j < C; ++j)
				val[i+1][j+1] = w[i][j]-'0' + D;
		
		for (i = 1; i <= R; ++i)
			for (j = 1; j <= C; ++j)
			{
				sum[0][i][j] = sum[0][i-1][j] + sum[0][i][j-1] - sum[0][i-1][j-1] + val[i][j];
				sum[1][i][j] = sum[1][i-1][j] + sum[1][i][j-1] - sum[1][i-1][j-1] + (ll)val[i][j] * (i-1);
				sum[2][i][j] = sum[2][i-1][j] + sum[2][i][j-1] - sum[2][i-1][j-1] + (ll)val[i][j] * (R-j);			
			}
			
		pdd c, c1;
		bst = 0;
		for (i = 1; i <= R; ++i)
			for (j = 1; j <= C; ++j)
				for (k = 3; k <= i && k <= j; ++k)
				{
					c = center(i, j, k);
					c1 = real_c(i, j, k);
					// printf("? (%d %d): %.2lf %.2lf, %.2lf %.2lf\n", i, j, c.x, c.y, c1.x, c1.y);
					if (cmp(c.x, c1.x) == 0 && cmp(c.y, c1.y) == 0)
						bst = maxim(bst, k);
				}
			
		if (bst >= 3)
			printf("Case #%d: %d\n", tst, bst);
		else
			printf("Case #%d: IMPOSSIBLE\n", tst);
	}
	
	return 0;
}
