#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <set>

using namespace std;

const int MaxN = 1000 + 10;

int N, W, L;
int R[MaxN], Ord[MaxN], ROrd[MaxN];
int X[MaxN], Y[MaxN];

int qq[MaxN * 5], nqq;

void Work()
{
	scanf("%d%d%d", &N, &W, &L);
	for (int i = 0; i < N; i ++)
	{
		scanf("%d", &R[i]);
		Ord[i] = i;
	}
	for (int i = 0; i < N; i ++)
		for (int j = 0; j < N; j ++)
			if (R[Ord[i]] > R[Ord[j]])
				swap(Ord[i], Ord[j]);
	for (int i = 0; i < N; i ++)
		ROrd[Ord[i]] = i;

	X[0] = Y[0] = 0;
	for (int i = 1; i < N; i ++)
	{
		int r = R[Ord[i]];
		
		nqq = 0;
		qq[nqq ++] = -r;
		qq[nqq ++] = -r + W;
		for (int j = 0; j < i; j ++)
		{
			if (X[j] - R[Ord[j]] >= -r)
				qq[nqq ++] = (X[j] - R[Ord[j]]);
			if (X[j] + R[Ord[j]] <= W + r)
				qq[nqq ++] = (X[j] + R[Ord[j]]);
		}
		int F = 1;
		for (int pp = 0; pp < nqq; pp ++)
		{
			if (qq[pp] + r > W)
				continue;
			int Left = qq[pp];
			int Top = 0;
			for (int j = 0; j < i; j ++)
				if (X[j] + R[Ord[j]] > qq[pp] && X[j] - R[Ord[j]] < qq[pp] + r + r)
					Top = max(Top, Y[j] + R[Ord[j]]);
			int FirstX = (Left == 0) ? 0 : (Left + r);
			int FirstY = (Top == 0) ? 0 : (Top + r);
			if (FirstY <= L)
			{
				if (F || FirstY < Y[i])
				{
					F = 0;
					X[i] = FirstX;
					Y[i] = FirstY;
				}
			}
		}
	}
	for (int i = 0; i < N; i ++)
		printf(" %d %d", X[ROrd[i]], Y[ROrd[i]]);
	printf("\n");
	fflush(stdout);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		printf("Case #%d:", Case);
		Work();
	}
	return 0;
}