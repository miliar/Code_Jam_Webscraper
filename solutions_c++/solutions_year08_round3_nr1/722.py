#include <stdio.h>

#include <algorithm>
using namespace std;

#define MAXK 1000

bool desc(int a, int b)
{
	return a > b;
}
int main()
{
	FILE *fin, *fout;
	int N, maxNum, keyNum, K;
	int i,j, l1, l2;
	int kick[MAXK];
	int seq[MAXK];
	long sum;
	fin = fopen("A-small.in", "r");
	fout = fopen("A-small.out", "w");
	fscanf(fin, "%d", &N); 
	for(i = 0; i < N; i++)
	{
		fscanf(fin, "%d %d %d\n", &maxNum, &keyNum, &K);


		for(j = 0; j < K; j++)
		{
			fscanf(fin, "%d", &seq[j]);
		}
		sort(&seq[0], &seq[K], desc);
		for(j = 0; j < K; j++)
			kick[j] = 0;
		j = 0;
		while(j < K)
		{	
			kick[j] = j/keyNum + 1;
			j++;
		}
		sum = 0;
		for(j = 0; j < K; j++)
			sum += kick[j] * seq[j];
		fprintf(fout, "Case #%d: %ld\n", i+1,sum);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}