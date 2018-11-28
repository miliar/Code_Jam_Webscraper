#include<stdio.h>
#include<math.h>
int main()
{
	int tc,n,i=1;
	long on,k;
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
		fscanf(in,"%d %d\n",&n,&k);
		on = pow(2,n)-1;
		fprintf(out,"Case #%d: ",i);
		if(on == k || (k-on)%(on+1) == 0)
			fprintf(out,"ON\n");
		else
			fprintf(out,"OFF\n");
		i++;
	}

	fclose(in);
	fclose(out);

	return 0;
}