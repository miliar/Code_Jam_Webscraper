#include<iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int i=0;i<T;++i)
	{
		unsigned long long int sum=0;
		unsigned long int min;
		unsigned long int total_exor;
		int N;
		cin >> N;
		cin >> min;  //treat first num as min..
		total_exor = min;
		sum = min; //init sum to min...i.e. first num..
		for(int j=1;j<N;++j)
		{
			unsigned long int  num;
			cin >> num;
			sum += num;
			if(min > num)	min = num;
			total_exor = total_exor ^ num;
		}
		if(total_exor)//nonzero
		{
			cout<<"Case #"<< i+1<<": "<<"NO\n";
		}
		else //0  means division possible
		{
			cout<<"Case #"<< i+1<<": "<<(sum-min)<<"\n";	
		}
	}
	return 0;
}
