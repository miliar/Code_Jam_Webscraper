#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXCHAR 8192

FILE * Fopen(const char* filename, const char* mode)
{
	FILE * fp = fopen(filename, mode);
	if(!fp)
	{
		perror("Open file failed!");
		exit(-1);
	}
	return fp;
}

char * Fgets(char* buf, int count, FILE * fp)
{
	if( !fgets(buf, count, fp) )
	{
		perror("Read file failed!");
		return NULL;
	}
	return buf;
}


int main(int argc, char ** argv)
{
	char infile[100];
	char outfile[100];
	printf("input file: ");
	scanf("%s", infile);
	printf("output file: ");
	scanf("%s", outfile);

	FILE * infp = Fopen(infile, "r");
	FILE * outfp = Fopen(outfile, "w");

	char buf[MAXCHAR];

	// T
	Fgets(buf, sizeof(buf), infp);
	int T = atoi(buf);

	for(int t = 0; t < T; t++)
	{
		unsigned int sum, min, xorsum;

		// N
		Fgets(buf, sizeof(buf), infp);
		char * strN = strtok(buf, " ");
		int N = atoi(strN);

		// begin
		Fgets(buf, sizeof(buf), infp);
		char * strValue = strtok(buf, " ");
		unsigned int value = (unsigned int)atoi(strValue);
		sum = value;
		min = value;
		xorsum = value;

		for( int n = 1; n < N; n++ )
		{
			strValue = strtok(NULL, " ");
			value = (unsigned int)atoi(strValue);

			sum += value;
			if(min > value)
				min = value;
			xorsum ^= value;
		}
		
		// output
		if(xorsum != 0)
		{
			fprintf( outfp, "Case #%d: NO\n", t+1 );
		}
		else
		{
			fprintf( outfp, "Case #%d: %d\n", t+1, sum - min );
		}
	}

	fclose(infp);
	fclose(outfp);

	return 0;
}