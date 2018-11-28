#include <iostream>
#include <fstream>
using namespace std;

int a[1002];
int next[1002];
int count[1002];

int main()
{
	int t,r,k,n,temp,sum,nextstep;
	bool iffirst;
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
	fin>>t;
	for (int i=0;i<t;i++)
	{
		fin>>r>>k>>n;
		for (int j=0;j<n;j++)
			fin>>a[j];
		for (int j=0;j<n;j++)
		{
			temp=j;
			sum=0;
			iffirst=true;
			while (iffirst||(sum+a[temp]<=k &&temp!=j)) 
			{
				sum+=a[temp];
				temp++;
				temp%=n;
				iffirst=false;
			}
			count[j]=sum;
			next[j]=temp;
				while (next[j]<0) next[j]+=n;
		}
		temp=0;
		sum=0;
		for (int j=0;j<r;j++)
		{
			sum+=count[temp];
			temp=next[temp];
		}
		fout<<"Case #"<<i+1<<": "<<sum<<endl;
	}

}