#include<stdio.h>
#include<conio.h>
#define INPUTFILE "C-large.in"
#define OUTPUTFILE "C-large.out"

int t=0;
int n;
FILE *in;
FILE *out;


void main(void)
{
	clrscr();

	in = fopen(INPUTFILE,"r");
	out = fopen(OUTPUTFILE,"w");

	fscanf(in, "%d", &t);
	for(int ti=0; ti<t; ++ti)
	{
		long falsesum = 0;
		long sum = 0;
		long least = -1;
		fscanf(in, "%d", &n);

		for(int ni=0; ni<n; ni++)
		{
			long val = 0;
			fscanf(in, "%ld", &val);
			falsesum ^= val;
			sum += val;
			if(least > val || least == -1)
				least = val;
		}

		fprintf(out, "Case #%d: ", ti+1);
		if(falsesum == 0)
		{
			fprintf(out, "%ld\n", sum - least);
		}
		else
		{
			fprintf(out, "NO\n");
		}
	}
	fclose(in);
	fclose(out);
	printf("Done.");
	getch();
}