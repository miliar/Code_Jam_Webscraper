/**
 *
 * /file a.cpp
 *
 * Contains the solution to the A problem from Round 1A of the Google Code Jam 2008.
 *
 * /author Dimitar Asenov
 * /date July 26, 2008
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
	int N;
	cin>>N;

	for (int ni = 1; ni <=N; ++ni)
	{

		int n;
		cin>>n;

		vector<int> a,b;

		for (int i = 0; i<n; ++i)
		{
			int t;
			cin>>t;
			a.push_back(t);
		}

		for (int i = 0; i<n; ++i)
		{
			int t;
			cin>>t;
			b.push_back(t);
		}

		sort(a.begin(), a.end() );
		sort(b.begin(), b.end() );

		long ip = 0;

		for (int i = 0; i<n; ++i)
		{
			ip += a[i]*b[n-i-1];
		}

		cout<<"Case #"<<ni<<": "<< ip <<endl;
	}

	return 0;
}
