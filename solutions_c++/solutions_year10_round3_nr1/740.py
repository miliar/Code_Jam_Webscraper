#include <fstream>
#include <iostream>
#include <map>
using namespace std;

#define dataIn inFile
#define dataOut outFile

int GetIntersectNum( map<int, int>& wireNum )
{
	int result = 0;
	for ( map<int, int>::iterator mapIter = wireNum.begin(); mapIter != wireNum.end(); mapIter++ )
	{
		int right = mapIter->second;
		for ( map<int, int>::iterator iterBefore = wireNum.begin(); iterBefore != mapIter; iterBefore++ )
		{
			if ( iterBefore->second > right )
				result++;
		}
		for ( map<int, int>::iterator iterAfter = mapIter; iterAfter != wireNum.end(); iterAfter++ )
		{
			if ( iterAfter->second < right )
				result++;
		}
	}
	return result;
}

int main()
{
	ifstream inFile("A-large.in");
	//ifstream inFile();
	ofstream outFile("output.txt");

	int caseNum;
	dataIn>>caseNum;
	for ( int i = 0; i < caseNum; i++ )
	{
		map<int, int> wireMap;
		int wireNum;
		dataIn>>wireNum;
		for ( int j = 0; j < wireNum; j++ )
		{
			int leftH, rightH;
			dataIn>>leftH>>rightH;
			wireMap[leftH] = rightH;
		}
		dataOut<<"Case #"<<i+1<<": "<<GetIntersectNum( wireMap )/2<<endl;
	}
	

	//cin.get();
	return 0;
}