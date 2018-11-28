#include <stdio.h>


int g[1000];
int sum[1000];
int next[1000];

int main()
{
	int t;
	int r, k, n;


	scanf("%d", &t);
	
	int ce = 0;


	FILE *fout = fopen("c.out","w");

	while(t--)
	{
		scanf("%d %d %d", &r, &k, &n);
		

		for (int i = 0; i < n; i++)
			scanf("%d", &g[i]);

		for (int i = 0; i < n; i++) 
		{
			sum[i] = 0;
			next[i] = i + 1;
			for (int j = i; ;)
			{
				if (sum[i] + g[j] > k || (sum[i] != 0 && i == j))
				{
					next[i] = j;
					break;
				}
				sum[i] = sum[i] + g[j];
				j = j + 1;
				j = j % n;
			}
		}

		int index = 0;
		int cost = 0;

		for (int i = 0; i < r; i++)
		{
			cost += sum[index];
			index = next[index];
		}
		ce++;
		fprintf(fout,"Case #%d: %d\n",ce, cost );
	}
	fclose(fout);
	return 0;
}