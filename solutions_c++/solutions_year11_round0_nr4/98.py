#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MaxN = 1 << 10;

int N, T;

int Work()
{
	int Cnt = 0;
	scanf("%d", &N);
	for (int i = 1; i <= N; i ++)
	{
		scanf("%d", &T);
		Cnt += (i != T);
	}
	return Cnt;
}

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);

	int Cases;
	scanf("%d", &Cases);
	for (int i = 1; i <= Cases; i ++)
		printf("Case #%d: %d.000000\n", i, Work());
	return 0;
}