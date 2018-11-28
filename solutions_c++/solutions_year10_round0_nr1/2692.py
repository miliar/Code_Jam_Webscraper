#include <stdio.h>
#include <math.h>

void main()
{
	int times=0;
	FILE *fp_in=fopen("A-large.in","r");
	FILE *fp_out=fopen("A-large.out","w");
	int t=0,n=0,k=0,n_power;
	fscanf(fp_in,"%d",&t);
	while(times<t)
	{
		times++;
		fscanf(fp_in,"%d %d",&n,&k);
		n_power=(int)pow(2.0,n);
		k=(k+1)%n_power;
		if(k)
		{
			fprintf(fp_out,"Case #%d: OFF\n",times);
		}
		else
		{
			fprintf(fp_out,"Case #%d: ON\n",times);
		}
	}
	fclose(fp_in);
	fclose(fp_out);
}