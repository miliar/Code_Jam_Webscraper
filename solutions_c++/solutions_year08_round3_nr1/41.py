#include <cstdio>
#include <algorithm>
#include <functional>

using namespace std;

int P, K, L;
int letters[1024];

void input(void)
{
	scanf("%d %d %d", &P, &K, &L);
	for(int i = 0; i < L; ++i)
	{
		scanf("%d", &letters[i]);
	}
}

long long calc(void)
{
	long long res = 0;
	
	sort(letters, letters+L, greater<int>());
	for(int i = 0; i < L; ++i)
	{
		res += letters[i] * (i/K + 1);
	}
	
	return res;
}

int main(void)
{
	int N, i;
	
	scanf("%d", &N);
	fprintf(stderr, "cases=%d\n", N);
	for(i = 1; i <= N; ++i)
	{
		fprintf(stderr, "%d\n", i);
		input();
		if(L > P*K)
		{
			printf("Case #%d: Impossible\n", i);
		}
		else
		{
			printf("Case #%d: %Ld\n", i, calc());
		}
	}
	return 0;
}
