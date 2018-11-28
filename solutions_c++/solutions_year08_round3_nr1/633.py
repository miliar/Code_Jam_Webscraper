/**
 *
 * /file a.cpp
 *
 * Contains the solution to the A problem from Round 1C of the Google Code Jam 2008.
 *
 * /author Dimitar Asenov
 * /date July 27, 2008
 */

// A bunch of standard headers.
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

typedef long double real;

using namespace std;

int main()
{
	// Read the number of test cases.
	int TN;
	cin>>TN;

	for (int ni = 1; ni <=TN; ++ni)
	{

		int P,K,L;
		vector<int> freq;
		cin>>P>>K>>L;

		for (int i = 0; i<L; ++i)
		{
			int f;
			cin>>f;
			freq.push_back(f);
		}


		//Boundary
		if (P*K < L)
		{
			cout<<"Case #"<<ni<<": "<< "Impossible" <<endl;
			continue;
		}

		sort(freq.begin(), freq.end() );

		int num_keys = 1;
		int letters = 0;

		long total_keys = 0;
		for (int i = L-1; i>= 0; --i)
		{
			total_keys += freq[i] * num_keys;
			letters++;

			if (letters == K)
			{
				num_keys++;
				letters = 0;
			}
		}

		cout<<"Case #"<<ni<<": "<< total_keys <<endl;
	}

	return 0;
}
