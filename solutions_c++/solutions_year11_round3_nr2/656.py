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

struct LengthAndTime
{
	long long m_Len;
	long long m_Times;
	LengthAndTime(long long len, long long times) : m_Len( len ), m_Times( times ){};
	bool operator < (const LengthAndTime lenAndT)
	{
		return m_Len > lenAndT.m_Len;
	}
};

int FindIndex( const vector<LengthAndTime>& lenAndTVec, long long targLen )
{
	if ( targLen == 0 )
		return -1;
	long long llTempLen = 0;
	for ( int iIndex = 0; iIndex < lenAndTVec.size(); iIndex++ )
	{
		llTempLen += lenAndTVec[iIndex].m_Len;
		if ( llTempLen >= targLen )
			return iIndex;
	}
	return -1;
}

int main()
{
	int iCaseNum;

#ifdef SMALL
	std::ifstream inFile("B-small-attempt0.in");
#elif defined LARGE
	std::ifstream inFile("A-large.in");
#else
	std::ifstream inFile("TestData.txt");
#endif
	std::ofstream outFile( "Output.txt" );

	inFile >>iCaseNum;

	long long LL, t, N, C;
	for ( int iCaseIndex = 0; iCaseIndex < iCaseNum; iCaseIndex++ )
	{
		vector<LengthAndTime> LenAndTimeVec;
		inFile >> LL >> t >> N >> C;
		long long llSumLen = 0;
		long long llTotalLen = 0;
		long long CycleNum = N / C;
		long long RemainNum = N % C;
		for ( int iCIndex = 0; iCIndex < C; iCIndex++ )
		{
			long long len;
			inFile >> len;
			len = len << 1;
			if ( iCIndex < RemainNum )
			{
				LenAndTimeVec.push_back( LengthAndTime( len, CycleNum+1 ) );
				llTotalLen += len * (CycleNum+1);
			}
			else
			{
				LenAndTimeVec.push_back( LengthAndTime( len, CycleNum ) );
				llTotalLen += len * CycleNum;
			}
			llSumLen += len;
		};
		long long RemainLen = t % llSumLen;
		int iIndexWhenComp = FindIndex( LenAndTimeVec, RemainLen );
		long long remanT = t;
		for ( int iIndex = 0; iIndex <= iIndexWhenComp; iIndex++ )
		{
			LenAndTimeVec[iIndex].m_Times--;
			remanT -= LenAndTimeVec[iIndex].m_Len;
		}
		if ( iIndexWhenComp >= 0 )
			LenAndTimeVec.push_back(LengthAndTime( -remanT, 1));
		sort( LenAndTimeVec.begin(), LenAndTimeVec.end() );
		long long remainLL = LL;
		for ( int iIndex = 0; iIndex < LenAndTimeVec.size(); iIndex++ )
		{
			if ( remainLL <= 0 )
				break;
			long long reduceL = std::min( LenAndTimeVec[iIndex].m_Times, remainLL );
			remainLL -= reduceL;
			llTotalLen -= ( LenAndTimeVec[iIndex].m_Len>>1 ) * reduceL;
		}

		outFile << "Case #"<<iCaseIndex+1<< ": "<<llTotalLen<<endl;
	}

	outFile.flush();
	outFile.close();
	inFile.close();
	return 0;
}