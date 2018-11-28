// Practice.cpp : Defines the entry point for the console application.
//


#include <cmath>
#include <cstring>
#include "stdio.h"
//#include "string.h"
#include "stdlib.h"
//some common tasks
//char to int conversion, char to float
//string operations

int main(int argc, char* argv[])
{
	FILE *infp = NULL, *outfp = NULL;
	infp = fopen("c:\\Ashay_Backup\\input.txt","r");
	outfp = fopen("C:\\Ashay_BACKUP\\output.txt", "w+");
	if(infp==NULL || outfp==NULL)
	{
		printf("File read error\n");
		exit(1);
	}

	char buffer[50];
	char* wordptr;	
	
	fgets(buffer, 49, infp);
	long T = atol(buffer);

	long N = 0;
	long long K = 0;

	for(long i = 1; i <= T; i++)
	{
		if(fgets(buffer, 49, infp) == NULL)
			break;

		wordptr = strtok(buffer, " ");
		N = atoi(wordptr);
		wordptr = strtok(NULL, " ");
		K = atol(wordptr);

		long long twotoN = (long long)(pow((float)2, (int)N));
		if( (K+1) < twotoN )
		{
			fprintf(outfp, "Case #%d: OFF\n", i);
		}
		else if( (K+1) % twotoN )
		{
			fprintf(outfp, "Case #%d: OFF\n", i);
		}
		else
		{
			fprintf(outfp, "Case #%d: ON\n", i);
		}
	}

	fclose(infp);
	fclose(outfp);

	return 0;
}


