#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int TC, N, K, B, T;
int X[64], V[64];
int P[64];

bool can[64];

int main()
{
	freopen("f:\\B-small-attempt0.in", "r", stdin);
	freopen("f:\\B-small-attempt0.out", "w", stdout);

	scanf("%d", &TC);
	for (int t_case = 1; t_case <= TC; t_case++)
	{
		scanf("%d %d %d %d", &N, &K, &B, &T);
		for (int i = 0; i < N; i++)
			scanf("%d", &X[i]);
		for (int i = 0; i < N; i++)
			scanf("%d", &V[i]);
		
		int ct = 0;
		for (int i = 0; i < N; i++)
		{
			can[i] = V[i] * T >= B - X[i];
			ct += (can[i] ? 1 : 0);
		}


		if (ct < K)
		{
			printf("Case #%d: IMPOSSIBLE\n", t_case);
		}
		else
		{
			vector<int> v;
			for (int i = 0; i < N; i++) if (can[i])
			{
				int c = 0;
				for (int j = i + 1; j < N; j++) if (can[j] == false)
					c++;
				v.push_back(c);
			}
			sort(v.begin(), v.end());
			int res = 0;
			for (int i = 0; i < K; i++)
				res += v[i];
			printf("Case #%d: %d\n", t_case, res);
		}
	}
	return 0;
}
