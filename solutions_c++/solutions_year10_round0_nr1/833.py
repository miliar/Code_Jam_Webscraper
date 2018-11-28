#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;
typedef long long Long;


int main()
{
	int T;
	freopen("A-small.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &T);
	for (int k = 1 ; k <= T ; ++k)
	{
		int N, K;
		scanf("%d%d", &N, &K);
		Long l = 1;
		l = l << N;
		if ((K & (l - 1)) == (l - 1))
		{
			printf("Case #%d: ON\n", k);
		}
		else
		{
			printf("Case #%d: OFF\n", k);
		}
	}

	return 0;
}
