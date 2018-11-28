#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MaxN = 1 << 10;
const int Max = 1 << 20;

int C, D, N;
char Combine[26][26];
int Oppose[26][26];
char Buf[1000];
char Current[1000];
int Len;

void Work()
{
	memset(Combine, -1, sizeof(Combine));
	memset(Oppose, 0, sizeof(Oppose));
	scanf("%d", &C);
	while (C --)
	{
		scanf("%s", Buf);
		Combine[Buf[0] - 'A'][Buf[1] - 'A'] = Combine[Buf[1] - 'A'][Buf[0] - 'A'] = Buf[2] - 'A';
	}
	scanf("%d", &D);
	while (D --)
	{
		scanf("%s", Buf);
		Oppose[Buf[0] - 'A'][Buf[1] - 'A'] = Oppose[Buf[1] - 'A'][Buf[0] - 'A'] = 1;
	}
	scanf("%d%s", &N, &Buf);
	Len = 0;
	for (int i = 0; i < N; i ++)
	{
		Buf[i] -= 'A';
		if (Len != 0 && Combine[Current[Len - 1]][Buf[i]] != -1)
			Current[Len - 1] = Combine[Current[Len - 1]][Buf[i]];
		else
			Current[Len ++] = Buf[i];
		for (int x = 0; x < Len - 1; x ++)
			if (Oppose[Current[x]][Current[Len - 1]])
				Len = 0;
	}
	printf("[");
	for (int i = 0; i < Len; i ++)
	{
		printf("%c", Current[i] + 'A');
		if (i != Len - 1)
			printf(", ");
	}
	printf("]\n");
			
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int i = 1; i <= Cases; i ++)
	{
		printf("Case #%d: ", i);
		Work();
	}
	return 0;
}