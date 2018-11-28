/* 
 * Google CodeJam
 * Problem A. Saving the Universe From Evil
 *
 */

#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<set>
#include<iterator>
#include<cstdlib>
#include<cassert>

using namespace std;

#define N_MIN 0 
#define N_MAX 20

#define S_MIN 2 
#define S_MAX 100
#define Q_MIN 0 
#define Q_MAX 1000

struct ltstr
{
  bool operator()(string s1, string s2) const
  {
    return s1 < s2;
  }
};

/* Entry point. */
int main(int argc, char * argv[])
{

	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int N = 0;

	/* First line of the input. No of test cases.*/
	fin >> N; 
	assert((N_MIN < N) && (N <= N_MAX));

	cout << "# Test case count = " << N << endl << endl;

	/* For each test case 1 to N. */
	for(int tc_index = 1; tc_index <= N; tc_index++) 
	{ 
		/* Reset. */
		int S = 0, Q = 0;
		set<string, ltstr> SearchEngines; /* Name of all search engines. */
		string line;

		fin >> S; /* No of search engines. */
		assert((S_MIN <= S) && (S <= S_MAX));
		cout << "S = " << S << endl;
		getline(fin, line); /* eat newline. */

		/* Read search engine names 1 to S. */
		for(int se_index = 1; se_index <= S; se_index++) {

			getline(fin, line);
			SearchEngines.insert(line);
		}

		/* Print contents. */

		fin >> Q; /* No of queries. */
		assert((Q_MIN <= Q) && (Q <= Q_MAX));
		cout << "Q = " << Q << endl;
		getline(fin, line); /* eat newline. */
		
		int switch_count = 0;
		set<string, ltstr> UsedEngines; /* Engines used in queries. */

		/* Read each query from 1 to Q. */
		for(int qy_index = 1; qy_index <= Q; qy_index++) {

			/* Populate UsedEngines. */
			getline(fin, line);
			UsedEngines.insert(line);

			/* Increment switch count if difference between UsedEngines and 
			 * SearchEngines is a empty set. */

			set<string, ltstr> Diff;
		 	set_difference(SearchEngines.begin(), SearchEngines.end(), 
					UsedEngines.begin(), UsedEngines.end(),
                 			inserter(Diff, Diff.begin()), ltstr());

			if(Diff.empty() == true) {
				
				switch_count++; /* Increment Switch */

				/* Clear UsedEngines. */
				UsedEngines.clear();

				UsedEngines.insert(line);
			}
		}

		/* Print contents. */

		/* Print output. */
		fout << "Case #"<< tc_index << ": " << switch_count << endl;

	} // Next test case 

	return 0;
}

