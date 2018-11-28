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
#include <iterator>

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

int n_max;
//num : elements 数量
//k: 生成组合数数量
//pre 组合的内容
void calcCombination(const int elements[], int num, int k, vector<int> &pre, vector<int> &total)
{
	assert (k <= num);

	vector<int> post = total;

	if (k == 0)
	{
		if (pre.size() == 0)
			return;

		// output one combination
//        copy(pre.begin(), pre.end(), ostream_iterator<int>(cout, " "));

		for (int i = 0; i < pre.size(); i++)
		{
			for (int j = 0; j < post.size(); j++) 
			{
				if (pre[i] == post[j])
				{
					post.erase( post.begin() + j);
					break;
				}
			}
		}
		
//        cout << " haha ";
//        copy(post.begin(), post.end(), ostream_iterator<int>(cout, " "));
//        cout << endl;

		int bsum_pre, bsum_post;
		int sum_post, sum_pre;

		sum_pre = pre[0];
		bsum_pre = pre[0];
		for (int i = 1; i < pre.size(); i++)
		{
			bsum_pre ^= pre[i];
			sum_pre += pre[i];
		}

		sum_post = post[0];
		bsum_post = post[0];
		for (int i = 1; i < post.size(); i++)
		{
			bsum_post ^= post[i];
			sum_post += post[i];
		}

		if (bsum_pre == bsum_post)
		{
			int tmp_max; 
			tmp_max = (sum_post > sum_pre) ? sum_post : sum_pre;
			if (tmp_max > n_max)
			{
				n_max = tmp_max;
			}
		}

		return;
	}

	for (int i=0; i <= num - k; ++i)
	{
		pre.push_back(elements[i]);
		calcCombination(elements + i + 1, num - i - 1, k - 1, pre, post);
		pre.pop_back();
	}
}

int data[100];
void solveProblem( ifstream &inputfile, ofstream &outputfile )
{
	int nTestCase, nCurCase;

	inputfile >> nTestCase;

	for (nCurCase = 0; nCurCase < nTestCase; nCurCase++)
	{
		int ans;
		//output the result
		int n_num;
		inputfile >> n_num;

		vector<int> one;
		vector<int> total;

		n_max = 0;

		for (int i = 0; i < n_num; i++)
		{
			inputfile >> data[i];
			total.push_back (data[i]);
		}

		for (int i = 0; i <= n_num/2 ; i++)
		{
			calcCombination (data, n_num, i, one, total);
		}

		if (n_max == 0)
		{
			outputfile << "Case #" << nCurCase + 1 << ": NO" << endl;
		}
		else
		{
			outputfile << "Case #" << nCurCase + 1 << ": " << n_max << endl;
		}
	}
}

void test()
{
	cout << "--- test start --- "<< endl;
	cout << "--- test end --- "<< endl;
}
