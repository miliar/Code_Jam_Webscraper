#include <fstream>
#include <vector>
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

vector<string> picture;
int nR, nC;
bool check()
{
	for (int i=0; i<nR; i++)
	{
		for (int j=0; j<nC; j++)
		{
			if ((i == nR-1) || (j == nC-1))
			{
				continue;
			}

			if(picture[i][j] == '#')
			{
				if ((picture[i][j+1] == '#')
						&& (picture[i+1][j+1] == '#')
						&& (picture[i+1][j] == '#'))
				{
					picture[i][j] = '/';
					picture[i][j+1] = '\\';
					picture[i+1][j] = '\\';
					picture[i+1][j+1] = '/';
				}
			}
		}
	}

	for (int i=0; i<nR; i++)
	{
		for (int j=0; j<nC; j++)
		{
			if (picture[i][j] == '#')
			{
				return false;
			}
		}
	}

	return true;
}

void solveProblem( ifstream &inputfile, ofstream &outputfile )
{
	int nTestCase, nCurCase;

	inputfile >> nTestCase;

	for (nCurCase = 0; nCurCase < nTestCase; nCurCase++)
	{
		bool ans = false;

		inputfile >> nR >> nC;

		picture.clear();

		for (int i=0; i<nR; i++)
		{
			string tmp;
			inputfile >> tmp;

			picture.push_back(tmp);
		}

		ans = check();
		//output the result
		//
		if (ans)
		{
			outputfile << "Case #" << nCurCase + 1 << ":" << endl;
			for (int i=0; i<nR; i++)
			{
				outputfile << picture[i] << endl;
			}
		}
		else
			outputfile << "Case #" << nCurCase + 1 << ": " << endl << "Impossible" << endl;
	}
}

void test()
{
	cout << "--- test start --- "<< endl;
	cout << "--- test end --- "<< endl;
}
