#include <stdio.h>

void main()
{
	FILE *in,*out;
	in = fopen("Rope.in","r");
	out = fopen("Rope.out","w+");

	int T,t;
	fscanf(in,"%d\n",&T);

	for(t=0; t<T; t++)
	{
		int i,j,k;
		int N,A[1000],B[1000];

		printf("%d...",t+1);
		fscanf(in,"%d\n",&N);
		k=0;
		for(i=0;i<N;i++)
		{
			fscanf(in,"%d %d\n",&A[i],&B[i]);
			for(j=0;j<i;j++)
				if((A[i]>A[j] && B[i]<B[j]) || (A[i]<A[j] && B[i]>B[j]))
					k++;
		}

		fprintf(out,"Case #%d: %d\n",t+1,k);
		printf("Done!\n");
	}
	fclose(in);
	fclose(out);
}
