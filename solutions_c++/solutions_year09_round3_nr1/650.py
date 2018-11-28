#define CAPP1

#ifdef CAPP1

#include<stdio.h>
#include<string.h>
#include<memory.h>
#include <stdlib.h>
#include <math.h>

#define maxbfr 100

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	if ( !fp )
		return 0;
	int N = 0;
	fscanf(fp, "%d\n", &N);
	for( int i = 1 ; i <= N ; i++ )
	{
		char bfr[maxbfr];
		memset(bfr,0,maxbfr);
		int val[256];
		memset(val,-1,sizeof(int)*256);
		fgets(bfr,maxbfr,fp);
		int end = strlen( bfr ) - 1;
		while( bfr[end] < '0' || bfr[end] > 'z' )
			end--;
		long int ans = 0;
		if( !end )
		{
			ans = 1;
		}
		else
		{
			if( end == 1 )
			{
				if( bfr[ 0 ] != bfr[ 1 ] )
					ans = 2;
				else
					ans = 3;
			}
			else
			{
				val[bfr[0]]=1;
				char *tmp = bfr;
				while( *tmp >= '0' && *tmp <= 'z' && *tmp == *bfr )
					tmp = tmp + 1;
				if( *tmp >= '0' && *tmp <= 'z' )
					val[*tmp]=0;
				int base = 2;
				for( int j = 1 ; j <= end ; j++ )
				{
					if( val[bfr[j]] < 0 )
					{
						val[bfr[j]] = base;
						base++;
					}
				}
				long int bb = 1;
				for( int j = end ; j > -1 ; j-- )
				{
					ans = ans + bb * val[bfr[j]];
					bb = bb * base;
				}
			}
		}
		fprintf(ofp, "Case #%ld: %d\n" , i , ans );
	}
	fclose(ofp);
	fclose(fp);
	return 0;
}
#endif