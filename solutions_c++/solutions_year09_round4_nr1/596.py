#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

char M[64][64];
int B[64], A[64];
bool used[64];

int main()
{
	freopen("f:\\A-small-attempt0.in", "r", stdin);
	freopen("f:\\A-small.outu", "w", stdout);
	int T, N;
	scanf("%d", &T);
	for (int t_case = 1; t_case <= T; t_case++)
	{
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
		{
			scanf("%s", M[i]);
			int j;
			for (j = N - 1; j >= 0; j--)
				if (M[i][j] == '1') break;
			if (j < 0) j = 0;
			B[i] = j;
		}
		memset(used, 0, sizeof(used));
		for (int i = 0; i < N; i++)
		{
			for (int j = B[i]; j < N; j++)
			{
				if (!used[j])
				{
					used[j] = true;
					A[i] = j;
					break;
				}
			}
		}
		int res = 0;
		for (int i = 0; i < N; i++)
			for (int j = i + 1; j < N; j++)
				if (A[i] > A[j]) res++;
		printf("Case #%d: %d\n", t_case, res);
	}
	return 0;
}
