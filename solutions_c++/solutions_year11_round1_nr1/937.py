#include <iostream>

using namespace std;

int main()
{
	int numTest;
	cin>>numTest;
	for(int run=0; run < numTest; ++run)
	{
		unsigned long long n;
		double pd, pg;
		cin>>n>>pd>>pg;
		if(pg == 100 && pd != 100) goto badone;
		if(pg == 0 && pd != 0) goto badone;
		pd /= 100;
		for(unsigned long long i=1; i<=n; ++i)
		{
			for(unsigned long long j=0; j<=i; ++j)
			{
				if(((double)j/(double)i) == pd) {
					cout<<"Case #"<<run+1<<": Possible"<<endl;
					goto endinner;
				}
				if(((double)j/(double)i) > pd) break;
			}
		}
		badone:
		cout<<"Case #"<<run+1<<": Broken"<<endl;
		endinner:
			run=run;
	}
}
