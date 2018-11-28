#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
using namespace std;
int map[26];

int main()
{
	ifstream fin1("./sample");
	ifstream fin("./in");
	ofstream fout("./out");
	map['q'-'a']='z'-'a';
	map['e'-'a']='o'-'a';
	map['y'-'a']='a'-'a';
	map['z'-'a']='q'-'a';
	int n;
	fin1>>n;
	
	char temp[6][1000];
	fin1.getline(temp[0],10);
	for(int i=0;i<n*2;i++)
	{
		fin1.getline(temp[i],1000);
	}
	for(int i=0;i<n;i++)
	{
		cout<<temp[i]<<endl;
		int len=strlen(temp[i]);
		for(int j=0;j<len;j++)
		{
			if(temp[i][j]!=' ')
				map[temp[i][j]-'a']=temp[i+3][j]-'a';
		}
	}
	fin1.close();
	int m;
	fin>>m;
	char in[100000];
	fin.getline(in,10);
	for(int i=0;i<m;i++)
	{
		fin.getline(in,100000);
		int len=strlen(in);
		for(int j=0;j<len;j++)
		{
			if(in[j]!=' ')
				in[j]=char(map[in[j]-'a']+'a');
		}
		fout<<"Case #"<<i+1<<": "<<in<<endl;
	}
	fin.close();
	fout.close();
	return 1;
}
