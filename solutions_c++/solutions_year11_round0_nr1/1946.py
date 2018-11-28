#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXCHAR 512

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
	Fgets(buf, sizeof(buf), infp);
	int T = atoi(buf);

	for(int t = 0; t < T; t++)
	{
		int osrc, odes, bsrc, bdes;
		osrc = 1;
		bsrc = 1;

		int otime = 0;
		int btime = 0;

		Fgets(buf, sizeof(buf), infp);

		// N
		char * strN = strtok(buf, " ");
		int N = atoi(strN);

		// begin

		int pos = 0;
		for( int n = 0; n < N; n++ )
		{
			char * color = strtok(NULL, " ");
			char * des = strtok(NULL, " ");

			if( color[0] == 'O' )
			{
				odes = atoi(des);
				int movetime = odes - osrc;
				if(movetime < 0)
					movetime = -movetime;
				otime += movetime;
				if(otime < btime)
					otime = btime;
				otime++;
				osrc = odes;
			}
			else if( color[0] == 'B' )
			{
				bdes = atoi(des);
				int movetime = bdes - bsrc;
				if(movetime < 0)
					movetime = -movetime;
				btime += movetime;
				if(btime < otime)
					btime = otime;
				btime++;
				bsrc = bdes;
			}
			else
			{
				printf("error!\n");
				return -1;
			}
		}
		int totaltime = otime;
		if( totaltime < btime )
			totaltime = btime;

		// output
		fprintf( outfp, "Case #%d: %d\n", t+1, totaltime );
	}

	fclose(infp);
	fclose(outfp);

	return 0;
}