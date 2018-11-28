#include <fstream>
#include <iostream>
#include <map>
using namespace std;

#define dataIn inFile
#define dataOut outFile

int cirDiv( int n1, int n2, int c )
{
	int result = 0;
	n1 *= c;
	while ( n1 < n2 )
	{
		n1 *= c;
		result++;
	}
	return result;
}

int deshu( int n )
{
	int result = 0;
	while ( n )
	{
		n = n>>1;
		result++;
	}
	return result;
}

int main()
{
	ifstream inFile("B-small-attempt0.in");
	//ifstream inFile();
	ofstream outFile("output.txt");
	int caseNum;
	dataIn>>caseNum;
	for ( int i = 0; i < caseNum; i++ )
	{
		int L, P, C;
		dataIn>>L>>P>>C;
		dataOut<<"Case #"<<i+1<<": "<<deshu( cirDiv(L, P, C) )<<endl;
	}
	cout<<"end"<<endl;
	cin.get();
	return 0;
}