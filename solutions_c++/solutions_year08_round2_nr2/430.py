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



vector<long long> primes;

bool isPrime(long long n)
{
	if( n == 1 ) return false;
	long long m = sqrt((long double) n);
	for( long long i = 0 ; i < primes.size() && i <= m  ; ++i)
		if( n % primes[i] == 0 ) return false;
	return true;
}

void generate()
{
	long long m = sqrt((long double)10000000000ll);
	for( long long i = 2 ; i <= m ; ++i)
	{
		if( isPrime( i )) primes.push_back(i);
	}
}


int main()
{
	ifstream input("input.txt");
	ofstream outputfile("output.txt");
	int n ;
	generate();
	input >> n ;

	for( int casen = 1 ; casen <= n;  ++casen)
	{
		vector<long long> nums;
		vector<int> sets;
		long long a , b , p;
		input >> a >> b >> p;
	
		long long c = b - a + 1;
		for( int j = 0 ; j < c ; ++j)
		{
			nums.push_back(a + j);
			sets.push_back(j);
		}

		long long res = c;

		int pos = 0;
		while ( primes[pos] < p ) ++pos;
		int cnt = 0;
		vector<long long > gp;
		for( ; primes[pos] <= b ; ++pos)
		{
			gp.push_back(primes[pos]);
		}

		for( int i = 0 ; i < nums.size();++i)
			for( int j = i +1 ; j < nums.size();++j)
			{
				
				// check they have a prime factor

				bool isOk = false;

				for( int k = 0 ; k < gp.size();++k)
				{
					if( nums[i] % gp[k] == 0 && nums[j] % gp[k] == 0)
					{
						isOk = true;
						break;
					}
				}

				if( !isOk) continue;

				int oldSet = sets[j];
				int newSet = sets[i];

				for( int k = 0 ; k < nums.size();++k) 
					if( sets[k] == oldSet )
						sets[k] = newSet;
			}

		set<int> ans;
		for( int i = 0 ; i < sets.size();++i) ans.insert(sets[i]);

			




		outputfile << "Case #" << casen << ": " << ans.size()  << endl;
	}

	getchar();
	return 0;
}
