#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MaxN = 256;

int N;
int Now[MaxN][MaxN], Next[MaxN][MaxN];

int Work()
{
	scanf("%d", &N);
	memset(Now, 0, sizeof(Now));
	for (int i = 0; i < N; i ++)
	{
		int x1, y1, x2, y2;
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		for (int x = x1; x <= x2; x ++)
			for (int y = y1; y <= y2; y ++)
				Now[x][y] = 1;
	}
	for (int Step = 0; ; Step ++)
	{
		int Cnt = 0;
		for (int x = 0; x < MaxN; x ++)
			for (int y = 0; y < MaxN; y ++)
				Cnt += Now[x][y];
		if (Cnt == 0)
			return Step;
		for (int x = 0; x < MaxN; x ++)
			for (int y = 0; y < MaxN; y ++)
			{
				Cnt = 0;
				if (x != 0 && Now[x - 1][y])
					Cnt ++;
				if (y != 0 && Now[x][y - 1])
					Cnt ++;
				Next[x][y] = ((Now[x][y] && Cnt) || Cnt == 2);
			}
		memcpy(Now, Next, sizeof(Now));
	}
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
		printf("Case #%d: %d\n", Case, Work());
	return 0;
}
