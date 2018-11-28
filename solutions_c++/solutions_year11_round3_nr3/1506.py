#include<iostream>
using namespace std;

#include<stdio.h>

int main()
{
	int flag=0;
	long long int l,h,t,n,i,j,k,c,a[11000];
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n>>l>>h;
		for(j=0;j<n;j++)
			cin>>a[j];
		flag=0;
		for(k=l;k<=h;k++)
		{
			c=0;
			for(j=0;j<n;j++)
			{
				if(((a[j]%k)==0) || ((k%a[j])==0))
					c++;
			}
			if(c==n)
			{
				c=k;
				flag=1;
				goto asd;
			}
		}
		asd:
		if(flag==0)
			cout<<"Case #"<<i<<": NO";
		else
			cout<<"Case #"<<i<<": "<<c;
		cout<<"\n";
	}
	return 0;
}
