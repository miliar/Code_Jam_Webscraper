//#define SMALL
#define LARGE
#ifdef SMALL
#elif defined LARGE
#else
#endif
#include <fstream>
#include <iostream>

//��Ҫ���������е��������������Ϊ0
//���������������������Сֵ������ĺͣ�Ȼ�󽫺� - ��Сֵ

int main( int argc, char* argv[] )
{
	int iCaseNum;
#ifdef SMALL
	std::ifstream inFile("C-small-attempt0.in");
#elif defined LARGE
	std::ifstream inFile("C-large.in");
#else
	std::ifstream inFile("TestData.txt");
#endif

	std::ofstream outFile("Output.txt");

	inFile >> iCaseNum;
	for ( int iCaseIndex = 0; iCaseIndex < iCaseNum; iCaseIndex++ )
	{
		int xorResult = 0;
		long long iSum = 0;
		int iMin = 0x7fffffff;
		int iCandyNum;
		inFile >> iCandyNum;
		for ( int iCandyIndex = 0; iCandyIndex < iCandyNum; iCandyIndex++ )
		{
			int iCandyWeight;
			inFile >> iCandyWeight;
			xorResult ^= iCandyWeight;
			iMin = std::min( iCandyWeight, iMin );
			iSum += iCandyWeight;
		}
		outFile << "Case #" <<iCaseIndex+1 << ": ";
		if ( xorResult )
			outFile << "NO" << std::endl;
		else
			outFile << iSum - iMin << std::endl;
	}
}