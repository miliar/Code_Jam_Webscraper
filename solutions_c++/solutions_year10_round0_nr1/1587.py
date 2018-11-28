#include<stdio.h>
#include<iostream>
#include<math.h>


using namespace std;

int main()
{
	int n;
	long long int k;
	long long int temp1,temp2;

	int p;

	int t;

	scanf("%d",&t);

	for ( int i=0;i<t;i++)
	{
		scanf("%d%lld",&n,&k);
		temp1=pow(2,n) ;
		temp2=k%temp1;
		temp1-=1;
		if(temp1==temp2)
		{
			cout<<"Case #"<<i+1<<": "<<"ON"<<endl;
		}
		else
			cout<<"Case #"<<i+1<<": "<<"OFF"<<endl;
	}
	return 0;
}

