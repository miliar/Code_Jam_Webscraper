#include <iostream>
using namespace std;


int main()
{
	long long a, m, sxor,sum;
	
	int T,N;
	cin>>T;
	for(int i = 0; i < T; i++)
	{
		m = 1000000000;
		sum=0;
		cin>>N;
		for(int j = 0; j < N; j++)
		{
			cin>>a;
			sum+=a;
			if(j==0)
			{
				sxor = a;
				if(m>a)
					m=a;
			}
			else
			{
				sxor = sxor^a;
				if(m>a)
					m=a;
			}
		}
		cout<<"Case #"<<(i+1)<<": ";
		if(sxor !=0 )
			cout<<"NO"<<endl;
		else cout<<(sum-m)<<endl;
			
	}
	
}

