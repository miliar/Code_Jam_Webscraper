#include<iostream>
#include<fstream>
using namespace std;

void main()
{
	int t,flag;
	char c[51][51];
	int r,cl;
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("output2.txt");
	fin>>t;
    for(int ti=1;ti<=t;ti++)
	{
		flag=0;
	fin>>r>>cl;
	for(int i=0;i<r;i++)
	{
		fin>>c[i];
	}
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<cl;j++)
		{
			if(c[i][j]=='#')
			{
				if(c[i][j+1]=='#' && c[i+1][j]=='#' && c[i+1][j+1]=='#')
				{
					c[i][j]='/';
				    c[i][j+1]='\\';
					c[i+1][j]='\\';
					c[i+1][j+1]='/';
					flag=0;
				}
				else
				{
					flag=-1;
					goto l;
				}
				
			}
		}
	}
l:
	if(flag==-1)
		fout<<"Case #"<<ti<<":\nImpossible\n";
	else 
	{
		fout<<"Case #"<<ti<<":\n";
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<cl;j++)
				fout<<c[i][j];
			fout<<"\n";
		}
		fout<<"\n";
	}
}
}
