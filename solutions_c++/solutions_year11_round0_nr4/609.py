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

#define MAXSIZE 1010

struct IDValue
{
	int m_iID;
	int m_iValue;
	IDValue( int iID, int iValue ) : m_iID( iID ), m_iValue( iValue ){};
	bool operator < ( const IDValue& opp )
	{
		return m_iValue < opp.m_iValue;
	}
};

int CalcSwapNumber( const std::vector<IDValue>& dataVector )
{
	int iSwapNumber = 0;
	int iSize = dataVector.size();
	bool bIsVisited[MAXSIZE];
	memset( bIsVisited, 0, sizeof( bIsVisited ) );
	for ( int iIndex = 0; iIndex < iSize; iIndex++ )
	{
		if ( bIsVisited[iIndex] )
			continue;
		if ( dataVector[iIndex].m_iID == iIndex )
		{
			bIsVisited[iIndex] = true;
			continue;
		}
		int iTempIndex = iIndex;
		int iReserveNumber = iSwapNumber;
		do 
		{
			iSwapNumber++;
			bIsVisited[iTempIndex] = true;
			iTempIndex = dataVector[iTempIndex].m_iID;
		} while( dataVector[iTempIndex].m_iID != iIndex );
		iSwapNumber++;
		//printf( "%d ", iSwapNumber - iReserveNumber );
		bIsVisited[iTempIndex] = true;
	}
	printf( "\n" );
	return iSwapNumber;
}

int main()
{
	int iCaseNum;
#ifdef SMALL
	std::ifstream inFile("D-small-attempt1.in");
#elif defined LARGE
	std::ifstream inFile("D-large.in");
#else
	std::ifstream inFile("TestData.txt");
#endif
	std::ofstream outFile( "Output.txt" );

	inFile >>iCaseNum;
	for ( int iCaseIndex = 0; iCaseIndex < iCaseNum; iCaseIndex++ )
	{
		int iDataNum;
		std::vector<IDValue> dataVector;
		inFile >> iDataNum;
		for ( int iDataIndex = 0; iDataIndex < iDataNum; iDataIndex++ )
		{
			int iData;
			inFile >> iData;
			dataVector.push_back( IDValue( iDataIndex, iData ) );
		}
		sort( dataVector.begin(), dataVector.end() );
		printf( "%d:\t", iCaseIndex+1 );
		int iSwapNumber = CalcSwapNumber( dataVector );
		outFile << "Case #" <<iCaseIndex+1 << ": " << std::setiosflags( std::ios::fixed )<< std::setprecision(6) << iSwapNumber*1.0 << std::endl;
	}

	outFile.flush();
	outFile.close();
	inFile.close();
	return 0;
}