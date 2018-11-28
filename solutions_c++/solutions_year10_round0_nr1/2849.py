//		printf( "iSocketsCount:%li , iSnapsCount:%li \n", iSocketsCount, iSnapsCount  );
//		printf( "( (int)pow( 2 , iSocketsCount ) ) = %i\n", ( (int)pow( 2 , iSocketsCount ) ) );

#include "stdio.h"
#include "stdlib.h"
#include "math.h"


int main()
{


	
	long int iSnapsCount   = 0; //K
	long int iSocketsCount = 0; //N
        int 	  iInputLinesCount = 0;
	
	FILE* pInputFile = fopen( "./A-large.in" , "r" );
       	//FILE* pInputFile = fopen( "./input.txt" , "r" );
	FILE* pOutputFile = fopen( "./output.txt", "w");
	
	fscanf( pInputFile , "%i\n", &iInputLinesCount );
	
	for( int iLine = 1 ; iLine <= iInputLinesCount ; iLine++)
	{
		fscanf( pInputFile , "%li %li\n", &iSocketsCount, &iSnapsCount );

		if( 0 == ( iSnapsCount + 1 )%( (int)pow( 2 , iSocketsCount ) ) )
		{
			fprintf( pOutputFile , "Case #%i: ON\n", iLine );   //Case #1:ON
			printf( "State Number is :%i, state is: %s\n", iLine,"ON" );
		}
		else
		{
			fprintf( pOutputFile , "Case #%i: OFF\n",iLine );
			printf( "State Number is :%i, state is: %s\n", iLine,"OFF" );
		}
		
	}
	
	fclose( pInputFile );
	fclose( pOutputFile );

	return 0;
	
}

