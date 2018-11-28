#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
	freopen("f:\\A-small-attempt0.in", "r", stdin);
	freopen("f:\\A-small-attempt0.out", "w", stdout);
	int T, N, K;
	scanf("%d", &T);
	for (int t_case = 1; t_case <= T; t_case++)
	{
		scanf("%d %d", &N, &K);
		if ((((1<<N)-1)&(K+1)) == 0)
			printf("Case #%d: ON\n", t_case);
		else
			printf("Case #%d: OFF\n", t_case);
	}

	return 0;
}
