#include <stdio.h>
#include <algorithm>
using namespace std;

bool f(const int T, const int N, const int K)
{
	int mask = 0;
	for(int i = 0; i < K; ++i)
	{
		for(int j = 0; j < N; ++j)
		{
			if(mask & 1<<j)
			{
				mask = mask & (~(1<<j));
			}
			else
			{
				mask |= 1<<j;
				break;
			}
		}

	}
	return ((0xFFFFFFFF<<N) | mask) == 0xFFFFFFFF;
}

int main()
{
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	int T;	
	
	scanf("%d", &T);
	for (int tcase = 0; tcase < T; ++tcase)
	{
		int N, K;
		scanf("%d %d", &N, &K);	

		if (f(T, N, K)) 
		{
			printf("Case #%d: ON\n", tcase + 1);
		}
		else {
			printf("Case #%d: OFF\n", tcase + 1);
		}
		
	}
	return 0;
}