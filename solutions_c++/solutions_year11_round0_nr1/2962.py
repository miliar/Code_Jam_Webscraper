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

//#define TRACE 
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

#define MAX_NUM 100
char in_color[MAX_NUM];
int in_num[MAX_NUM];
int blue_obj;
int blue_cur;
int org_obj;
int org_cur;
void solveProblem( ifstream &inputfile, ofstream &outputfile )
{
	int nTestCase, nCurCase;

	inputfile >> nTestCase;

	for (nCurCase = 0; nCurCase < nTestCase; nCurCase++)
	{
		int n_N;

		inputfile >> n_N;
		blue_cur = 1;
		org_cur = 1;


		for (int i = 0; i < n_N; i++)
		{
			inputfile >> in_color[i];
			inputfile >> in_num[i];
		}

		int ans = 0;

		int j = 0;
		while (j < n_N)
		{
			int step_seconds = 0;

			if (in_color[j] == 'B')
			{
				blue_obj = in_num[j];

				step_seconds += abs(blue_obj - blue_cur) + 1;

				blue_cur = blue_obj;
			}
			else
			{
				org_obj = in_num[j];
				step_seconds += abs(org_obj - org_cur) + 1;
				org_cur = org_obj;
			}

			ans += step_seconds;
			for (int k = j+1; k < n_N; k++)
			{
				if (in_color[k] != in_color[j])
				{
					if (in_color[k] =='B')
					{
						blue_obj = in_num[k];
						
						if (blue_cur == blue_obj)
							break;

						if (blue_cur < blue_obj)
						{
							blue_cur += step_seconds;
							if (blue_cur > blue_obj)
							{
								blue_cur = blue_obj;
							}
						}
						else
						{
							blue_cur -= step_seconds;
							if (blue_cur < blue_obj)
							{
								blue_cur = blue_obj;
							}
						}
					}
					else
					{
						org_obj = in_num[k];

						if (org_cur == org_obj)
							break;

						if (org_cur < org_obj)
						{
							org_cur += step_seconds;
							if (org_cur > org_obj)
							{
								org_cur = org_obj;
							}
						}
						else
						{
							org_cur -= step_seconds;
							if (org_cur < org_obj)
							{
								org_cur = org_obj;
							}
						}
					}

					break;
				}
			}
#ifdef TRACE 
		printf ("N: %d blue_obj: %d org_obj: %d blue_cur: %d org_cur: %d\n", step_seconds, blue_obj, org_obj, blue_cur, org_cur);
#endif

			j++;
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
