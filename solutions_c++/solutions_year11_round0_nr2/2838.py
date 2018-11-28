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

#include <unordered_map>
#include <unordered_set>

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

//#define TRACE
#define MAX_SIZE 100
vector<string> v_combine;
vector<string> v_clear;

typedef pair <string, char> inPair;

unordered_map<string, char> hm_combine;
unordered_set<string> hs_clear;

void solveProblem( ifstream &inputfile, ofstream &outputfile )
{
	int nTestCase, nCurCase;

	inputfile >> nTestCase;

	for (nCurCase = 0; nCurCase < nTestCase; nCurCase++)
	{
#ifdef TRACE
		cout << "=== testcase: " << nCurCase + 1 << endl;
#endif
		int n_c = 0;
		int n_d = 0;	
		int n_n = 0;	
		string input_data;

		v_combine.clear();
		v_clear.clear();
		hm_combine.clear();
		hs_clear.clear();

		inputfile >> n_c;
		for (int i = 0; i < n_c; i++)
		{
			string tmp;
			inputfile >> tmp;

			string key(tmp, 0, 2);	
			char value = tmp[2];

			hm_combine.insert(pair<string, char>(key, value));

#ifdef TRACE
			cout << "combine: "<< key << " " << value << endl;
#endif
		}

		inputfile >> n_d;
		for (int i = 0; i < n_d; i++)
		{
			string tmp;
			inputfile >> tmp;
			hs_clear.insert(tmp);

#ifdef TRACE
			cout << "clear: "<< tmp << endl;
#endif
		}

		inputfile >> n_n;

		input_data.clear();
		inputfile >> input_data;

		for (int i = 1; i < n_n; i++)
		{
			//combination
			string combine;
			combine.clear();
			combine	+= input_data[i-1];
			combine += input_data[i];

			string combine_rse; 
			combine_rse.clear();
			combine_rse += input_data[i];
			combine_rse += input_data[i-1];

			unordered_map<string, char>::iterator itr = hm_combine.find(combine);
			unordered_map<string, char>::iterator itr_rev = hm_combine.find(combine_rse);
			if (itr != hm_combine.end())
			{
				input_data[i-1] = itr->second;
				input_data[i] = 0;
				continue;
			}

			if (itr_rev != hm_combine.end())
			{
				input_data[i-1] = itr_rev->second;
				input_data[i] = 0;
				continue;
			}

			//clear
			//clear all the list
			for (int j=0; j<i; j++)
			{
				string str_clear;
				str_clear.clear();
				str_clear	+= input_data[j];
				str_clear += input_data[i];

				string clear_rse; 
				clear_rse.clear();
				clear_rse += input_data[i];
				clear_rse += input_data[j];

				if ( (hs_clear.find(str_clear) != hs_clear.end()) 
						|| (hs_clear.find(clear_rse) != hs_clear.end()) )
				{
					for(int idx = 0; idx <= i; idx++)
					{
						input_data[idx] = 0;
					}
					break;
				}
			}

#ifdef TRACE
//            for (int tmp = 0; tmp < n_n; tmp++)
//            {
//                if (input_data[tmp] == 0)
//                {
//                    outputfile << "_";
//                }
//                else
//                    outputfile << input_data[tmp] ;
//            }

//            outputfile << endl;
#endif
		}

		outputfile << "Case #" << nCurCase + 1 << ": ["; 
		int idx_i = 0;
		while (idx_i < n_n)
		{
			if (input_data[idx_i] != 0)
			{
				outputfile << input_data[idx_i];
				break;
			}
			idx_i ++;
		}
		for (int i = idx_i+1; i < n_n; i++)
		{
			if (input_data[i] == 0)
				continue;
			outputfile << ", " << input_data[i] ;
		}

		outputfile << "]" << endl;
	}
}

void test()
{
	cout << "--- test start --- "<< endl;
	cout << "--- test end --- "<< endl;
}
