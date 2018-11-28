#include <cstdio>
using namespace std;

int T,N,K;

int main()
{
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d %d", &N, &K);
		int mx = (1 << N);
		if(K%mx == mx-1)
			printf("Case #%d: ON\n", t);
		else
			printf("Case #%d: OFF\n", t);
	}
	return 0;
}
