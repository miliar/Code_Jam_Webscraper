#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;

long long change(long long a)
{
	long long  i;
	if(a==1)
	{
		i=0;
	}
	if(a==0)
	{
		i=1;
	}
	return i;
}

int main()
{	
	ifstream cin("a.in");
	ofstream cout("a.out");
	long long onoff[40];
	long long test;
	long long n,k;
	long long i,j,a,b,c;
	long long total;
	long long time;

	cin>>test;
	for(i=0;i<test;i++)
	{
		total=0;
		cin>>n>>k;
		for(b=0;b<n;b++)
		{
			onoff[b]=0;
		}
		for(j=0;j<n;j++)
		{
			time=0;
			time=k/long long(pow(2,double(j)));
			if(time%2==0)
			{
				onoff[j]=0;
			}
			if(time%2==1)
			{
				onoff[j]=1;
			}

		}
		for(c=0;c<n;c++)
		{
			total+=onoff[c];
		}
		if(total==n)
		{
			cout<<"Case #"<<i+1<<": ON"<<endl;
		}
		else
		{
			cout<<"Case #"<<i+1<<": OFF"<<endl;
		}


	}

	return 0;
}