#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;


int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("D://a.in");
	fout.open("D://output.txt");
	unsigned long c,N,sum,n;
	unsigned long K;

	fin>>c;
	for(unsigned long count=1;count<=c;count++)
	{
		fin>>N>>K;
		sum=0;
		n=2;
		for(unsigned long i=1;i<N;i++)
			n*=2;
		n--;
		for(unsigned long i=0;i<K;i++)
		{
			if(sum==n)
				sum=0;
			else
				sum++;
		}

		if(sum==n)
		{
			cout<<"Case #"<<count<<":ON"<<endl;
			fout<<"Case #"<<count<<":ON"<<endl;
		}
		else
		{
			cout<<"Case #"<<count<<":OFF"<<endl;
			fout<<"Case #"<<count<<":OFF"<<endl;
		}
	}
	cin.get();
	cin.get();
	return 0;
}