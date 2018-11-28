#include<stdio.h>
#include<math.h>
void main(int argc, char** argv)
{
	if(argc != 2)
	{
		printf("usage: ThemePark <input file name>");
		return;
	}

	FILE* finput = fopen(argv[1], "r");
	if(0 == finput)
	{
		printf("input file %s not found", argv[1]);
		return;
	}

	int num_cases;
	int ret = fscanf(finput, "%d", &num_cases);
	if(ret != 1)
	{
		printf("wrong format found in input file %s", argv[1]);
		return;
	}

	int R, k, N;
	for(int i=1; i<=num_cases; i++)
	{
		ret = fscanf(finput, "%d %d %d", &R, &k, &N);
		if(ret != 3)
		{
			printf("wrong format found in input file %s", argv[1]);
			return;
		}

		int* g = new int[N];
		for(int j=0; j<N; j++)
		{
			ret = fscanf(finput, "%d", &(g[j]));
		}
		if(ret != 1)
		{
			printf("wrong format found in input file %s", argv[1]);
			return;
		}

		int queue_front = 0;
		int total_income = 0;
		for(int j=0; j<R; j++)
		{
			int num_occupied = 0;
			int num_groups = 0;
			while(true)
			{
				if(g[queue_front] + num_occupied <= k)
				{
					num_occupied += g[queue_front];
					queue_front = (queue_front+1) % N;
					num_groups ++;
					if(num_groups == N)
					{
						break;
					}
				}
				else
				{
					break;
				}
			}
			total_income += num_occupied;
		}

		printf("Case #%d: %d\n", i, total_income);
		delete [] g;
	}
}