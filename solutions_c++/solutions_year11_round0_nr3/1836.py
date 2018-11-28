#include <stdio.h>
#include<stdlib.h>
#include<time.h>

int T,N;
int c[2000];

int main()
{
	FILE *fin=fopen("input.txt","r");
	FILE *fout = fopen("output.txt","w");

	fscanf(fin, "%d", &T);
	for(int aaa=1; aaa<=T; aaa++)
	{
		fscanf(fin, "%d", &N);
		int result = 0;
		int sum = 0;
		int min = 2147483647;
		for(int i = 0; i < N; i++)
		{
			int temp;
			fscanf(fin,"%d",&temp);
			result ^= temp;
			if(min > temp) min = temp;
			sum+=temp;
		}
		if(result) fprintf(fout,"Case #%d: NO\n", aaa);
		else fprintf(fout,"Case #%d: %d\n", aaa, sum-min);
	}

	return 0;
}
