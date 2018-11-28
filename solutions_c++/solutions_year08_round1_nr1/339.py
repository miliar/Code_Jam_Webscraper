
#include <cstdio>
#include <iostream>
#include <vector>
#include <fstream>
#include <cassert>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;


void ReadVec(istream & in, __int64 number, vector<__int64> & v)
{
	for( __int64 i = 0; i < number; ++i )
	{
		__int64 x;
		in >> x;
		v.push_back(x);
	}
}

__int64 FindMinimum( vector<__int64> & x, vector<__int64> & y )
{
	std::sort(x.begin(),x.end());
	std::sort(y.begin(),y.end());
	__int64 result = 0;
	for( size_t i = 0,j=y.size()-1; i < x.size(); ++i,--j )
	{
		result += x[i] * y[j];
	}
	return result;
}

int main(int argc, char * argv[])
{
	if ( argc < 3 )
	{
		cout << "MinimumSP inputfile outputfile" << endl;
		return 1;
	}

	ifstream in(argv[1],ios::in);
	ofstream out(argv[2]);
	if( !in )
	{
		cout << "can't open input file" << endl;
		return 1;
	}

	if( !out )
	{
		cout << "can't open output file" << endl;
		return 1;
	}
	

	int totalCase = 0;
	in>> totalCase;
//	cout << totalCase << endl;
	assert( totalCase > 0 );

	for( int i = 1; i <= totalCase; ++i )
	{
		int number;
		in >> number;
		vector<__int64> vecx;
		vector<__int64> vecy;
		ReadVec(in,number,vecx);
		ReadVec(in,number,vecy);
		out << "Case #" << i <<": " << FindMinimum(vecx,vecy) << endl;
	}
}