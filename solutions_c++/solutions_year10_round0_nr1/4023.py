#include "stdio.h"
#include "stdlib.h"

typedef unsigned int DWORD;

int main()
{
	FILE *fi, *fo;
	fi = fopen("A-small.in", "rt");
	fo = fopen("output.out", "wt");
	DWORD t,n,k;
	fscanf(fi, "%d", &t);
	for (int i = 0 ; i < t ; ++i)
	{
		fscanf(fi, "%d %d", &n, &k);
		DWORD n2 = 1;
		while (n>0)
		{
			n2*=2;
			--n;
		}
		bool bOn = false;

		fprintf(fo, "Case #%d: ", i);

		if ( (k%n2) == (n2-1) )
		{
			fprintf(fo, "ON");
		}
		else
		{
			fprintf(fo, "OFF");
		}
		fprintf(fo, "\n");
	}
	fclose(fo);
	fclose(fi);
	return 0;
}
