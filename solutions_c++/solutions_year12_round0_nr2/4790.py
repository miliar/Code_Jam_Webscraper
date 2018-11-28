#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int T, i, j, N, P, S, a[105], mem[105][105];

int solve(int i, int s)
{
	if(mem[i][s] != -1)
		return mem[i][s];
	if(i == N)
	{
		if(s == 0) 
			return 0;
		else
			return -1234567890;
	}
	int k, m, n;
	int res = 0;
	bool ok = false;
	for(k = 0; k <= 10 && k <= a[i]; k++)
		for(m = 0; m <= 10 && m + k <= a[i]; m++)
			for(n = 0; n <= 10 && k + m + n <= a[i]; n++)
				if(k + n + m == a[i])
				{
					if(abs(k - n) <= 1 && abs(k - m) <= 1 && abs(m - n) <= 1)
					{
						if(k >= P || n >= P || m >= P)
							res = max(res, 1 + solve(i + 1, s));
						else
							res = max(res, solve(i + 1, s));
					}
					else
						if(abs(k - n) <= 2 && abs(k - m) <= 2 && abs(m - n) <= 2 && s > 0)
						{
							if(k >= P || n >= P || m >= P)
								res = max(res, 1 + solve(i + 1, s - 1));
							else
								res = max(res, solve(i + 1, s - 1));
						}
				}
	return mem[i][s] = res;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	scanf("%d", &T);
	for(j = 1; j <= T; j++)
	{
		memset(mem, -1, sizeof(mem));
		scanf("%d %d %d", &N, &S, &P);
		for(i = 0; i < N; i++)
			scanf("%d", &a[i]);
		printf("Case #%d: %d\n", j, solve(0, S));
	}
	return 0;
}