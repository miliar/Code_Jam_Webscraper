#include <iostream>
using namespace std;

int main(void)
{

	int T,N,K;
	int i;
	
	cin>>T;
	for(i=1;i<=T;i++)
	{
		cin>>N>>K;
		N=1<<N;
		cout<<"Case #"<<i<<": ";
		if(K%N==N-1)
			cout<<"ON"<<endl;
		else
			cout<<"OFF"<<endl;
	}

//	system("PAUSE");
	return 0;
}
