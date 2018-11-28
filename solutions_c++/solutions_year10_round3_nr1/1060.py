#include <iostream>
#include <vector>
#include <iterator>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>


using namespace std;

int main()
{
	int cases; cin >> cases;		// number of cases 
	//cin.ignore();

	for ( int ca = 1; ca <= cases; ++ca )
	{   
		cerr << "Test: " << ca << endl;  
		int N; cin >> N;
		int A[N], B[N];
		int inter = 0;
		for (int i= 0; i < N; i++)
			cin >> A[i] >> B[i];

		for (int i = 0; i < N-1; i++)
			for (int j = i+1; j < N; j++)
				if ( (A[i] - A[j]) * (B[i] - B[j])  < 0 )
					inter++;

		cout << "Case #" << ca << ": " 
	    	 << inter
			 << endl;
	}
	return 0;
}
