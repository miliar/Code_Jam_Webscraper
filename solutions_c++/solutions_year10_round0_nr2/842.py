#include  <iostream>
#include <stdio.h>
#include <math.h>
#include <fstream>
using namespace std;
int n;
long a[1000];
long GCD(long a, long b)
{
    while( 1 )
    {
        a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

        if( b == 0 )
			return a;
    }
}
long find()
{
	int re=0;
	
	if(n==2)
	{
		long temp=abs(a[0]-a[1]);
		long h=a[0]/temp;
		a[0]-=temp*h;
		if(a[0]<=0)
			re= a[0];
		else
			re= a[0]-temp;
	}
	if(n== 3)
	{
		long temp1=abs(a[0]-a[1]);
		long temp2=abs(a[1]-a[2]);
		if(temp2==0)
		{
			long temp=abs(a[0]-a[1]);
			long h=a[0]/temp;
			a[0]-=temp*h;
			if(a[0]<=0)
				re= a[0];
			else
				re= a[0]-temp;
		}
		else if(temp1==0)
		{
			long temp=abs(a[2]-a[1]);
			long h=a[2]/temp;
			a[2]-=temp*h;
			if(a[2]<=0)
				re= a[2];
			else
				re= a[2]-temp;
		}
		else
		{
		long temp3=GCD(temp1,temp2);
		long h1=a[0]/temp3;
		a[0]-=temp3*h1;
		if(a[0]<=0)
			re= a[0];
		else
			re= a[0]-temp3;
		}
	}
	return re;
}
int main()
{
	ofstream fout ("google.out");
    ifstream fin ("google.in");
	long m;
	fin>>m;
	
	for(int i=0;i<m;i++)
	{
		fin>>n;
		for(int j=0;j<n;j++)
		{
			fin>>a[j];
			
		}
		int re=find();
		fout<<"Case #"<<i+1<<": "<<-1*re<<endl;
	}
	return 1;
}