#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;
/*
long int binary(long int value)
{
	long int out=0;
	for(int i=0;i<32;i++){
		if( (value%2)== 1)
		{
			out = out^(1<<i);
		}
		value = value/10;
	}
	return out;
}
*/

int main()
{
	int T,N;
	ifstream in("a.in");
	ofstream out("a.out");
	in>>T;
	for(int i=0;i<T;i++)
	{
		in>>N;
		long int *ar= new long int[N];
		for(int _i=0;_i<N;_i++)
		{
			in>>ar[_i];
			//std::cout<<ar[_i];
		}
		std::vector<long int> v(ar,ar+N);
		sort(v.begin(),v.end());
		unsigned long int sum1a, sum1 ,sum2a , sum2;
		int j;
		
		for(j=0;j<N;j++)
		{
			sum1 = sum2 = sum1a = sum2a = 0;
			
			for(int first=0;first<j+1;first++)
			{
				sum1=sum1^v[first];
				sum1a += v[first];
			}
			for(int last=j+1;last<N;last++)
			{
				sum2^=v[last];
				sum2a += v[last];
			}
			//std::cout<<(int)sum1<<" "<<sum1<<" "<<sum2<<" "<<sum2a<<std::endl;
			if(sum1 == sum2)
			{
				//sum2=0;
				out<<"Case #"<<i+1<<": "<<sum2a<<std::endl;
				break;
			}
			
		}
		if(j==N)
			out<<"Case #"<<i+1<<": "<<"NO"<<std::endl;
	}
	//std::cin.get();
	return 0;
}