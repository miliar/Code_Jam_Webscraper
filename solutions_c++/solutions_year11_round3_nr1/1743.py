#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXCHAR 128

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


		// R
		Fgets(buf, sizeof(buf), infp);
		char * strR = strtok(buf, " ");
		int R = atoi(strR);

		// C
		char * strC = strtok(NULL, " ");
		int C = atoi(strC);

		// begin
		char ** picture = new char*[R];
		for(int i = 0; i < R; i++)
		{
			// every column
			picture[i] = new char[C+1];
			Fgets(buf, sizeof(buf), infp);
			for(int j = 0; j < C; j++)
			{
					picture[i][j] = buf[j];
			}
			picture[i][C] = '\0';
		}

		bool result = true;
		for(int i = 0; i < R; i++)
		{
			if(!result)
				break;
			for(int j = 0; j < C; j++)
			{
				if(picture[i][j] == '#')
				{
					if(i == R - 1 || j == C - 1)
					{
						result = false;
						break;
					}
					else if(picture[i][j+1] != '#' || picture[i+1][j] != '#' || picture[i+1][j+1] != '#')
					{
						result = false;
						break;
					}
					else
					{
						picture[i][j] = '/';
						picture[i][j+1] = '\\';
						picture[i+1][j] = '\\';
						picture[i+1][j+1] = '/';
					}
				}
			}
		}
		
		fprintf( outfp, "Case #%d:\n", t+1 );
		if(!result)
		{
			fprintf( outfp, "Impossible\n" );
		}
		else
		{
			for(int i = 0; i < R; i++)
			{
				fprintf( outfp, "%s\n", picture[i] );
			}
		}

	}

	fclose(infp);
	fclose(outfp);

	return 0;
}