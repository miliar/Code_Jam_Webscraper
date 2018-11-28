#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	int n,k;
	int count=0,cases,flag,makeallone;
	
	cin>>cases;
	while(count++<cases)
	{
		flag=0;
		cin>>n>>k;

		makeallone = (int) pow(2.0,n);
		if(k > makeallone)
			k = k%makeallone;
		if(k == makeallone-1)
			flag=1;
		if(flag)
		cout<<"Case #"<<count<<": "<<"ON"<<endl;
		else
		cout<<"Case #"<<count<<": "<<"OFF"<<endl;
	}

	return 0;
}
