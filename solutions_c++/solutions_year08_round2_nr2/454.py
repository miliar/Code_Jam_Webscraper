#include <iostream>
#include <fstream>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <cassert>

using namespace std;

typedef priority_queue<int, vector<int>, std::greater<int> > pqueue ;

/*
  primes.txt is a list of the primes up to 1,000,000, downloaded from http://primes.utm.edu/lists/small/

  You dream of colors that have never been made,
  you imagine songs that have never been played.
 */

int main(int argc, char *argv[])
{
	assert(argc > 1);
	ifstream ifile(argv[1]);
	
	int cases=0;
	ifile >> cases;
	for(int caseno=1; caseno <= cases; caseno++)
	{
		long long a, b, p;
		ifile >> a >> b >> p;
		ifstream millionprimes("primes.txt");
		vector<int> primes;
		int prime;
		millionprimes >> prime;
		while(millionprimes)
		{
			if(prime >= p && prime <= b-a)
			primes.push_back(prime);	
			millionprimes >> prime;
		}
		map<int, set<int> > primesets;
		for(vector<int>::iterator it = primes.begin(); it != primes.end(); it++)
		{
			set<int> theset;
			theset.insert(*it);
			primesets[*it] = theset;
		}

		for(vector<int>::iterator it = primes.begin(); it != primes.end(); it++)
		{
			for(vector<int>::iterator it2 = primes.begin(); it2 != primes.end(); it2++)
			{
				int product = (*it) * (*it2);
				long long rem = a % product;
				if(rem == 0)
					rem = product;
				if(a - rem + product <= b)
				{
					set<int> unioned = primesets[*it];
					unioned.insert(primesets[*it2].begin(), primesets[*it2].end());
					for(set<int>::iterator sit = unioned.begin(); sit != unioned.end(); sit++)
					{
						primesets[*sit] = unioned;
					}
				}
			}
		}

		int answer=0;
		set<int> primestodo;
		primestodo.insert(primes.begin(), primes.end());

		bool *sieve = new bool[(size_t)(b-a+1)];
		for(int i=0; i< b-a+1; i++)
			sieve[i] = true;

		while(!primestodo.empty())
		{
			int curprime = *primestodo.begin();
			set<int> plist = primesets[curprime];
			for(set<int>::iterator sit = plist.begin(); sit != plist.end(); sit++)
			{
				set<int>::iterator ptd = primestodo.find(*sit);
				assert(ptd != primestodo.end());
				primestodo.erase(ptd);
				int rem = (int)(a % *sit);
				if(rem == 0)
					rem = *sit;
				for(int i = *sit - rem; i <= b-a; i += *sit)
				{
					sieve[i] = false;
				}
			}
			answer++;
		}
		
		for(int i=0; i<b-a+1; i++)
		{
			if(sieve[i])
				answer++;
		}
		cout << "Case #" << caseno << ": " << answer << endl;
	}
}