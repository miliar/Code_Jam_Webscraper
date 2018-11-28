#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("o.txt");

int main()
{
	int t,i,j,n,s,p;
	fin>>t;
	for(j=1; j<=t; ++j)
	{
		fout<<"Case #"<<j<<": ";
		int k =0;
		fin>>n>>s>>p;
		int okP = 3*p - 2;
		int spP = 3*p - 4;
		if(p == 0 || p == 1)
			okP = spP = p;
		int l;
		for(i=0; i<n; ++i)
		{
			fin>>l;
			if(l>=okP)
				++k;
			else if(l>=spP && s)
			{
				--s;
				++k;
			}
		}
		fout<<k<<endl;
	}
	return 0;
}