#include <stdio.h>
#include <string.h>

char map[128];

char in[4][500] = {
	"ejp mysljylc kd kxveddknmc re jsicpdrysi" ,
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" ,
	"de kr kd eoya kw aej tysr re ujdr lkgc jv" ,
	"y qee"
};

char out[4][500] = {
	"our language is impossible to understand" ,
	"there are twenty six factorial possibilities" ,
	"so it is okay if you want to just give up" ,
	"a zoo"
};

char input[1024];
char output[1024];

void convert( const char * inp , char *outp )
{
	while( *inp )
	{
		*outp = map[ *inp ];

		++inp;
		++outp;
	}
}

int main()
{
	FILE *inF = fopen("C:/Users/Serdar/Desktop/A.in" , "r");
	FILE *outF = fopen("C:/Users/Serdar/Desktop/A.out" , "w");

	for( int i = 0 ; i < 4 ; i++ )
	{
		for( int j = 0 ; in[i][j] ; j++ )
		{
			map[ in[i][j] ] = out[i][j];
		}
	}
	map[ 'z' ] = 'q';

	for( int i = 'a' ; i <= 'z' ; i++ )
	{
		printf("Map[ %c ] = %c\n" , i , map[i]);
	}

	int N;
	fscanf( inF , "%d " , &N );

	for( int i = 0 ; i < N ; i++ )
	{
		fgets( input , 1024 , inF );
		convert( input , output );
		fprintf( outF , "Case #%d: %s\n",i+1,output);
	}

	strcpy( input , in[0] );
	convert( input , output );
	printf("%s\n",output);

	return 0;
}
