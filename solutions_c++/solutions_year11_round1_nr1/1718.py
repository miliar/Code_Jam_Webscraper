// ProgramA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

#define fabc(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fa0c(a,b) fabc( a, 0, ( b ) )
#define for_i(a) fa0c( i, ( a ) )
#define for_j(a) fa0c( j, ( a ) )
#define for_k(a) fa0c( k, ( a ) )

int _tmain(int argc, _TCHAR* argv[])
{
	int i,j,k;
	fstream f_input, f_output,f_output1;
	f_input.open(argv[1],fstream::in);
	f_output.open("ProgramAOut.txt",fstream::out);
	f_output1.open("ProgramAOutRead.txt",fstream::out);


	//read test cases
	int T = 0;
	f_input >> T;
	for_i(T)
	{
		bool Possible = false;
		bool t1 = false;
		bool t2 = false;
		int MaxD = 0;
		int PercentD = 0;
		int PercentG = 0;
		f_input >> MaxD;
		f_input >> PercentD;
		f_input >> PercentG;

		fabc(j,1,MaxD+1) //j - game played today
		{
			float fDWon = ((float)PercentD/100)*j;
			int iDwon = (int)fDWon;

			if((float)iDwon == fDWon) //whole number of games;
			{
				t1 = true;
				t2= true;
					if(PercentD > 0 && PercentG == 0)
					{
						Possible = false;
						
					}
					else if(PercentD == 100 && PercentG <=100)
					{
						Possible = true;
					}
					else if(PercentD < 100 && PercentG < 100)
					{
						Possible = true;
					}
					else if( PercentD < 100 && PercentG == 100)
					{
						Possible = false;
					}
					else
					{
						t2 = false;
					}
					break;
			}

			//fabc(k,j,c
		}

		f_output << "Case #" << i+1 << ": " << (Possible?"Possible":"Broken") << endl;
		f_output1 << MaxD <<" "<< PercentD << " "<<PercentG << " \t " << (t1?"1":"0") << " " << (t2?"1":"0")  << "\t Case #" << i+1 << ": " << (Possible?"Possible":"Broken") <<  endl;

	}


	f_input.close();
	f_output.close();
	f_output1.close();
	return 0;
}

