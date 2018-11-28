#include <stdio.h>

const int SIZE = 400;

int data[SIZE][SIZE], ans;

void init()
{
	int i, j;

	for(i = 0; i < SIZE; i++)
		for(j = 0; j < SIZE; j++)
			data[i][j] = 0;
}

void process()
{
	int i, j;
	int copy[SIZE][SIZE];

	for(ans = 0;; ans++)
	{
		/*for(i = 0; i < 6; i++)
		{
			for(j = 0; j < 6; j++)
				printf("%d ", data[i][j]);
			printf("\n");
		}
		printf("\n");*/
		for(i = 0; i < SIZE; i++)
		{
			for(j = 0; j < SIZE; j++)
				if(data[i][j]) break;
			if(j < SIZE) break;
		}
		if(i >= SIZE) return;

		for(i = 0; i < SIZE; i++)
			for(j = 0; j < SIZE; j++)
				copy[i][j] = 0;
		for(i = 1; i < SIZE; i++)
			for(j = 1; j < SIZE; j++)
			{
				if(data[i][j])
					copy[i][j] = (data[i-1][j] || data[i][j-1]);
				else copy[i][j] = (data[i-1][j] && data[i][j-1]);
			}
		for(i = 0; i < SIZE; i++)
			for(j = 0; j < SIZE; j++)
				data[i][j] = copy[i][j];
		
	}
}

int main()
{
	int t, r, z = 1;
	int i, x1, x2, y1, y2, j, k;

	scanf("%d", &t);
	while(t > 0)
	{
		scanf("%d", &r);
		init();
		for(i = 0; i < r; i++)
		{
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for(j = x1; j <= x2; j++)
				for(k = y1; k <= y2; k++)
					data[k][j] = 1;
		}
		process();
		printf("Case #%d: %d\n", z++, ans);
		t--;
	}

	return 0;
}