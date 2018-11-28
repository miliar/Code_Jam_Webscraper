#if 1

#include <cstdio>
#include <cstring>

typedef long long T;

const int SZ = 10001;
T sound[SZ];
int N, L, H;

T cal()
{
	T result;
	T i, j;
	for (i = L; i <= H; i++)
	{
		result = i;
		for (j = 0; j < N; j++)
		{
			if (i % sound[j] != 0 && sound[j] % i != 0)
			{
				result = -1;
			}
		}
		if (result != -1) break;
	}
	return result;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int TT;
	scanf("%d", &TT);
	int t;
	for (t = 1; t <= TT; t++)
	{
		printf("Case #%d: ", t);
		scanf("%d%d%d", &N, &L, &H);
		int i;
		for (i = 0; i < N; i++)
		{
			scanf("%d", &sound[i]);
		}
		T result = cal();
		if (result == -1) printf("NO\n");
		else printf("%ld\n", result);
	}
	return 0;
}

#endif