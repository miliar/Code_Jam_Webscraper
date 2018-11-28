#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <memory.h>
#include <map>
#include <set>
#include <vector>
#include <functional>
#include <algorithm>
using namespace std;

#define N 16

int m, n, d, K;
int s[N][N];

int IsCorner(int i, int j)
{
	if (i==0 && j==0) return 1;
	if (i==K-1 && j==0) return 1;
	if (i==0 && j==K-1) return 1;
	if (i==K-1 && j==K-1) return 1;
	return 0;
}

int go(int r, int c)
{
	if (r+K>m || c+K>n) return 0;
	//double cx = (2*c+K-1)*0.5, cy = (2*r+K-1)*0.5;
	unsigned sum = 0;
	double tx = 0, ty = 0;
	for (int i = 0; i < K; ++i)
		for (int j = 0; j < K; ++j) if (!IsCorner(i, j))
		{
			tx += s[r+i][c+j]*j;
			ty += s[r+i][c+j]*i;
			sum += s[r+i][c+j];
		}
	tx /= sum; ty /= sum;
	return fabs(tx*2+1-K)<1e-6 && fabs(2*ty+1-K)<1e-6;
}

int main()
{
	int T, TT;
	scanf("%d", &TT);
	for (T = 1; T <= TT; ++T)
	{
		scanf("%d%d%d", &m, &n, &d);
		for (int i = 0; i < m; ++i)
			for (int j = 0; j  < n; ++j)
			{
				char c;
				scanf(" %c", &c);
				s[i][j] = d + c - '0';
			}
		for (K = min(m, n); K >= 3; --K)
			for (int i = 0; i < m; ++i)
				for (int j = 0; j  < n; ++j)
					if (go(i, j)) goto ans;
ans:
		printf("Case #%d: ", T);
		if (K >= 3) printf("%d\n", K); else puts("IMPOSSIBLE");
	}

	return 0;
}
