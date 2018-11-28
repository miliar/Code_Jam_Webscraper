#include <iostream>
#include <fstream>
#include <inttypes.h>
#include <assert.h>

using namespace std;

int main(int argc, char* argv[])
{
	ifstream f(argv[1]);
	int testcases;
	f >> testcases;
	for(int i=0;i<testcases;i++)
	{
		uint64_t N=0,K=0;
		f >> N >> K;
		assert(N!=0);
		uint64_t res=K;
		uint64_t mod=(1<<N)-1;
		bool ret=(res&mod)==mod;
		cout << "Case #" << (i+1);
		if(ret)
			cout << ": ON" << endl;
		else
			cout << ": OFF" << endl;
	}
}
