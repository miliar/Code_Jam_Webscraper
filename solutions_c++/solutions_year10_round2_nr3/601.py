#include <iostream>
#include <fstream>
#include <inttypes.h>

using namespace std;

uint64_t binom(uint64_t k, uint64_t n)
{
	uint64_t ret=n;
	for(int64_t i=n-1;i>=(n-k+1);i--)
	{
		ret*=i;
	}
	uint64_t fact=k;
	for(int64_t i=k-1;i>1;i--)
	{
		fact*=i;
	}
	return ret/fact;
}

uint64_t solve(uint64_t n, uint64_t max, uint64_t prev, bool skipRange)
{
	if(n==1)
		return 1;
	uint64_t ret=0;
	for(uint64_t i=0;i<max-1;i++)
	{
		uint64_t tmp=solve(i+1,i+1,n,false);
		if(tmp)
		{
			int64_t range=prev-n-1;
			uint64_t space=max-i-2;
			if(space>range);
			else if(space==0 || skipRange)
				ret+=tmp;
			else
				ret+=(tmp*binom(space, range));
			
			ret%=100003;
		}
	}

	return ret%100003;
}

int main(int argc, char* argv[])
{
	ifstream f(argv[1]);
	int cases;
	f >> cases;
	for(int cas=0;cas<cases;cas++)
	{
		int N;
		f >> N;
		uint64_t ret=solve(N,N,N,true);
		cout << "Case #" << (cas+1) << ": " << ret << endl;
	}

}
