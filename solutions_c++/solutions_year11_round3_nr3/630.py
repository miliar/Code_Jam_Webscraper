#define SMALL
//#define LARGE
#ifdef SMALL
#elif defined LARGE
#else
#endif
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <string>
using namespace std;

long long NoteVec[11000];

bool CheckMatch( long long Freq, long long N )
{
	for ( int iNoteIndex = 0; iNoteIndex < N; iNoteIndex++ )
	{
		if ( Freq > NoteVec[iNoteIndex] && ( Freq % NoteVec[iNoteIndex] != 0) )
			return false;
		if ( Freq < NoteVec[iNoteIndex] && ( NoteVec[iNoteIndex] % Freq != 0) )
			return false;
	}
	return true;
}

long long GetMatchNote( long long L, long long H, long long N )
{
	for ( long long FreqIndex = L; FreqIndex <= H; FreqIndex++ )
	{
		if ( CheckMatch( FreqIndex, N ) )
			return FreqIndex;
	}
	return -1;
}

int main()
{
	int iCaseNum;

#ifdef SMALL
	std::ifstream inFile("C-small-attempt0.in");
#elif defined LARGE
	std::ifstream inFile("A-large.in");
#else
	std::ifstream inFile("TestData.txt");
#endif
	std::ofstream outFile( "Output.txt" );
	
	inFile >>iCaseNum;
	long long N, L, H;
	for ( int iCaseIndex = 0; iCaseIndex < iCaseNum; iCaseIndex++ )
	{
		inFile >> N >> L >> H;
		for ( int iNoteIndex = 0; iNoteIndex < N; iNoteIndex++ )
			inFile >> NoteVec[iNoteIndex];
		long long llResult = GetMatchNote(L, H, N);
		outFile << "Case #"<<iCaseIndex+1<< ": ";
		if ( llResult < 0 )
			outFile << "NO" << endl;
		else
			outFile << llResult << endl;
	}

	outFile.flush();
	outFile.close();
	inFile.close();
	return 0;
}