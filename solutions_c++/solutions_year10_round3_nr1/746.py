#include <fstream>
#include <map>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#include <assert.h>
using namespace std;

/*
 * define macros
  */
//#define TEST 
//#define DEBUG_OUTPUT
//#define TRACE_OUTPUT

/*
 * framework functions
 * */
void solveProblem(ifstream &inputfile, ofstream &outputfile);
void test();

/* *
 * define limits
 * */

/*
 * define gloab variables
 * */
vector< pair<int, int> > points;
//避免重复计算,将中间值用map来保存

/**
 * problem-related functions
 */

/**
 * problem-related test functions
 */

/*
 * argv[1] : input file name
 * argv[2] : output file name
*/
int main( int argc, char* argv[] )
{

#ifdef TEST
	test();
	return 0;
#endif

	if( argc != 3 )
	{
		cout << "err: no input data file or output data file" << endl;
		return -1;
	}

	ifstream inFile( argv[1], ifstream::in );
	if( !inFile )
	{
		cout << "error: input file" << endl;
		return -1;
	}

	ofstream outFile( argv[2], ofstream::out|ofstream::trunc );
	if( !outFile)
	{
		cout << "error: output File" << endl;
		return -1;
	}

	solveProblem(inFile, outFile);
	
	inFile.close();
	outFile.close();

	return 0;
}

void solveProblem( ifstream &inputfile, ofstream &outputfile )
{
	int nTestCase, nCurCase;

	inputfile >> nTestCase;

	for (nCurCase = 0; nCurCase < nTestCase; nCurCase++)
	{
		int ans = 0;
		int nN;

		points.clear();

		inputfile >> nN;

		for (int i=0; i<nN; i++)
		{
			int ina,inb;

			inputfile >> ina >> inb;

			pair<int, int> newpoint(ina, inb);
			for (int j=0; j<points.size(); j++)
			{
				if ((newpoint.first - points[j].first) * (newpoint.second - points[j].second) < 0)
					ans++;
			}
			points.push_back(newpoint);
		}
		//output the result
		outputfile << "Case #" << nCurCase + 1 << ": " << ans << endl;
	}
}

void test()
{
	cout << "--- test start --- "<< endl;
	cout << "--- test end --- "<< endl;
}
