#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

#define two(x) (1<<(x))

int M[2048], N;

int solve(int l, int r)
{
	for (int i = l; i <= r; i++)
		if (M[i] <= 0) return 0;
	for (int i = l; i <= r; i++)
		M[i]--;
	return 1;
}

int main()
{
	freopen("f:\\B-small-attempt2.in", "r", stdin);
	freopen("f:\\B-small-attempt2.out", "w", stdout);

	int P, T;
	scanf("%d", &T);
	for (int t_case = 1; t_case <= T; t_case++)
	{
		scanf("%d", &P);
		N = two(P);
		int sum = 0;
		for (int i = 0; i < N; i++)
		{
			scanf("%d", &M[i]);
			sum += M[i];
		}
		
		int res = N - 1;

		for (int i = 1; i <= P; i++)
		{
			for (int j = 0; j < N; j += two(i))
			{
				res -= solve(j, j + two(i) - 1);
				int x;
				scanf("%d", &x);
			}
		}

		printf("Case #%d: %d\n", t_case, res);
	}
	return 0;
}
