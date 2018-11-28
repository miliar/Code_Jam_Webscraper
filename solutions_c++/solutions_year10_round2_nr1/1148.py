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
vector<string> had_string;

/**
 * problem-related functions
 */
bool isexist(string &in);

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
		int inN, inM;
		int ans = 0;
		inputfile >> inN >> inM;
#ifdef DEBUG_OUTPUT
	cout << endl << "===testCase " << nCurCase+1 << endl;
#endif

		string tmp;

		had_string.clear();

		for (int i=0; i<inN; i++)
		{
			inputfile >> tmp;
			had_string.push_back(tmp);
		}

		for (int i=0; i<inM; i++)
		{
			int idx;
			string inPath;
			inputfile >> inPath;

#ifdef DEBUG_OUTPUT
			cout << "inputstring: " << inPath << endl;
#endif

//                        for (idx=0; idx<inPath.size(); idx++)
//                        {
//                                if (inPath[idx] == '/')
//                                        continue;
//                                else
//                                        break;
//                        }

			int nsubstring = 1;
			//ignore '/'
			for (int j=1; j<inPath.size(); j++)
			{
				if (inPath[j] != '/')
				{
					nsubstring++;
					continue;
				}
				else
				{
					//if isexist
					string tmpstring = string(inPath, 0, nsubstring);
					if (!isexist(tmpstring))
					{
						ans++;
						had_string.push_back(tmpstring);
					}

					nsubstring ++;
					//else ans++
					//add string to vector
				}
			}

			if (!isexist(inPath))
			{
				ans++;
				had_string.push_back(inPath);
			}

		}

		//output the result
		outputfile << "Case #" << nCurCase + 1 << ": " << ans << endl;
	}
}

bool isexist(string &in)
{

#ifdef DEBUG_OUTPUT
	cout << "check: " << in << endl;
	cout << "in" << endl;

	for (int i=0; i<had_string.size(); i++)
	{
		cout << had_string[i] << endl;
	}
#endif

	for (int i=0; i<had_string.size(); i++)
	{
		if (had_string[i] == in)
			return true;
	}

	return false;
}

void test()
{
	cout << "--- test start --- "<< endl;
	cout << "--- test end --- "<< endl;
}
