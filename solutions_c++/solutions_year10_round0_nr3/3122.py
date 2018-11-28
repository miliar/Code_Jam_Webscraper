#include <fstream>
#include <iostream>

using namespace std;

void main()
{
	unsigned long long TotalEarnings = 0 ;

	FILE *pInputFileStream = NULL ;
	FILE *pOutputFileStream = NULL ;

	errno_t err;

//	string strInputFileName = "C-small-attempt.in" ;
//	string strOutputFileName = "C-small-attempt.out" ;

	string strInputFileName = "C-small-attempt0.in" ;
	string strOutputFileName = "C-small-attempt0.out" ;


	err = freopen_s(&pInputFileStream, strInputFileName.c_str(),"r",stdin) ;
	if( 0 != err )
	{
		printf("Failed to open the input file\n");
		return ;
	}

	err = freopen_s(&pOutputFileStream, strOutputFileName.c_str(),"w",stdout) ;
	if( 0 != err )
	{
		printf("Failed to open the output file\n");
		return ;
	}

	//Get the Number of Test Cases
	int  T = 0; // Test case 
	scanf_s("%d",&T);

	int MaxCapacityOfRollerCoaster = 0 ;
	int NumberOfGroups = 0 ;
	int RidesPerDay = 0 ;

	int *Groups = NULL ;
	int i = 0;

	//Iterate through T test cases
	for(i = 0; i < T; i++)
	{

		// Get the values of RidesPerDay, MaxCapacityOfRollerCoaster,NumberOfGroups);
		scanf_s("%d%d%d",&RidesPerDay,&MaxCapacityOfRollerCoaster,&NumberOfGroups);

		// Get the values of each group
		Groups = (int *) malloc(NumberOfGroups * sizeof(int ));
		for(int j = 0; j < NumberOfGroups; j++)
		{
			scanf_s("%d",&Groups[j]);
		}

		int Index = 0 ;
	
		for(int k = 0 ; k < RidesPerDay; k++ )
		{
			int AnyGroupsLeft = NumberOfGroups ;
			int FillIndex = MaxCapacityOfRollerCoaster ;

			while( FillIndex > 0 )
			{

				if(Groups[Index] <= FillIndex)
				{

					// Bingo am rich
					TotalEarnings += Groups[Index] ;

					FillIndex -= Groups[Index] ;
					Index++ ;

					if(Index == NumberOfGroups)
					{
						Index = 0 ;
					}	// if(Index == NumberOfGroups)

					AnyGroupsLeft-- ;

					if( AnyGroupsLeft <= 0 )
					{
						FillIndex = 0 ;
					}

				}	// if(Groups[Index] < FillIndex)
				else
				{
					FillIndex = 0 ;
				}

			}	// while( FillIndex > 0 )

		}

		int casenum = i + 1 ;
		printf("Case #%d: %llu\n",casenum,TotalEarnings) ;
		TotalEarnings = 0 ;

		//Free the memory so that we can reiterate through the remaining test cases
		free(Groups);
		Groups = NULL ;

	}

	//Close both the files
	fclose(pInputFileStream);
	fclose(pOutputFileStream);

}