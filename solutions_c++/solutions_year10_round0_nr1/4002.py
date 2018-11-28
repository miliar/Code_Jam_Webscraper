#include <iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int zzz=1;zzz<=T;zzz++)
	{
		int N;
		long K;
		cin>>N>>K;
		int I=0;
		for(int i=0;i<N;i++)
			I |= 1<<i;

		if( (K - (long)I) % ((long)(I + 1))  == 0 )
			cout<<"Case #"<<zzz<<": ON"<<endl;
		else
			cout<<"Case #"<<zzz<<": OFF"<<endl;
	}
}
