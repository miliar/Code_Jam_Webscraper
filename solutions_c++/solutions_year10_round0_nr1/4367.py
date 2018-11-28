#include <stdio.h>




int main()
{
	bool state[1000];
	bool power[1000];

	int T, N, K;

	scanf("%d\n", &T);

	for (int t = 0; t < T; t++)
	{
		scanf("%d %d\n", &N, &K);

		// run a case
		// N snappers total
		// K finger snaps

		
		for (int n = 0; n < N; n++) state[n] = false;
		for (int n = 0; n < N; n++) power[n] = false;
		power[0] = true;

		for (int k = 0; k < K; k++)
		{

			// snap!
			for (int n = 0; n < N; n++)
				if (power[n]) state[n] = !(state[n]);

			// propogate power
			for (int n = 1; n < N; n++)
			{
				if (power[n-1] && state[n-1]) power[n] = true;
				else power[n] = false;
			}

		}

		if (power[N-1] && state[N-1]) printf("Case #%d: ON\n", t+1);
		else printf("Case #%d: OFF\n", t+1);
	}

	char str[100];
	scanf("%s", str);

	return 0;
}