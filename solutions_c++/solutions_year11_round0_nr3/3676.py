#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
	int Z;
	scanf("%d",&Z);
	for(int i = 0; i < Z; i++)
	{
		int N;
		scanf("%d",&N);
		long long min = 1000001;
		long long sum = 0;
		long long v;
		for(int j = 0; j < N; j++)
		{
			long long r;
			scanf("%lld",&r);
			if(j == 0) v = r;
			else v ^= r;
			sum += r;
			if(r < min) min = r;
		}
		cout<<"Case #"<<i+1<<": ";
		if(v == 0)
		{
			cout<<sum - min<<endl;
		}
		else cout<<"NO"<<endl;
	}
	return 0;
}
