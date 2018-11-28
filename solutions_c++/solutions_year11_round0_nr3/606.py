//#define SMALL
#define LARGE
#ifdef SMALL
#elif defined LARGE
#else
#endif
#include <fstream>
#include <iostream>

//需要满足则所有的数做异或结果必须为0
//如果满足该条件，则求出最小值与数组的和，然后将和 - 最小值

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