#include "stdio.h"
void main()
{
	FILE *fp1=fopen("g:\\input.txt","r");
	FILE *fp2=fopen("g:\\output.txt","w");
	long i,N,K,T,R,j;
	fscanf(fp1,"%ld",&T);
	for(i=1;i<=T;++i)
	{
		long n=1;
		fscanf(fp1,"%ld",&N);
		fscanf(fp1,"%ld",&K);
		for(j=1;j<N;++j)
		{
			n=(n<<1)|1;
		}
		R=K&n;
		//printf("%x %x %x %x\n",N,K,n,R);
		if(R==n)
			fprintf(fp2,"Case #%d: ON\n",i);
		else
			fprintf(fp2,"Case #%d: OFF\n",i);
	}
	fclose(fp1);
	fclose(fp2);
}