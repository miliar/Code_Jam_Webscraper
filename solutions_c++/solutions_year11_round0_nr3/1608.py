#include <iostream>
#include <cstdio>
#include <cstring>
#include <fstream>

using namespace std;

int num[20],a[1100];

ifstream fin("C-large.in.txt");
ofstream fout("C-small-attempt0.out");

int main()
{
	int t,i,j;
	fin>>t;
	for(i=1;i<=t;i++)
	{
		memset(num,0,sizeof(num));
		int n,k,w,sum=0,mins=10000000;
		fin>>n;
		for(j=0;j<n;j++)
		{
			fin>>a[i];
			sum+=a[i];
			if(a[i]<mins) mins=a[i];
			k=a[i];
			w=0;
			while(k)
			{
				if(k%2) num[w]++;
				w++;
				k/=2;
			}
		}
		sum-=mins;
		fout<<"Case #"<<i<<": ";
		for(j=0;j<20;j++)
		if(num[j]%2!=0)
		{
			fout<<"NO"<<endl;
			break;
		}
		if(j==20)
		{
			fout<<sum<<endl;
		}
	}
	return 0;
}
