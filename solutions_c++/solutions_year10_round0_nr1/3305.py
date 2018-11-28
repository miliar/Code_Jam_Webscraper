#include <stdio.h>

typedef unsigned int uint;

static const uint ones = (uint)(int)-1;
static const uint ones_n = sizeof(ones)*8;

int main()
{
	FILE* fi = fopen("data.in","r");
	FILE* fo = fopen("data.out","wb");
	if (fi && fo)
	{
		int n = 0;
		fscanf(fi,"%i\n",&n);
		uint N=0, K=0;
		char* on_s = "";
		uint mask;
		for (int i=1; i<=n; i++)
		{
			fscanf(fi,"%u %u\n", &N, &K);
			mask = ones >> (ones_n-N);
			on_s = (K&mask) == mask ? "ON" : "OFF";
			fprintf(fo,"Case #%i: %s\n", i, on_s);
		}
	}
	fclose(fo);
	fclose(fi);
	return 0;
}
