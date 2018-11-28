#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std; 
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("GCJ_C.txt", "w", stdout);
	int T, N, tcnt = 0;
	int candy[1010];
	scanf("%d", &T);
	for (int tcnt = 1; tcnt <= T; tcnt++)
	{
		scanf("%d", &N);
		int tot = 0, minCandy = 0x3fffffff, w = 0;
		for (int i = 0; i < N; i++)
		{
			scanf("%d", &candy[i]);
			tot ^= candy[i];
			minCandy = minCandy < candy[i] ? minCandy : candy[i];
			w += candy[i];
		}
		printf("Case #%d: ", tcnt);
		if (tot)
		{
			printf("NO\n");
		}
		else
			printf("%d\n", w - minCandy);
		
	}
	return 0;
}
