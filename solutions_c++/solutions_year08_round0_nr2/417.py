/**
 *
 * /file b.cpp
 *
 * Contains the solution to the B problem from the Qualification Round of the Google Code Jam 2008.
 *
 * /author Dimitar Asenov
 * /date July 17, 2008
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	// Read the number of test cases.
	int n;
	cin>>n;

	for (int ni = 1; ni <=n; ++ni)
	{

		// Read in the turnaround time and numer of train trips.
		int t,na,nb;
		cin>>t>>na>>nb;

		vector< int > trains_needed_A;
		vector< int > trains_needed_B;
		vector< int > trains_available_A;
		vector< int > trains_available_B;

		//Read trains leaving from A.
		for (int nai = 0; nai<na; ++nai)
		{
			int h,m;
			char c;

			cin>>h>>c>>m;
			trains_needed_A.push_back( h*60 + m );

			cin>>h>>c>>m;
			trains_available_B.push_back( h*60 + m + t );
		}

		//Read trains leaving from B.
		for (int nbi = 0; nbi<nb; ++nbi)
		{
			int h,m;
			char c;

			cin>>h>>c>>m;
			trains_needed_B.push_back( h*60 + m );

			cin>>h>>c>>m;
			trains_available_A.push_back( h*60 + m + t );
		}

		// Sort all lists.
		sort(trains_needed_A.begin(), trains_needed_A.end());
		sort(trains_needed_B.begin(), trains_needed_B.end());
		sort(trains_available_A.begin(), trains_available_A.end());
		sort(trains_available_B.begin(), trains_available_B.end());

		unsigned int availabe_ndx = 0;

		// Compute trains needed in A.
		int total_trains_A = 0;
		for( int nai = 0; nai<na; ++nai)
			if ( availabe_ndx<trains_available_A.size() && trains_needed_A[ nai ] >= trains_available_A[ availabe_ndx ] ) ++availabe_ndx;
			else ++total_trains_A;

		// Compute trains needed in B.
		int total_trains_B = 0;
		availabe_ndx = 0;
		for( int nbi = 0; nbi<nb; ++nbi)
			if ( availabe_ndx<trains_available_B.size() && trains_needed_B[ nbi ] >= trains_available_B[ availabe_ndx ] ) ++availabe_ndx;
			else ++total_trains_B;

		cout<<"Case #"<<ni<<": "<<total_trains_A<<' '<<total_trains_B<<endl;
	}

	return 0;
}
