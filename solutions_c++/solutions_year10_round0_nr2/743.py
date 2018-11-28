#include<iostream>
#include<cstdio>
#include<fstream>
#include<vector>
using namespace std;
	long gcd(	long  m,	long n)
{
	if(n==0)
		return m;
	else
		return gcd(n,m%n);
}
int main()
{
	ifstream infile("C:\\Users\\qingpingw\\Desktop\\B-small-attempt3.in");
	ofstream outfile("C:\\Users\\qingpingw\\Desktop\\B-small3.txt");
	int test;
	int N;
	int i,j;
	long   d;
	long  num[5];
	long temp;
	vector<long  > vi;
	infile>>test;
	int k=1;
	while(k<=test)
	{
		infile>>N;
		for(i=0;i<N;i++)
			infile>>num[i];
		for(i=0;i<N;i++)
			for(j=i+1;j<N;j++)
			{
				if(num[j]>num[i])
					vi.push_back(num[j]-num[i]);
				else
					vi.push_back(num[i]-num[j]);
			}
			
			d=vi[0];
			
			for(i=1;i<vi.size();i++)
				d=gcd(d,vi[i]);
			if(d==num[0])
				temp=0;
			else
				temp=d-num[0]%d;
			outfile<<"Case #"<<k<<": "<<temp <<endl;
			k++;
			vi.clear();
	}
	system("pause");
	return 0;
}


