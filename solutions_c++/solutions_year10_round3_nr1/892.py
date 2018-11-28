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
//#define outputfile cout

int main()
{
	ifstream input("A-large(2).in");
	ofstream outputfile("output.txt");
	int sz ;
	
	input >> sz ;

	for( int casen = 1 ; casen <= sz;  ++casen)
	{

		int n ;
		int a; 
		int b;
		vector<int> x;
		vector<int> y;
		int res = 0;

		input >> n ;
		for( int i = 0 ; i < n ; ++i)
		{
			input >> a >> b;
			x.push_back(a);			
			y.push_back(b);
		}
		for( int i = 0 ; i < n ; ++i)
		{
			for( int j = i + 1 ; j < n ; ++j)
			{
				if(( x[i] < x[j] & y[i] < y[j]) || ( x[i] > x[j] & y[i] > y[j]) ) continue;
				++res;
			}
		}

		outputfile << "Case #" << casen << ": " << res << endl;
	}
	getchar();
	return 0;
}
