#include<stdio.h>
#define SIZE 1000
int main()
{
	int tc,i=1;
	long r,k,n,g[SIZE],sum,x,y,j;
	double euros;
	FILE *in, *out;
	char filename[20];
	printf("Input file:");
	scanf("%s",filename);
	in=fopen(filename,"r");
	fscanf(in,"%d\n",&tc);
	printf("Output file:");
	scanf("%s",filename);
	out=fopen(filename,"w");

	while(i<=tc)
	{
		fscanf(in,"%ld %ld %ld\n",&r,&k,&n);
		for(j=0;j<n;j++)
			fscanf(in,"%ld",&g[j]);
		fscanf(in,"\n");

		x=0;
		euros=0;
		while(r--)
		{
			sum=0;
			y=x;
			do
			{
				if((sum+g[x])>k)
					break;
				sum+=g[x];
				x=(x+1)%n;
			}while(y!=x);
			euros+=sum;
		}

		fprintf(out,"Case #%d: %.0Lf\n",i,euros);
		i++;
	}

	fclose(in);
	fclose(out);

	return 0;
}