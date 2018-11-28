#include<iostream>
using namespace std;
#include<stdio.h>
#include<cstdio>


int candy[1001];

int main()
{

	FILE *fp = fopen("C-large.in","r");
	FILE *fpw = fopen("C-large.out","w");
	int T,N;
	fscanf(fp, "%d", &T);
	for(int i = 1; i <= T; i ++)
	{
		fscanf(fp, "%d", &N);
		int min = 1000001;
		int min_index;
		int sum = 0;
		for(int j = 0; j < N; j ++)
		{
			fscanf(fp, "%d", &candy[j]);
			sum += candy[j];
			if(candy[j] <= min)
			{
				min = candy[j];
				min_index = j;
			}
		}

		int f_sum = 0;

		for(int p = 0; p < N; p ++)
		{
			f_sum = candy[p] ^ f_sum;
		}

		if(f_sum == 0)
		{
			fprintf(fpw,"Case #%d: %d\n", i, sum - min);
		}
		else
		{
			fprintf(fpw,"Case #%d: NO\n", i);
		}

	}



	return 0;
}

