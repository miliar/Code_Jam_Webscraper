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
#define DEBUG_OUTPUT
//#define TRACE_OUTPUT

/*
 * framework functions
 * */
void solveProblem(ifstream &inputfile, ofstream &outputfile);
void test();

/* *
 * define limits
 * */
#define MXA_N 1000

/*
 * define gloab variables
 * */
int queues[MXA_N];

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
	//get inputs
	int nTestCase;
	inputfile >> nTestCase;
	int nTimes,nCapacity,nQueueSize;
	int nQueueStartIdx = 0;
	int nTotalMoney = 0;

	for (int nCurCase=0; nCurCase<nTestCase; nCurCase++)
	{
		memset(queues, 0, sizeof(queues));
		inputfile >> nTimes;
		inputfile >> nCapacity;
		inputfile >> nQueueSize;
#ifdef DEBUG_OUTPUT
		cout << "====testcases: " << nCurCase+1 << " of " << nTestCase << endl;
		cout << "R: " << nTimes << " K: " << nCapacity << " N: " << nQueueSize<< endl;
#endif

		nQueueStartIdx = 0;
		for (int i=0; i<nQueueSize; i++)
		{
			inputfile >> queues[i];
#ifdef DEBUG_OUTPUT
		cout << queues[i] << " ";
#endif
		}
#ifdef DEBUG_OUTPUT
		cout << endl;
#endif

		nTotalMoney = 0;
		for (int i=0; i<nTimes; i++)
		{
			int nSumPeople = 0;
			int nGroups = 0;

			while (nSumPeople<nCapacity)
			{
				nGroups++;
				if (nGroups > nQueueSize)
					break;

				nSumPeople += queues[nQueueStartIdx];

				if ((nSumPeople > nCapacity) )
					break;

				nTotalMoney += queues[nQueueStartIdx];
				nQueueStartIdx = (nQueueStartIdx+1)%nQueueSize;
			}
		}

		outputfile << "Case #" << nCurCase + 1 << ": " << nTotalMoney << endl;
	}
}

void test()
{
}
