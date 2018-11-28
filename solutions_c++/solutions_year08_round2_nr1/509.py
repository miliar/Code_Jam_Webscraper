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

		long long n, A, B, C, D, x0, y0 , M;

		input >> n >>  A >> B >> C >>  D >>  x0 >>  y0 >>  M;

		vector<long long> a;
		vector<long long> b;

		int X = x0, Y = y0 ;
		a.push_back( X);
		b.push_back(Y);
		for(int i = 1; i < n ; ++i)
		{
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			a.push_back( X);
			b.push_back(Y);
		}
		
		int res  = 0;

		for( int i = 0; i < a.size();++i)
			for( int j = i + 1 ; j < a.size();++j)
				for( int k = j +1 ; k < a.size();++k)
				{
					int xsum = a[i] + a[j] + a[k];
					int ysum = b[i] + b[j] + b[k];

					
					int xr = xsum / 3;
					int yr = ysum / 3;

					if( xr * 3 == xsum && yr * 3 == ysum ) ++res;

				}

		outputfile << "Case #" << casen << ": " << res << endl;
	}

	getchar();
	return 0;
}
