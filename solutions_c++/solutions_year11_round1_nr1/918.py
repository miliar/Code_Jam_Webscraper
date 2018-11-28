//#define SMALL
#define LARGE
#ifdef SMALL
#elif defined LARGE
#else
#endif
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

long long GCD( long long A, long long B )
{
	if ( B==0 )
		return A;
	return GCD( B, A%B );
}

bool Judge( long long N, long long Pd, long long Pg )
{
	if ( Pd == 100 && Pg == 100 )
		return true;
	if ( Pd == 0 && Pg == 0)
		return true;
	if ( Pg >= 100 || Pg == 0 )
		return false;
	int PdAnd100 = GCD( Pd, 100 );
	if ( 100/PdAnd100 > N )
		return false;
	return true;
}


int main()
{
	int iCaseNum;
#ifdef SMALL
	std::ifstream inFile("A-small-attempt2.in");
#elif defined LARGE
	std::ifstream inFile("A-large.in");
#else
	std::ifstream inFile("TestData.txt");
#endif
	std::ofstream outFile( "Output.txt" );

	inFile >>iCaseNum;
	long long N, Pd, Pg;
	for ( int iCaseIndex = 0; iCaseIndex < iCaseNum; iCaseIndex++ )
	{
		inFile >> N >> Pd >> Pg;
		outFile << "Case #" << iCaseIndex+1 <<": ";
		if ( Judge(N, Pd, Pg) )
			outFile << "Possible" <<std::endl;
		else
			outFile << "Broken" << std::endl;
	}

	outFile.flush();
	outFile.close();
	inFile.close();
	return 0;
}