#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int t;
	int n,k;
	int i;
	int s[31];
	for(i=1;i<=30;i++)
		s[i]=1<<i;
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	fin>>t;
	for(i=1;i<=t;i++)
	{
		fin>>n>>k;
		fout<<"Case #"<<i<<": ";
		if((k+1)%s[n])
			fout<<"OFF"<<endl;
		else fout<<"ON"<<endl;
	}
	return 0;
}
