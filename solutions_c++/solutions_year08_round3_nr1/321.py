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
	ifstream input("input.txt");
	ofstream outputfile("output.txt");
	int sz ;
	
	input >> sz ;

	for( int casen = 1 ; casen <= sz;  ++casen)
	{

		int letters, keys , alpha ;

		vector<int> f ;
		input >> letters >> keys >> alpha ;
		int t;
		for( int i = 0 ; i < alpha ; ++i)
		{
			input >>  t;
			f.push_back(t);
		}
		
		if( letters * keys < alpha ) 
		{
			outputfile << "Case #" << casen << ": "  << "Impossible" << endl;
		}

		sort( f.rbegin(),f.rend());
		int beg = 0;
		int res = 0 ;
		for( int i = 0 ; i < alpha ; ++i)
		{
			if( i % keys == 0 ) ++beg;
			res += beg * f[i];
		}

		outputfile << "Case #" << casen << ": " << res  << endl;
	}
	getchar();
	return 0;
}
