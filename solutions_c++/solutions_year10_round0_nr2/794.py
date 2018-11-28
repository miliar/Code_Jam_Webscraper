
#include<iostream>
#include<math.h>
#include<algorithm>
using namespace std;

int data[1010] ;

int dif[1010];


int gcd(int a,int b)
{
	if(b==0)
		return a;
	return gcd(b,a%b);
}

int main()
{


	int t;
	int n;
	cin>>t;
	int cases=0;
	while(t--)
	{
		cout<<"Case #"<<++cases<<": ";
		cin>>n;

		int i,j;
		for(i=0;i<n;i++)
		{
			cin>>data[i];
		}
		sort(data,data+n);
        for(i=0;i<n-1;i++)
			dif[i]=data[i+1]-data[i];
		int t=dif[0];
		for(i=0;i<n-1;i++)
		{
			t=gcd(t,dif[i]);
		}
		// cout<<t<<" "<<data[0]<<endl;
		if(data[0]%t==0)
		{
			cout<<0<<endl;
		}
		else
		    cout<<t-(data[0]%t)<<endl;
	}
}