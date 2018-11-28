#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <fstream>

using namespace std;



int main()
{
	ifstream input("B-large.in");
	ofstream outputfile("output.txt");
	long long sz ;
	
	input >> sz ;

	for( long long casen = 1 ; casen <= sz;  ++casen)
	{

		long long res = 0;
		long long n,k,b,t;
		input >> n >> k >> b >> t;
		vector<long long> pos;
		vector< long long> v;
		vector<bool> canReach ;
		vector<long long> lead;
		long long countReach = 0;
		long long q;
		for( long long i = 0 ; i < n ; ++i)
		{
			input >> q;
			pos.push_back(q);
		}
		for( long long i = 0 ; i < n ; ++i)
		{
			input >> q;
			bool doReach = false;
			if( t * q >= b - pos[i]) doReach = true;
			v.push_back(q);
			canReach.push_back(doReach);
			if(doReach) ++countReach;
			lead.push_back(0);
			
		}

		long long leaders = 0;
		for( long long i = n -1 ; i >= 0 ; --i)
		{
			lead[i] = leaders;
			if( !canReach[i] ) lead[i] = 200000;
			if(!canReach[i]) ++leaders;
			
		}

		sort(lead.begin(),lead.end());
		
		if( countReach < k ) 
		{
			outputfile << "Case #" << casen << ": " << "IMPOSSIBLE" << endl;
		}
		else
		{
			for( long long i = 0 ; i < k ; ++i) res += lead[i];
			outputfile << "Case #" << casen << ": " << res << endl;
		}
	}
	getchar();
	return 0;
}
