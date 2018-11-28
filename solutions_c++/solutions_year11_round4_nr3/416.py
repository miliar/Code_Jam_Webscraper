#include <fstream>
#include <cmath>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

long long n;

bool isPrime(int i)
{
	int j;
	for(j=2; j<= sqrt((long double)i); ++j)
		if(i%j == 0)
			return 0;
	return 1;
}

int getPow(long long i)
{
	int ans=0;
	long double ND = n, ID = i; 
	while(ID <= ND)
	{
		++ans;
		ID*=(long double)i;
	}
	return ans;
}

int solve()
{
	if(n==1)
		return 0;
	int i, ans=0;
	for(i=2; i<=sqrt((long double)n)+1; ++i)
	{
		if(isPrime(i))
		{
			int k = getPow(i);
			if(k>=2)
				ans += k - 1;
		}
	}
	return ans + 1;
}

int main()
{
	int caseN, t;
	fin>>t;
	//t = 100;
	//n = 1;
	for(caseN=1; caseN<=t; ++caseN)
	{
		fin>>n;
		fout<<"Case #"<<caseN<<": "<<solve()<<endl;
	//	++n;
	}
	return 0;
}