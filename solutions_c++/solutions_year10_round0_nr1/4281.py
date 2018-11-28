

#include <stdio.h>
#include <stdlib.h>

int main()
{
	int state[50], n=2, k=4, isOn=1, t=0;

	FILE *fl = fopen("A-small-attempt1.in", "r");
	fscanf(fl, "%d", &t);
	
	FILE *fl2 = fopen("A-small.out", "w");

	for (int p=0; p < t; p++)
	{
		isOn=1;
	
		fscanf(fl, "%d", &n);
		fscanf(fl, "%d", &k);

//printf("%d %d \n", n, k);

		for (int u=0; u < n;u++)
			state[u] = 0;			//OFF

		for (int i=0; i < k; i++)
			for (int u=(n-1); u >= 0;u--)
			{
				if (state[u] == 0)
				{
					state[u] = 1;
					
					for (int q=(u-1); q >= 0; q--)
						if (state[q] == 0)
						{
							state[u] = 0;	//REVERT
							break;
						}					
				}
				else
				{
					state[u] = 0;

					for (int q=(u-1); q >= 0; q--)
						if (state[q] == 0)
						{
							state[u] = 1;	//REVERT
							break;
						}			
				}
			}
			
		for (int q=0; q < n;q++)
		{
			//printf("state %d = %d\n", q, state[q]);
			if (state[q] == 0)
				isOn = 0;
		}

//		printf("%d\n", isOn);
		if (isOn)
			fprintf(fl2, "Case #%d: ON\n", p+1);
		else
			fprintf(fl2, "Case #%d: OFF\n", p+1);
	}


	return 0;
}
