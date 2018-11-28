#include <cstdio>
#include <algorithm>

using namespace std;

int Work()
{
	int N;
	scanf("%d", &N);
	int CurO = 1, CurB = 1, TimeO = 0, TimeB = 0, Ans = 0;
	char Buf[10];
	int To;
	for (int i = 0; i < N; i ++)
	{
		scanf("%s%d", &Buf, &To);
		if (Buf[0] == 'O')
		{
			TimeO = max(TimeB, TimeO + abs(CurO - To)) + 1;
			CurO = To;
		}
		else
		{
			TimeB = max(TimeO, TimeB + abs(CurB - To)) + 1;
			CurB = To;
		}
	}
	return max(TimeB, TimeO);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int i = 1; i <= Cases; i ++)
		printf("Case #%d: %d\n", i, Work());
	return 0;
}