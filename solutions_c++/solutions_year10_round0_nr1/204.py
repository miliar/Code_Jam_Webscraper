#include<iostream>
#include<fstream>
using namespace std;

int a[32],t,n,k,s;
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("A-large.out");

	a[0]=1;
	for (int i=1;i<=31;i++)
		a[i]=a[i-1]*2;
	fin>>t;
	for (int i=1;i<=t;i++)
	{
		fout<<"Case #"<<i<<": ";
		fin>>n>>k;
		s=(k%a[n]);
		if (s==a[n]-1) fout<<"ON"<<endl; 
		else fout<<"OFF"<<endl;
	}
	fout.close();
	//system("pause");
	return 0;
}
