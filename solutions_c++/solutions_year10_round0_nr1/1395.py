#include <stdio.h>
#include <math.h>

int main(int argc, char **argv)
{
	if(argc!=2)
	{
		printf("Usage: <prog> <input_file>\n");
		return 1;
	}

	FILE *fin = fopen("a.in","r");
	FILE *fout = fopen("a.out","w");
	
	unsigned long long k;
	int n,cnt;
	fscanf(fin,"%d",&cnt);
	for(int i=0;i<cnt;i++)
	{
		fscanf(fin,"%d %d",&n,&k);
		unsigned long long d = pow((double)2,n);
		if((k+1)%d==0)
			fprintf(fout,"Case #%d: ON\n",i+1);
		else
			fprintf(fout,"Case #%d: OFF\n",i+1);
	}
	fclose(fin);
	fclose(fout);
}
