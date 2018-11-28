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
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>
using namespace std;

#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define in(x,s) (s.find(x)!=s.end())

typedef long long int64;
typedef vector<int> VI;
typedef vector<string> VS;

const double eps = 1E-12;
const double pi=acos(-1.0); 


ifstream fin("c.in");
ofstream fout("c.out");

int T;
long long N;

const int MAX = 1000024;
bool isPrime[MAX];

void computePrime()
{
	memset(isPrime,true,sizeof(isPrime));
	isPrime[1] = false;
	for(int i=2;i*i<MAX;i++)
	{
		if(isPrime[i])
		{
			for(int j=i+i;j<MAX;j+=i)
				isPrime[j] = false;
		}
	}
}

long long distinctPrimeNum;
long long factorNumber;

long long newApproach(long long a)
{
	long long r = 0;
	for(int i=2;i<MAX;i++)
	{
		if(isPrime[i])
		{
			long long count =0;
			long long t = 1;
			while(t*i <= N)
			{
				count++;
				t = t*i;
			}
			if(count<=1)
				return r+1;
			r += count-1;

			
		}

	}
	return r+1;
}
void computeDistictPrimeNumber(long long a)
{
	if(a<10000)
	{
		distinctPrimeNum = 0;
		for(int i=2;i<=a;i++)
			if(isPrime[i])
			distinctPrimeNum ++;
	}
	
}
void computeCount()
{
	long long primeNum = 0;	
	factorNumber = 0;
	

	for(int i=2;i<MAX;i++)
		if(isPrime[i])
		{
			long long count =0;
			long long t = 1;
			while(t*i <= N)
			{
				count++;
				t = t*i;
			}
			if(count==0)
				break;
			primeNum++;
			factorNumber += count;

		}
	factorNumber += distinctPrimeNum - primeNum;

}



int main()
{
	computePrime();
	fin>>T;
	long long res;
	for(int c=1;c<=T;c++)
	{
		fin>>N;
		if(N==1LL) 
		{
			res = 0;
			goto output;
		}

		//computeDistictPrimeNumber(N);
		//computeCount();

		res = newApproach(N);
		//res = factorNumber+1 - distinctPrimeNum;


output:
		cout<<"Case #"<<c<<": "<<res<<endl;
		fout<<"Case #"<<c<<": "<<res<<endl;
		
	}
	return 0;
}
