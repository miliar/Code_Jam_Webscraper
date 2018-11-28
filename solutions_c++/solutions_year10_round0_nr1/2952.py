#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
int main()
{
	long long int t=0,a=0,b=0,i=0,m=1;
	ifstream fin("A-large.in");
	ofstream fout("outputlong.in");
	fin>>t;
	for(i=1;i<=t;i++)
	{
		fin>>a>>b;
		b++;
		m=pow(2,a);
		fout<<"Case #"<<i<<": ";
		if(b%m==0&&b>0) fout<<"ON"<<"\n";
		else fout<<"OFF"<<"\n";
	}
	return 0;
}
