#include <iostream>

using namespace std;

int main()
{
	long int t,n,p = 0,temp =1,small = 0,sum = 0;
	cin>>t;
	while(temp <= t)
	{
		cin>>n;
		int a[n];
		small = 0,sum = 0,p =0;
		for(int i= 0; i <n; i++)
		{
			cin>>a[i];
			p = p^a[i]; 	
			sum = sum + a[i];
			if(i == 0)
				small = a[0];
			if(a[i] < small)
				small = a[i];
		}
		if(p) 
			cout<<"Case #"<<temp<<": "<<"NO"<<endl;
		else
		{
			cout<<"Case #"<<temp<<": "<<(sum - small)<<endl;
		}
		temp++;
	}
	
}
