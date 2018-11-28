// Test.cpp : 定义控制台应用程序的入口点。
//
#include <iostream>
#include <fstream>
#include <map>
#include <string>

using namespace std;

int charInString(char c, string str)
{
	for(int i=0; i < str.length(); ++i)
	{
		if(c == str[i])
		{
			return 1;
		}
	}
	return 0;
}
int getMatch(string str, map<string, int> wordTable, int L)
{
	int mtN = 0;
	string ss = "";
	int t=0;
	for(int i = 0; i< str.length(); ++i)
	{
		if(str[i] == '(')
		{
			i++;
			while(str[i]!= ')')
			{
				ss += str[i];
				i++;
			}
		}
		else
		{
			ss += str[i];
		}

		for(map<string,int>::iterator it = wordTable.begin(); it != wordTable.end(); it++)
		{
			if(charInString(it->first[t],ss))
			{
				it->second ++;
			}
		}
		ss = "";
		t++;
	}
	for(map<string,int>::iterator it = wordTable.begin(); it != wordTable.end(); it++)
	{
		if(it->second == L)
		{
			mtN++;
		}
	}
	return mtN;
}

int main()
{
	int L, D, N;
	map <string,int> wordTable;
	string str = "";
	int d;
	int n;
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	fin>>L>>D>>N;
	//cout<<L;
	d=D;
	while(d--)
	{
		fin>>str;
		wordTable[str] = 0;		
	}
		
	for(n=1;n<=N; ++n)
	{
		fin>>str;
		fout<<"Case #"<<n<<": "<<getMatch(str, wordTable,L)<<endl;
	}

		L=D=N=0;


	return 0;
}