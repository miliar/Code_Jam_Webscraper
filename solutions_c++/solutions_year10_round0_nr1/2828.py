#include<iostream>
using namespace std;

int main()
{
	int Test;
	cin>>Test;
	int N,K;
	for(int T=1;T<=Test;T++)
	{
		cout<<"Case #"<<T<<": ";
		cin>>N>>K;
		if( (K+1)%( (1<<N) )== 0 )
			cout<<"ON"<<endl;
		else cout<<"OFF"<<endl;
	}
	return 0;
}
