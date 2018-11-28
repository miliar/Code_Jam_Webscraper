#include<iostream>
#include<fstream>
#include<string>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
ifstream in("easy.in");
ofstream out("easy.out");
long long deg(long long p)
{
	long long j=1;
	long long k;
	for(k=0;k<p;k++)
		j*=2;
	return j;
}
int main()
{
	long long t;
	long long n,k,sol=0;
	long long i;
	in>>t;
	for(i=0;i<t;i++)
	{
		in>>n>>k;
		sol = deg(n)-1;
		if(n==1)
		{
			if(k%2==0)
			{
				out<<"Case #"<<i+1<<": OFF"<<endl;
				continue;
			}
			if(k%2==1)
			{
				out<<"Case #"<<i+1<<": ON"<<endl;
				continue;
			}
		}
		if(sol == k%(sol+1))
		{
			out<<"Case #"<<i+1<<": ON"<<endl;
			continue;
		}
		else
		{
			out<<"Case #"<<i+1<<": OFF"<<endl;
			continue;
		}

	}
	return 0;
}

