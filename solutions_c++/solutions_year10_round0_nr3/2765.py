#include "stdio.h"
#include "stdlib.h"
#include <queue>


int main()
{
	//R K N 
	int iTrialsCount ; //T
	long int liRounds = 0;       //R : Number of Rounds the shuttle can make.
	long int liSeats  = 0;     //K : Number of seats.
	int 	 iGroupsCount = 0;  //N : Number of Groups.
	long int liGroupSize   = 0;
	long int liRevenue     = 0;

	
	FILE* pInputFile = fopen( "./C-small-attempt0.in" , "r");
	FILE* pOutputFile= fopen( "./output.txt", "w");

	fscanf( pInputFile, "%i\n", &iTrialsCount );
	
	for( int iTrial = 1; iTrial <= iTrialsCount ; iTrial++ )
	{
		std::queue< long int > qiGroups;
		fscanf( pInputFile , "%li %li %i\n", &liRounds , &liSeats, &iGroupsCount );

		//Fill The Group Queue
		for( int iGroupNumber = 0; iGroupNumber < iGroupsCount ; iGroupNumber++ )
		{
			liGroupSize = 0;
			if( iGroupNumber < iGroupsCount - 1 )
			{
 				fscanf( pInputFile , "%li ", &liGroupSize );
			}
			else
			{
				fscanf( pInputFile , "%li", &liGroupSize );
			}			
//			printf("Pushing Element: %li , Trial Number: %i\n", iGroupSize ,iTrial );
			qiGroups.push( liGroupSize );			
		}
		printf( "Trial Number:%i, rounds=%li, seats=%li, Number Of Groups=%i\n", iTrial, liRounds ,liSeats , iGroupsCount );
		
		//Logic.
		for( long int iRound = 0 ; iRound < liRounds ; iRound++ )
		{
			//Choose Groups.
			long int liNumberOfPeople = 0 ;
			long int iNumberOfLoops  = 0 ;
			while( ( iNumberOfLoops < qiGroups.size() ) && 
			     ( ( liNumberOfPeople + qiGroups.front() ) <= liSeats ) )
			{
				liNumberOfPeople += qiGroups.front();
				qiGroups.push( qiGroups.front() );
				qiGroups.pop();
				iNumberOfLoops++ ;
			}
			printf( "Trial Number: %i , Round Number:%li Number of people:%li \n", iTrial , iRound , liNumberOfPeople );
			liRevenue += liNumberOfPeople;			
		}	

		fprintf( pOutputFile , "Case #%i: %li\n",iTrial , liRevenue );
		liRevenue = 0;		
	}
	

}

