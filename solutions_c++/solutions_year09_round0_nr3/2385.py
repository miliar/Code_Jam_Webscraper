#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int n,i,j,k;
string st,s;
int f[500][19];
ifstream fin("input.txt");
ofstream fout("output.txt");
int main()
{
	fin>>n;
	getline(fin,s);
	st="welcome to code jam";
	for (i=0;i<n;i++)
	{
		getline(fin,s);
		for (j=0;j<500;j++)
			for (k=0;k<19;k++)
				f[j][k]=0;
		if (s[0]==st[0])
			f[0][0]=1;
		for (j=1;j<s.length();j++)
			if (s[j]==st[0])
				f[j][0]=(f[j-1][0]+1)%10000;
			else
				f[j][0]=f[j-1][0];
		for (k=1;k<19;k++)
			for (j=1;j<s.length();j++)
				if (s[j]==st[k])
					f[j][k]=(f[j-1][k]+f[j-1][k-1])%10000;
				else 
					f[j][k]=f[j-1][k];
		fout<<"Case #"<<i+1<<": ";
		if (f[s.length()-1][18]<1000)
			fout<<'0';
		if (f[s.length()-1][18]<100)
			fout<<'0';
		if (f[s.length()-1][18]<10)
			fout<<'0';
		fout<<f[s.length()-1][18]<<endl;
	}
	return 0;
}