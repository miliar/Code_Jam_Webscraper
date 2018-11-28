#include <stdio.h>

int t;

int main()
{
	int n, k;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ", i + 1);
		scanf("%d%d", &n, &k);
		if (k < n)
		{
			printf("OFF\n");
		}
		else if ((k + 1) % (1 << n) == 0)
		{
			printf("ON\n");
		}
		else 
		{
			printf("OFF\n");
		}

	}

	return 0;

}