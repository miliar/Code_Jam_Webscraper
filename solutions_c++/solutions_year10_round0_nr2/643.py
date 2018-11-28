#include <iostream>
#include <string>
#include <fstream>
#include <cstring>

#include <vector>
#include <map>

#include <assert.h>

#include "cryptopp560/nbtheory.h" //http://prdownloads.sourceforge.net/cryptopp/cryptopp560.zip

using namespace CryptoPP;
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
#define MAX_INT_LEN 50
#define MAX_INT_NUM 1000

/*
 * define gloab variables
 * */
//避免重复计算,将中间值用map来保存
//char inputNum[MAX_INT_LEN+50];
Integer g_Integers[MAX_INT_NUM];
Integer g_subs[MAX_INT_NUM];

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

	for (int nCurCase=0; nCurCase<nTestCase; nCurCase++)
	{
		int nNumSubs = 0;
		int nNumEvent;
		inputfile >> nNumEvent;
		Integer nMinInput;
#ifdef DEBUG_OUTPUT
		cout << "====testcases: " << nCurCase+1 << " of " << nTestCase << endl;
#endif

		for (int i=0; i<nNumEvent; i++)
		{
			string tmp;
			inputfile >> tmp;
			g_Integers[i] = Integer(tmp.c_str());

			if (i == 0)
			{
				nMinInput = g_Integers[i];
			}
			else
			{
				if (g_Integers[i] < nMinInput)
				{
					nMinInput = g_Integers[i];
				}
			}
		}

		nNumSubs = 0;
		for (int i=0; i<nNumEvent-1; i++)
		{
			g_subs[nNumSubs] = (g_Integers[0] - g_Integers[i+1]).AbsoluteValue();

			if (g_subs[nNumSubs] == 0)
				continue;

			nNumSubs++;
#ifdef DEBUG_OUTPUT
		cout << "[" << i << "]" << "gcdsubs: " << g_subs[i];
#endif
		}
#ifdef DEBUG_OUTPUT
		cout << endl;
#endif

		Integer nGcd = g_subs[0];
		assert (nGcd != 0);
		if (nNumSubs > 1)
		{
			for (int i=1; i<nNumSubs; i++)
			{
				nGcd = GCD(nGcd, g_subs[i]);

				if (nGcd == Integer::One())
					break;
			}
		}
#ifdef DEBUG_OUTPUT
		cout << "gcds: " << nGcd << " input0: " << g_Integers[0] <<endl;
#endif

		Integer nResult;
//                int nT=0;
		assert (nGcd != 0);
		//这里是瓶颈
		//1 不要选g_Integers[0]了，选最小的那个
		//2 修改循环方式
//                while (nT * nGcd < g_Integers[0])
//                {
//                        nT++;
//                }
//                Integer nT = g_Integers[0]/nGcd;
//                nResult = (nT * nGcd == g_Integers[0]) ? 0 : (nT + Integer::One()) * nGcd - g_Integers[0];
		Integer nSelectedInput = g_Integers[0];
		Integer nT = nSelectedInput/nGcd;
		nResult = (nT * nGcd == nSelectedInput) ? 0 : (nT + Integer::One()) * nGcd - nSelectedInput;

		outputfile << "Case #" << nCurCase + 1 << ": " << nResult << endl;
	}
}

void test()
{
}
