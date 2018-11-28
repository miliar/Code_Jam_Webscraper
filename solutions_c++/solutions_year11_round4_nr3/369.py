#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <queue>
#include <set>
#include <cassert>
#include <cmath>
#include <algorithm>
typedef long long LL; 
using namespace std;
 
#define FOR(k,a,b) for(int k(a); k < (b); ++k)
#define REP(k,a) for(int k=0; k < (a); ++k)

int main()
{
	const int pmax=1000005;
	vector<bool> primes(pmax+1,true);
	FOR(i,2,pmax)
	{
		if(primes[i]==true)
			for(int j=2*i;j<pmax;j+=i)
				primes[j]=false;
	}
	int testCaseCounter;
	cin >> testCaseCounter;
	for(int actTestCase=1;actTestCase<=testCaseCounter;++actTestCase)
	{
		LL N;
		cin >> N;
		LL res=1LL;
		for(LL i=2LL;i*i<=N;++i)
		{
			if(!primes[i])
				continue;
			LL tmp=i*i;
			while(tmp<=N)
			{
				tmp*=i;
				++res;
			}
		}
		if(N==1LL)
			res=0;
		cout << "Case #" << actTestCase << ": "<< res << endl;
	}
	return 0;
}
