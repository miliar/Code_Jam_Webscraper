#include <stdio.h>


#define N 1000

int main()
{
	int t1, n;

	//freopen("input.txt", "r", stdin);

	scanf("%d", &t1);


	int a[N], b[N];

	for (int t = 0; t < t1; t++)
	{
		scanf("%d", &n);

		printf("Case #%d: ", t + 1);

		for (int i = 0; i < n; i++)
		{
			scanf("%d%d", &a[i], &b[i]);
			
		}

		if (n == 1)
		{
			printf("0\n");
			continue;
		}

		if (n == 2)
		{
			if ((a[0] < a[1] && b[0] > b[1]) || (a[0] > a[1] && b[0] < b[1]))
			{
				printf("1\n");
			}
			else
			{
				printf("0\n");
			}
			continue;
		}

		int res = 0;
		
		for (int i = 0; i < n; i++)
		{
			for (int j = i + 1; j < n; j++)
			{
				if ((a[i] < a[j] && b[i] > b[j]) || (a[i] > a[j] && b[i] < b[j]))
				{
					res++;
				}
			}
			
				
		}
			printf("%d\n", res);


		
	}





	return 0;
}