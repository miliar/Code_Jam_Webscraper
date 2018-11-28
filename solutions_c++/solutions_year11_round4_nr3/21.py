#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

vector<int> primes;

bool isPrime(int x)
{
	for (int i=0;i<(int)primes.size();i++)
	{
		int t = primes[i];
		if (t * t > x)
			return true;
		if (x % t == 0)
			return false;
	}
	return true;
}

void build()
{
	for (int i=2;i<3000000;i++)
		if (isPrime(i))
			primes.push_back(i);
}
__int64 getAns(__int64 x)
{
	if (x == 1)
		return 0;
	__int64 res = 0;
	for (int i=0;i<(int)primes.size();i++)
	{
		__int64 t = primes[i];
		if (t * t > x)
			return res + 1;
		
		__int64 cnt = 0;
		while (t <= x)
		{
			t *= primes[i];
			++cnt;
		}
		res += cnt - 1;
	}
	throw 0;
	return res + 1;
}

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int taa;
	cin>>taa;
	cout.setf(ios_base::fixed);
	cout.precision(20);
	build();
	for (int aaa = 0; aaa < taa; aaa++)
	{
		__int64 n;
		cin>>n;
		cout<<"Case #"<<aaa + 1<<": ";
		cout<<getAns(n);
		cout<<endl;
	}
	
}