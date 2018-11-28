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

long long buf[500001];

int main()
{
	ifstream input("input.txt");
	ofstream outputfile("output.txt");
	int sz ;
	
	input >> sz ;

	for( int casen = 1 ; casen <= sz;  ++casen)
	{
		long long n, m, X, Y , Z ;
		input >> n >> m >> X >> Y >> Z ;
		vector<long long> A;
		long long t;
		for( int i = 0 ; i < m ; ++i) 
		{
			input >> t;
			A.push_back(t);
		}
		
		vector<long long >  s;
		for( int i = 0 ; i < n ; ++i)
		{
			 
			s.push_back( A[i % m]);
			A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z ;
		}

		fill(buf,buf+500001,0);
		const long long mod = 1000000007ll;
		
		buf[0] = 1;
		for( int i = 1 ; i < n ; ++i)
		{
			long long cnt = 1; // for itself.
			for( int j = 0 ; j < i ; ++j)
			{
				if( s[j] < s[i] )
				{
					cnt += buf[j];
					cnt %= mod;
				}
			}
			buf[i] = cnt;

		}
		
		long long res = 0; 
		for( int i = 0 ; i < n ; ++i)
		{
			res += buf[i];
			res %= mod;
		}


		outputfile << "Case #" << casen << ": " <<  res % mod << endl;
	//	cout << "Case #" << casen << ": Solved"  << endl;
	}
//	cout << "All problems solved ..." << endl;
	getchar();
	return 0;
}
