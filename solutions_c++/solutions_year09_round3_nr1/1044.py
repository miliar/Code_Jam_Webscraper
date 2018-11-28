#include<stdio.h>
#include<string.h>
#include<memory.h>
#include<conio.h>
#include<math.h>




void openfiles( FILE **fin, FILE **fout )
{
	char filename[32] = "";
	char infile[32];
	char outfile[32];

	printf( "filename: " );
	scanf_s( "%s", filename, 32 );
	strcpy_s( infile, 32, filename );
	strcpy_s( outfile, 32, filename );
	
	strcat_s( infile, 32, ".in" ); 
	strcat_s( outfile, 32, ".out" );
	
	fopen_s( fin, infile, "r" );
	fopen_s( fout, outfile, "w" );
}


unsigned long solve( const char *num )
{
	int numbers[256];
	int base;
	int n;
	const char *c;
	int cnt;
	unsigned long res;
	int i, p;

	memset( numbers, -1, sizeof(int)*256 );
	base = 0;
	cnt = 0;
	n = 0;

	c = num;
	while( *c != '\0' )
	{
		if( numbers[*c] == -1 )
		{
			if( n == 0 )
				numbers[*c] = 1;
			else if( n == 1 )
				numbers[*c] = 0;
			else
				numbers[*c] = n;

			n++;
			base++;
		}

		cnt++;
		c++;
	}
	if( base == 1 ) base++;


	//c = num;
	//printf("%s ", num );
	//while( *c != '\0' )
	//{
	//	printf("%d", numbers[*c]);
	//	c++;
	//}
	//printf(" base :%d\n", base);
	//getch();


	c = num;
	res = 0;
	while( *c != '\0' )
	{
		p = 1;
		for( i=0; i<cnt-1; i++ ) p *= base;

		//p = pow( (float)base, cnt-1 );
		res += numbers[*c] * p;
		//res += numbers[*c] * pow( (float)base, cnt-1 );
		cnt--;
		c++;
	}

	return res;
}


int main()
{
	FILE *fin;
	FILE *fout;
	char num[255];
	unsigned long res;
	int T;
	int i;

	openfiles( &fin, &fout );

	fscanf( fin, "%d\n", &T );
	for( i=0; i<T; i++ )
	{
		fgets( num, 255, fin );
		num[ strlen(num)-1 ] = '\0';
		res = solve( num );

		printf( "Case #%d: %ld\n\n", i+1, res );
		fprintf( fout, "Case #%d: %ld\n", i+1, res );
	}

	fclose( fin );
	fclose( fout );

	getch();
	return 0;
}