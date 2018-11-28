#include <iostream>

using namespace std;

long long n, K;

int main(void)
{
	int t;
	cin>>t;
	for(int caseN=1;caseN<=t;caseN++)
	{
		cin>>n>>K;
		cout<<"Case #"<<caseN<<": ";
		if(K==(1LL<<n)-1) cout<<"ON"<<endl;
		else if (K<(1LL<<n)-1) cout<<"OFF"<<endl;		
		else
		{
			K-=((1LL<<n)-1);
			if(K%(1LL<<n)) cout<<"OFF"<<endl;
			else cout<<"ON"<<endl;
		}
	}

	return 0;
}
