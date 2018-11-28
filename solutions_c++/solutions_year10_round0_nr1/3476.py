#include<iostream>
using namespace std;

int main()
{
	long N,K,T,counter=0;
	cin>>T;
	while(T>0)
	{
		counter++;
		cin>>N>>K;
		cout<<"Case #"<<counter<<": ";
		if((K+1)%(1<<N)==0)
			cout<<"ON"<<endl;
		else
                        cout<<"OFF"<<endl;
		T--;
	}
	return 0;
}
