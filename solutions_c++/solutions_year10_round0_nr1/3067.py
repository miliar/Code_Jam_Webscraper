#include <stdio.h>
#include <stdlib.h>

int main()
{
	int cases, N, K, num = 1, comb, i;
	char data[1000];
	bool on;

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%i", &cases);
	while(cases--)
	{
		scanf("%i %i\n", &N, &K);
		comb = 1;
		for(i = 1; i <= N; i++)
			comb <<= 1;
		while(K >= comb)
			K -= comb;
		itoa(K, data, 2);
		on = true;
		for(i = 0; data[i]; i++)
		{
			if(data[i] == '0')
			{
				on = false;
				break;
			}
		}
		if(on && i == N) printf("Case #%i: ON\n", num++);
		else printf("Case #%i: OFF\n", num++);
	}

	return 0;
}