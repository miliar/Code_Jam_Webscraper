#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
int main()
{
	long long int ti=0,x=0,y=0,i=0,m=1;
	ifstream fin("A-large.in");
	ofstream fout("outputlong.in");
	fin>>ti;
	for(i=1;i<=ti;i++)
	{
		fin>>x>>y;
		y++;
		m=pow(2,x);
		fout<<"Case #"<<i<<": ";
		if(y%m==0&&y>0) fout<<"ON"<<"\n";
		else fout<<"OFF"<<"\n";
	}
	return 0;
}
