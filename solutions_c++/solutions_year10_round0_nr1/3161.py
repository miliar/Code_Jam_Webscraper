#include<stdio.h>

int main(void)
{
	int T, N, K, mul, i, num=1;

	FILE * INPUT = fopen("A-large.in","r");
	FILE * OUTPUT = fopen("output.txt","w");

	fscanf(INPUT,"%d",&T);

	while(T--)
	{
		mul=1;
		fscanf(INPUT,"%d %d", &N, &K);

		for(i=0;i<N;i++)
			mul*=2;

		if((K+1)%mul==0)
			fprintf(OUTPUT,"Case #%d: ON\n",num++);
		else		
			fprintf(OUTPUT,"Case #%d: OFF\n",num++);
	}

	fclose(INPUT);
	fclose(OUTPUT);

	return 0;
}