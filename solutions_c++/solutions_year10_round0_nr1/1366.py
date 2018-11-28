#include <iostream>
#include <string>
#include <fstream>
#include <cstring>

#include <vector>
#include <map>

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

void solveProblem( ifstream &inputfile, ofstream &outputfile )
{
	//get input
	int nTestCase;

	inputfile >> nTestCase;

	for (int nCurTest=0; nCurTest<nTestCase; nCurTest++)
	{
		int nN,nK;
		int nNumBubleOn = 0; //need nNumBubleOn times toggole to make the buble on from the init
				//state
		int nTimes; 
		bool bState = false;

		inputfile >> nN;
		inputfile >> nK;
#ifdef DEBUG_OUTPUT
		cout << "====testcases: " << nCurTest+1 << " of " << nTestCase << endl;
		cout << "N: " << nN << " K: " << nK << endl;
#endif

//                nNumBubleOn = 1;
//                for (int i=1; i<nN; i++)
//                {
//                        nNumBubleOn = 2*nNumBubleOn + 1;
//                }

		nNumBubleOn = (1 << nN) - 1;

		nTimes = nK;

#ifdef DEBUG_OUTPUT
		cout << "nNumBubleOn: " << nNumBubleOn << " times: " << nTimes << endl;
#endif
		if (nTimes < nNumBubleOn)
		{
			bState = false;
		}
		else
		{
			if (nTimes%(nNumBubleOn+1) == nNumBubleOn)
			{
				bState = true;
			}
			else
			{
				bState = false;
			}
		}

#ifdef DEBUG_OUTPUT
		cout << "buble light:? " << bState << endl;
#endif

		if (bState)
		{
			outputfile << "Case #" << nCurTest + 1 << ": ON" << endl;
		}
		else
		{
			outputfile << "Case #" << nCurTest + 1 << ": OFF" << endl;
		}
	}
}

void test()
{
}
