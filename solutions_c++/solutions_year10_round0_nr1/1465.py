#include <stdio.h>

long long T, N, K;

bool Func()
{
	long long mask = 1;

	if( K == 0 )
		return false;

	for(int i = 0; i < N; i++)
	{
		long long ans = K & mask;

		if( ans == 0 )
			return false;
		
		mask = mask << 1;
	}

	return true;
}


int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	scanf("%d", &T);

	for(int i = 0; i < T; i++)
	{
		scanf("%d%d", &N, &K);

		printf("Case #%d: ", i+1);
		
		if( Func() )
			printf("ON\n");
		else
			printf("OFF\n");
	}

	return 0;
}