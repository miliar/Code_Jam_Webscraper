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
#include <string>
using namespace std;

char charMap[100][100];

bool Convert(int R, int C)
{
	for ( int iRowIndex = 0; iRowIndex < R; iRowIndex++ )
	{
		for ( int iColIndex = 0; iColIndex < C; iColIndex++ )
		{
			if ( charMap[iRowIndex][iColIndex] == '#')
			{
				if(charMap[iRowIndex+1][iColIndex] == '#' &&
					charMap[iRowIndex][iColIndex+1] == '#' &&
					charMap[iRowIndex+1][iColIndex+1] == '#')
				{
					charMap[iRowIndex][iColIndex] = '/';
					charMap[iRowIndex+1][iColIndex] = '\\';
					charMap[iRowIndex][iColIndex+1] = '\\';
					charMap[iRowIndex+1][iColIndex+1] = '/';
				}
				else
					return false;
			}
		}
	}
	return true;
}

int main()
{
	int iCaseNum;

#ifdef SMALL
	std::ifstream inFile("A-small-attempt0.in");
#elif defined LARGE
	std::ifstream inFile("A-large.in");
#else
	std::ifstream inFile("TestData.txt");
#endif
	std::ofstream outFile( "Output.txt" );

	inFile >>iCaseNum;
	int R;
	int C;
	for ( int iCaseIndex = 0; iCaseIndex < iCaseNum; iCaseIndex++ )
	{
		inFile >> R >> C;
		for ( int iRowIndex = 0; iRowIndex < R; iRowIndex++)
			inFile >> charMap[iRowIndex];
		bool bResult = Convert(R, C);
		outFile << "Case #"<<iCaseIndex+1<< ": "<<std::endl;
		if ( !bResult )
			outFile << "Impossible" << std::endl;
		else
		{
			for (  int iRowIndex = 0; iRowIndex < R; iRowIndex++ )
				outFile << charMap[iRowIndex] << endl;
		}
	}

	outFile.flush();
	outFile.close();
	inFile.close();
	return 0;
}