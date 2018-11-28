#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>


char words[6000][20];
int wordcount;

char tokens[20][1000]; /* 255? */
int tokencount;



int iswordindictionary( char *word )
{
	return 1;
}


void generatetokens( char *str )
{
	char t[1000];
	int ind;
	int ps;
	int len;
	int i;

	ind = 0;
	len = strlen( str );

	tokencount = 0;
	ps = -1;
	for( i=0; i<len; i++ )
	{
		if( str[i] != '(' && str[i] != ')' )
		{
			tokens[tokencount][0] = str[i];
			tokens[tokencount][1] = '\0';
			tokencount++;
		}
		
		if( str[i] == '(' )
		{
			/* get chars until ) found */
			ind = 0;
			i++;
			while( str[i] != ')' )
			{
				tokens[tokencount][ind++] = str[i];
				i++;
			}
			tokens[tokencount][ind] = '\0';
			tokencount++;
		}
	}
}


int possiblewords( int k, int start, int end )
{
	static char word[20];
	static char ind = 0;
	int i;
	int j;
	int js;
	int je;
	int res = 0;
	int found;

	int ss,se;

	int len;
	len = strlen( tokens[k] );


	if( k == tokencount )
	{
		word[ind] = '\0';
		//printf("%s\n",word);
		return 1;
	}

	ss = 0;
	se = wordcount;
	for( i=0; i<len; i++ )
	{
		found = 0;
		word[ind] = tokens[k][i];
		
		for( j=start; j<end; j++ )
		{
			if( found && words[j][ind] != word[ind] )
				break;
			else if( words[j][ind] == word[ind] )
			{
				if( !found )
				{
					js = je = j;
				}

				je++;
				found = 1;
			}
		}
		
		if( found )
		{
			ind++;
			res += possiblewords( k+1, js, je );
			ind--;
		}
	}

	return res;
}


int compare( const void * a, const void * b)
{
	return strcmp( (char*)a, (char*)b );
}

int main( void )
{
	FILE *fin;
	FILE *fout;
	int L, D, N;
	int i;
	int res;
	char word[1000];


	fin = fopen( "A-large.in", "r" );
	//fin = fopen( "A-small test.in", "r" );
	fout = fopen( "A-large.out", "w" );


	fscanf( fin, "%d %d %d", &L, &D, &N );


	/* words */
	wordcount = 0;
	for( i=0; i<D; i++ )
	{
		fscanf( fin, "%s", word );
		strcpy( words[wordcount++], word );
	}


	/* sort words */
	qsort( words, wordcount, 20, compare );
	//for( i=0;i<D;i++)
	//	printf("%s\n", words[i]);
	//printf("\n");


	/* test cases */
	for( i=0; i<N; i++ )
	{
		fscanf( fin, "%s", word );

		generatetokens( word );
		res = possiblewords( 0, 0, wordcount );
		//printf( "Case #%d: %d\n\n", i+1, res );
		fprintf( fout, "Case #%d: %d\n", i+1, res );
	}


	fclose( fin );
	fclose( fout );


	//getch();
	return 0;
}