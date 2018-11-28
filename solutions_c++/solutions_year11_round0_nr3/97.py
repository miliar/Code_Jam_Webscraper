#include <cstdio>
#include <algorithm>

using namespace std;

const int MaxN = 1 << 10;
const int Max = 1 << 20;

int N;
int C[MaxN];

void Work()
{
	scanf("%d", &N);
	int Ans = 0, Tot = 0, Min = 1000000000;
	for (int i = 0; i < N; i ++)
	{
		scanf("%d", &C[i]);
		Ans ^= C[i];
		Min = min(Min, C[i]);
		Tot += C[i];
	}
	if (Ans)
	{
		printf("NO\n");
		return;
	}
	printf("%d\n", Tot - Min);
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int i = 1; i <= Cases; i ++)
	{
		printf("Case #%d: ", i);
		Work();
	}
	return 0;
}