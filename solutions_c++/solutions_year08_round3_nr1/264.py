#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>


int ls[1001];

long long int ans, qq,m;

int comp (const void * a, const void * b) 
{
	int c=*((int *)a);
	int d=*((int *)b);
	
	return d-c;
}

int main(int argc, char **argv)
{
	if (argc<=1) {printf("test\n\n"); return 0;}

	FILE *input=fopen(argv[1], "rt");

	FILE *output=fopen("output", "wt");

	int N=0;

	int i, j, k;


	int P, K, L;

	fscanf(input, "%d\n", &N);

	
	for (i=0;i<N; i++)
	{
		fscanf (input, "%d %d %d\n", &P, &K, &L);
	
		ans=0;
		for (j=0;j<L; j++)
		{
			fscanf (input, "%d", ls+j);
			if (j<L-1) fgetc(input); else fscanf(input, "\n");
		}

		qsort ((void *)ls, L, 4, comp);
		//for (j=0; j<L; j++)
		//	printf("%d\n", ls[j]);

		m=0;
		for (j=0;j<L;j++)
		{
			if (j%K==0) m++;
			qq=ls[j];

			qq*=m;
			ans+=qq;
		}
		fprintf(output, "Case #%d: %d\n", i+1, ans);
		if (i==27) std::cout << ans;
	}

	fclose(output);
	fclose(input);

}

