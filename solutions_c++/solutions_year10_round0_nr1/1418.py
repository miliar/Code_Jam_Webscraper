#include <iostream>
using namespace std;

int main()
{
	unsigned int T;
	cin>>T;
	for(int t = 0; t < T; t++)
	{
		unsigned int N,K;
		cin>>N>>K;
		if(K == 0)
		{
			cout<<"Case #"<<t+1<<": OFF"<<endl;
		}
		else if(K == 1)
		{
			if(N == 1)
			{
				cout<<"Case #"<<t+1<<": ON"<<endl;
			}
			else
			{
				cout<<"Case #"<<t+1<<": OFF"<<endl;
			}
		}
		else
		{
			unsigned int tot = 1;
			for(int i = 0; i < N; i++)
			{
				tot <<= 1;
			}
			K%=tot;
			if(K == tot - 1)
			{
				cout<<"Case #"<<t+1<<": ON"<<endl;
			}
			else
			{
				cout<<"Case #"<<t+1<<": OFF"<<endl;
			}
		}
	}
	return 0;
}
