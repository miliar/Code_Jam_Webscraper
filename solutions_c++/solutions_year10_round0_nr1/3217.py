#include <fstream>
#include <iostream>
#include <math.h>

using namespace std;

void main()
{
	unsigned long long TotalEarnings = 0 ;

	FILE *pInputFileStream = NULL ;
	FILE *pOutputFileStream = NULL ;

	errno_t err;

//	string strInputFileName = "A-small-attempt.in" ;
//	string strOutputFileName = "A-small-attempt.out" ;

//	string strInputFileName = "A-small-attempt0.in" ;
//	string strOutputFileName = "A-small-attempt0.out" ;

	string strInputFileName = "A-large.in" ;
	string strOutputFileName = "A-large.out" ;


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

	int nSnappers = 0 ;
	int kTimes = 0 ;

	int ON = 0 ;
	int tempON ;
	//Iterate through T test cases
	for(int i = 0; i < T; i++)
	{
		bool bResult = false;
		
		// Get the values of RidesPerDay, MaxCapacityOfRollerCoaster,NumberOfGroups);
		scanf_s("%d%d",&nSnappers,&kTimes);

		ON = (int) pow(2.0,(double)nSnappers) ;
		tempON = ON - 1 ;

		if( tempON == kTimes % ON )
			bResult = true ;
	
		int casenum = i + 1 ;
		if(bResult)
		{
			printf("Case #%d: ON\n",casenum) ;
		}
		else
		{
			printf("Case #%d: OFF\n",casenum) ;
		}

		fflush(pOutputFileStream);
	}

	//Close both the files
	fclose(pInputFileStream);
	fclose(pOutputFileStream);

}