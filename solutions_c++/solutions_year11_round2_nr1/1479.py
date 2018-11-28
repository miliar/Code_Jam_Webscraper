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

#define MAXSIZE 200

char compMap[MAXSIZE][MAXSIZE];
double WP[MAXSIZE];
double OWP[MAXSIZE];
double OOWP[MAXSIZE];

void CalcWP(int iSize)
{
	memset( WP, 0, sizeof(WP) );
	for ( int iIndex = 0; iIndex < iSize; iIndex++ )
	{
		double iCompNum = 0.0;
		double iWinNum = 0.0;
		for ( int iIndex_Op = 0; iIndex_Op < iSize; iIndex_Op++ )
		{
			if ( compMap[iIndex][iIndex_Op] == '.' )
				continue;
			iCompNum++;
			if ( compMap[iIndex][iIndex_Op] == '1')
				iWinNum++;
		}
		WP[iIndex] = iWinNum / iCompNum;
	}
}

void CalcOWP(int iSize)
{
	memset( OWP, 0, sizeof(OWP) );
	for ( int iIndex = 0; iIndex < iSize; iIndex++ )
	{
		int iOpNum = 0;
		double dSpecOWP = 0.0;
		for ( int iIndex_Op = 0; iIndex_Op < iSize; iIndex_Op++ )
		{
			if ( compMap[iIndex][iIndex_Op] == '.' )
				continue;
			iOpNum++;
			double iCompNumOp = 0.0;
			double iWinNumOp = 0.0;
			for ( int iIndex_OOP = 0; iIndex_OOP < iSize; iIndex_OOP++ )
			{
				if (compMap[iIndex_OOP][iIndex_Op] == '.' || iIndex_OOP == iIndex )
					continue;
				iCompNumOp++;
				if (compMap[iIndex_OOP][iIndex_Op] == '0')
					iWinNumOp++;
			}
			dSpecOWP += iWinNumOp / iCompNumOp;
		}
		OWP[iIndex] = dSpecOWP / iOpNum;
	}
}

void CalcOOWP(int iSize)
{
	memset( OOWP, 0, sizeof(OOWP) );
	for ( int iIndex = 0; iIndex < iSize; iIndex++ )
	{
		int iOpNum = 0;
		double dSumOOWP = 0.0;
		for ( int iIndex_Op = 0; iIndex_Op < iSize; iIndex_Op++ )
		{
			if ( compMap[iIndex][iIndex_Op] == '.' )
				continue;
			iOpNum++;
			dSumOOWP += OWP[iIndex_Op];
		}
		OOWP[iIndex] = dSumOOWP / iOpNum;
	}
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
	int iSize;
	for ( int iCaseIndex = 0; iCaseIndex < iCaseNum; iCaseIndex++ )
	{
		memset( compMap, 0, sizeof(compMap) );
		inFile >> iSize;
		for ( int iIndex = 0; iIndex < iSize; iIndex++ )
			inFile >> compMap[iIndex];
		CalcWP( iSize );
		CalcOWP( iSize );
		CalcOOWP( iSize );

		outFile << "Case #"<<iCaseIndex+1<< ":"<<std::endl;
		for ( int iIndex = 0; iIndex < iSize; iIndex++ )
		{
			double RPI = 0.25 * WP[iIndex] + 0.5 * OWP[iIndex] + 0.25 * OOWP[iIndex];
			outFile << std::setprecision(12) << RPI << std::endl;
		}
	}

	outFile.flush();
	outFile.close();
	inFile.close();
	return 0;
}