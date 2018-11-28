#include<iostream>

using namespace std;
int T, N, K;

int main()
{
	
	cin >> T;
	//~ cout<<(1<<31)-1<<endl;
	for(int i = 0;i<T;i++)
	{
		cin >> N >> K;
		if((K+1) % (1<<N) == 0)
			cout<<"Case #"<<(i+1)<<": ON"<<endl;
		else
			cout<<"Case #"<<(i+1)<<": OFF"<<endl;
	}
}
