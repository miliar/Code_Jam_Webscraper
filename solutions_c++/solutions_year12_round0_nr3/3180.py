#include<cstdio>
#include<iostream>
#include<cmath>
#include<fstream>
#include<string>
using namespace std;

bool recycle(int a, int b)
{
	int digitsa=0,digitsb=0,i=0,l;
	bool answer=false;
	l=(a/pow(10.0,i));
	while(l!=0)
	{
		i++;
		l=(a/pow(10.0,i));
	}
	digitsa=i;
	i=0;
	l=(b/pow(10.0,i));
	while(l!=0)
	{
		i++;
		l=(b/pow(10.0,i));
	}
	digitsb=i;
	if(digitsa!=digitsb)
	{
		return false;
	}
	int p1=0,p2=0,newa=0,newb=0;
	for(int j=0;j<digitsa;j++)
	{
		p1=a/pow(10.0,j);
		p2=a-(p1*pow(10.0,j));
		newa=(p2*pow(10.0,digitsa-j))+p1;
		if(b==newa)
		{
			answer=true;
			return answer;
			break;
		}
	}
	for(int j=0;j<digitsb;j++)
	{
		p1=b/pow(10.0,j);
		p2=b-(p1*pow(10.0,j));
		newb=(p2*pow(10.0,digitsb-j))+p1;
		if(a==newb)
		{
			answer=true;
			return answer;
			break;
		}
	}
	return answer;
}
int main()
{
	int t,a,b,x=0;
	ifstream infile ("test small.txt");
	ofstream outfile;
	outfile.open("output test.txt");
	infile>>t;
	for(int i=0;i<t;i++)
	{
		x=0;
		infile>>a>>b;
		for(int n=a;n<b;n++)
		{
			for(int m=n+1;m<=b;m++)
			{
				if(recycle(n,m)==true)
				{
					x++;
				}
			}
		}
		outfile<<"Case #"<<i+1<<": "<<x<<endl;
	}
	return 0;
}
