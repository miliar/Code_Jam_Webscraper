#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>
#include <string>
using namespace std;

int main()
{
   // cout << "Hello World!" << endl;
    
	FILE * fp = fopen( "B-large.in" , "r");
    
	char cTmp[ 1 << 15 ];
	int iNum;

	fgets( cTmp , ( 1 << 15 ) - 1 , fp );
	sscanf( cTmp , "%d" , &iNum );
    
	ofstream ofile( "Result.txt" );
	for ( int i = 0 ; i < iNum ; i ++ )
	{
		fgets( cTmp , ( 1 << 15 ) - 1 , fp );
		int N , K , B, T;
		sscanf( cTmp , "%d %d %d %d", &N, &K, &B, &T);
   
		int * LocationArray = (int *) malloc( sizeof(int) * N );
		int * SpeedArray = (int *)malloc( sizeof(int) * N );

		fgets( cTmp , ( 1<< 15) - 1 , fp );
		int iTmp = 0 ;
		int iIndex =0;
        for ( int j = 0 ; j < strlen(cTmp) - 1 ; j ++ )
        {
			
            if ( cTmp[j] == ' ' )
            {
                LocationArray[iIndex] = iTmp;
				iIndex++;
				iTmp = 0;
            }
			else
			{
                iTmp *= 10;
				iTmp += cTmp[j] - '0';
				//cout << "Tmp:" << iTmp << endl;
			
			}
        }
        LocationArray[N-1] = iTmp;

		fgets( cTmp , ( 1<< 15) - 1 , fp );
		iTmp = 0 ;
		iIndex =0;
		for ( int j = 0 ; j < strlen(cTmp) - 1 ; j ++ )
		{

			if ( cTmp[j] == ' ' )
			{
				SpeedArray[iIndex] = iTmp;
				iIndex++;
				iTmp = 0;
			}
			else
			{
				iTmp *= 10;
				iTmp += cTmp[j] - '0';
				//cout << "Tmp:" << iTmp << endl;

			}
		}
		SpeedArray[N-1] = iTmp;



		int iNumNot = 0 ;
        int iNumExchange = 0 ;
        int iNumCan = 0;
		
		/*cout << B << endl;
		cout << T << endl;
		cout << K << endl;*/
		for ( int j = N - 1 ; j >= 0 ; j -- )
		{
             if ( LocationArray[j] + SpeedArray[j] * T >= B )
             {

				 iNumExchange += iNumNot;
               
				 if ( --K<=0 )
				 {
					 
					 break;
					
				 }
             }
			 else
			 {
                 iNumNot ++;
			 }
		}
        
		ofile << "Case #";
		char cNum[10];
		itoa( i + 1 , cNum , 10 );
		ofile << string(cNum) ;
		ofile << ": " ;
        if (K<=0)
        {
			itoa( iNumExchange , cNum , 10 );
			ofile << string(cNum) << endl;
        }
		else
		{
			ofile << "IMPOSSIBLE" << endl;
		}

		//cout << N << " " << K << " " << B << " " << T << endl;
	}

	fclose(fp);

}