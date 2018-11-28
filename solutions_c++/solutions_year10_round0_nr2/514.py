#include<fstream>
#include<iostream>
using namespace std;
int gcd(int a,int b)
{
	if(a<b)
	{
		int l=a;
		a=b;
		b=l;
	}
	if(b>0)
	{
		return gcd(a%b,b);
	}
	else return a;
}
int main()
{
	ifstream fin("B-small-attempt1.in");
	ofstream fout("1.out");
	int N,n;
	int data[200];
	fin>>N;
	int i,j;
	for(j=0;j<N;j++)
	{
	
		fin>>n;
		for(i=0;i<n;i++)
		{
			fin>>data[i];
		}
		for(i=1;i<n;i++)
		{
			data[i]-=data[0];
			if(data[i]<0)
				data[i]*=-1;
		}
		int m=data[1];
		for(i=2;i<n;i++)
		{
			m=gcd(m,data[i]);
		}
		int s=(data[0]/m)*m;
		if(s<data[0])s=s+m;
		fout<<"Case #"<<j+1<<": "<<s-data[0]<<endl;
	}
	return 0;
}