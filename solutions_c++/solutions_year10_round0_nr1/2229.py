
#include<iostream>
#include<math.h>
using namespace std;

int main()
{

	int t;
	int n,k;
	cin>>t;
	int cases=0;
	while(t--)
	{
		cout<<"Case #"<<++cases<<": ";
		cin>>n>>k;
        int temp=pow(2.0,n);
		k=k%temp;
		temp=pow(2.0,n);
		temp--;
		if(temp&k!=temp)
			cout<<"OFF"<<endl;
		else
			cout<<"ON"<<endl;
	}
}