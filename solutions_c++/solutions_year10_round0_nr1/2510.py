#include<iostream>

using namespace std;

void main()
{
	int T,N[10000];
	long K[10000];
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	for(int i=0;i<T;i++)
	cin>>N[i]>>K[i];

	int tc=1;

	for(i=0;i<T;i++)
	{	
		tc=1;
		for(int j=0;j<N[i];j++)
			tc*=2;
		if((K[i]+1)%tc==0)
			cout<<"Case #"<<i+1<<": ON"<<endl;
		else
			cout<<"Case #"<<i+1<<": OFF"<<endl;
	}
}
