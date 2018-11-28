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

void solveProblem( ifstream &inputfile, ofstream &outputfile )
{
	int nTestCase, nCurCase;

	inputfile >> nTestCase;

	for (nCurCase = 0; nCurCase < nTestCase; nCurCase++)
	{
		vector<string> table;
		vector<double> wp;
		vector<int> win;
		vector<int> lose;
		vector<int> conponents;
		vector<double> owp;
		vector<double> oowp;

		table.clear();

		int nN;

		inputfile >> nN;

		//input
		for (int i=0; i<nN; i++)
		{
			string tmp;
			inputfile >> tmp;
			table.push_back(tmp);
		}

		//caculate wp
		for (int i=0; i<nN; i++)
		{
			int nWin = 0;
			int	nLose = 0;
			for (int j=0; j<nN; j++)
			{
				if (table[i][j] == '1')
				{
					nWin++;
				}
				else if (table[i][j] == '0')
				{
					nLose++;
				}
			}
			double t_wp = (double)nWin / (double)(nWin + nLose);
			wp.push_back(t_wp);
			win.push_back(nWin);
			lose.push_back(nLose);
		}

		//cacluate owp
		for (int i=0; i<nN; i++)
		{
			double t_owp = 0; 
			for (int j=0; j<nN; j++)
			{
				//component
				if (table[i][j] != '.')
				{
					if (table[i][j] == '1')
						t_owp += (double)(win[j]) / (win[j]+lose[j]-1);
					else
						t_owp += (double)(win[j]-1) / (win[j]+lose[j]-1);
				}
			}
			owp.push_back(t_owp/(win[i]+lose[i]));
		}

		//caculate oowp
		for (int i=0; i<nN; i++)
		{
			double t_oowp = 0;
			for (int j=0; j<nN; j++)
			{
				if (table[i][j] != '.')
				{
					t_oowp += owp[j];
				}
			}
			oowp.push_back(t_oowp/(win[i]+lose[i]));
		}

#ifdef TRACE_OUTPUT
		cout << "wp" << endl;
		for (int i=0; i<nN; i++)
		{
			cout << wp[i] << " ";
		}
		cout <<endl << "owp" << endl;
		for (int i=0; i<nN; i++)
		{
			cout << owp[i] << " ";
		}
		cout <<endl << "oowp" << endl;
		for (int i=0; i<nN; i++)
		{
			cout << oowp[i] << " ";
		}
		cout << endl;

#endif

		int ans;
		//output the result
		outputfile << "Case #" << nCurCase + 1 << ": " << endl;
		for (int i=0; i<nN; i++)
		{
			outputfile << setprecision(10) << (0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]) << endl;
		}
	}
}

void test()
{
	cout << "--- test start --- "<< endl;
	cout << "--- test end --- "<< endl;
}
