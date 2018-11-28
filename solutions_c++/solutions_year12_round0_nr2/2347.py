// ProgramB.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


// ProgramA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <map>
#include <string>

using namespace std;

#define fabc(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fa0c(a,b) fabc( a, 0, ( b ) )
#define for_i(a) fa0c( i, ( a ) )
#define for_j(a) fa0c( j, ( a ) )
#define for_k(a) fa0c( k, ( a ) )

enum result{POSSIBLE,NOTPOSSIBLE,POSSIBLE_WITH_SUPRISE};
result scoringPossibility(int totalScore, int bestScore);

int _tmain(int argc, _TCHAR* argv[])
{
	int i,j,k;

	fstream f_input, f_output;
	f_input.open(argv[1],fstream::in);
	f_output.open("ProgramBOut.txt",fstream::out);

	//read test cases
	int T = 0;
	f_input >> T;
	for_i(T)
	{
		int PossibleWithSuprise = 0;
		int Possible = 0;
		int People = 0;
		int MaxSurprise = 0;
		int BestScore = 0;
		f_input >> People;
		f_input >> MaxSurprise;
		f_input >> BestScore;
		for_k(People)
		{
			int totalScore = 0;
			f_input >> totalScore;
			result r = scoringPossibility(totalScore,BestScore);
			if( r == POSSIBLE)
			{
				Possible++;
			}
			else if( r == POSSIBLE_WITH_SUPRISE)
			{
				PossibleWithSuprise++;
			}
		}
		cout << "Case #" << i+1 <<": " << Possible + ((PossibleWithSuprise > MaxSurprise)?MaxSurprise:PossibleWithSuprise) << endl;
		f_output << "Case #" << i+1 <<": " << Possible + ((PossibleWithSuprise > MaxSurprise)?MaxSurprise:PossibleWithSuprise) << endl;
	}
	

	f_input.close();
	f_output.close();
	return 0;
}

result scoringPossibility(int totalScore, int bestScore)
{
	double average = (double)totalScore/3.0;
	cout << average << "\t";;

	if(average - (int)average > .5)
	{
		//cout << ".66" << endl;
		if(((int)average) + 1 >= bestScore && ((int)average) + 1 <= 10)
		{ 
			cout << ((int)average) + 1 << ((int)average) + 1 << ((int)average) <<  " Possible" << endl;
			return POSSIBLE;
		}
		else if(((int)average) + 2 >= bestScore && ((int)average) + 2 <= 10 )
		{
			cout << ((int)average) + 2 << ((int)average) << ((int)average) <<  " Possible With Suprise" << endl;
			return POSSIBLE_WITH_SUPRISE;
		}
		else
		{
			cout << "Not Possible" << endl;
			return NOTPOSSIBLE;
		}
 	}
	else if(average - (int)average == 0)
	{
		//cout << ".0" << endl;
		if(((int)average) >= bestScore)
		{ 
			cout << ((int)average) << ((int)average) << ((int)average) <<  " Possible" << endl;
			return POSSIBLE;
		}
		else if(((int)average) + 1 >= bestScore && ((int)average) + 1 <= 10 && ((int)average) -1 >= 0)
		{
			cout << ((int)average) + 1 << ((int)average) - 1 << ((int)average) <<  " Possible With Suprise" << endl;
			return POSSIBLE_WITH_SUPRISE;
		}
		else
		{
			cout << " Not Possible" << endl;
			return NOTPOSSIBLE;
		}
	}
	else
	{
		if(((int)average)+1 >= bestScore && ((int)average) + 1 <= 10)
		{ 
			cout << ((int)average)+1 << ((int)average) << ((int)average) <<  " Possible" << endl;
			return POSSIBLE;
		}
		else
		{
			cout << " Not Possible" << endl;
			return NOTPOSSIBLE;
		}
		//cout << ".33" << endl;
	}

}