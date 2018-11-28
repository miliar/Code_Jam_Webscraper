#include<stdio.h>
#include<math.h>
void main(int argc, char** argv)
{
	if(argc != 2)
	{
		printf("usage: SnapperChain <input file name>");
		return;
	}

	FILE* finput = fopen(argv[1], "r");
	if(0 == finput)
	{
		printf("input file %s not found", argv[1]);
		return;
	}

	int total_lines;
	int ret = fscanf(finput, "%d", &total_lines);
	if(ret != 1)
	{
		printf("wrong format found in input file %s", argv[1]);
		return;
	}

	int N, K;
	for(int i=1; i<=total_lines; i++)
	{
		ret = fscanf(finput, "%d %d", &N, &K);
		if(ret != 2)
		{
			printf("wrong format found in input file %s", argv[1]);
			return;
		}

		int cycle_length = (int)(pow(2.0, N));
		if(0 == ((K+1) % cycle_length))
		{
			printf("Case #%d: ON\n", i);
		}
		else
		{
			printf("Case #%d: OFF\n", i);
		}
	}
}