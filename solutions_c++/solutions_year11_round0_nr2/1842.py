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

int charToIndex(char c)
{
	int index;
	switch(c)
	{
	case('Q'):
		index = 8;
		break;
	case('W'):
		index = 7;
		break;
	case('E'):
		index = 6;
		break;
	case('R'):
		index = 5;
		break;
	case('A'):
		index = 4;
		break;
	case('S'):
		index = 3;
		break;
	case('D'):
		index = 2;
		break;
	case('F'):
		index = 1;
		break;
	default:
		index = 0;
		break;
	}
	return index;
}

int pairToIndex(char a, char b)
{
	int ai = charToIndex(a);
	int bi = charToIndex(b);
	
	if( ai == 0 || bi == 0 )
		return -1;

	int temp = ai;
	if(temp < bi)
	{
		ai = bi;
		bi = temp;
	}
	// assure ai > bi
	int index = ai * (ai - 1) / 2 + bi - 1;
	return index;
}

void insCpair(char * pair, int * carray)
{
	char a = pair[0];
	char b = pair[1];
	char c = pair[2];

	int index = pairToIndex(a, b);
	carray[index] = (int)c;
}

void insDpair(char * pair, int * darray)
{
	char a = pair[0];
	char b = pair[1];

	int index = pairToIndex(a, b);
	darray[index] = -1;
}

int getPair(char a, char b, int * cdarray)
{
	int index = pairToIndex(a, b);

	if(index == -1)
		return 0;
	else
		return cdarray[index];
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
		int carray[36] = {0};
		int darray[36] = {0};

		Fgets(buf, sizeof(buf), infp);
		// C
		char * strC = strtok(buf, " ");
		int C = atoi(strC);
		for(int c = 0; c < C; c++ )
		{
			char * cpair = strtok(NULL, " ");
			insCpair(cpair, carray);
		}
		// D
		char * strD = strtok(NULL, " ");
		int D = atoi(strD);
		for(int d = 0; d < D; d++)
		{
			char * dpair = strtok(NULL, " ");
			insDpair(dpair, darray);
		}
		// N
		char * strN = strtok(NULL, " ");
		int N = atoi(strN);
		char * list = strtok(NULL, " ");

		// transform
		char listFinal[100] = { '\0' };
		int pos = 0;
		for( int n = 0; n < N; n++ )
		{
			if(pos == 0)
			{
				listFinal[pos] = list[n];
				pos++;
			}
			else
			{
				int cresult = getPair(listFinal[pos-1], list[n], carray);
				if(cresult != 0)
				{
					listFinal[pos-1] = (char)cresult;
				}
				else
				{
					int dresult;
					for( int i = 0; i < pos; i++ )
					{
						dresult = getPair(listFinal[i], list[n], darray);
						if( dresult == -1 )
						{
							pos = 0;
							break;
						}
					}
					if( dresult != -1 )
					{
						listFinal[pos] = list[n];
						pos++;
					}
				}

			}
		}

		// output
		if(pos > 0)
		{
			fprintf( outfp, "Case #%d: [", t+1 );
			for( int i = 0; i < pos - 1; i++ )
			{
				fprintf( outfp, "%c, ", listFinal[i] );
			}
			fprintf( outfp, "%c]\n", listFinal[pos-1] );
		}
		else
			fprintf( outfp, "Case #%d: []\n", t+1 );
	}
	return 0;
}