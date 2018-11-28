/*
ID: aditya21
PROG: calfflac
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;
vector<string> tokenize(string str, int a);
bool matched1(string str, vector<string> table);

int main() 
{
	ifstream fin ("d:\\io\\A-large.in");
	ofstream fout ("d:\\io\\A-large.out");

	int a, b, c;
	int i, j, k;
	int p, q, r, x, y, z;

	int cost,max;
	string str1,str2;
	char str[82];
	vector<int> inp,inp2;
	vector<string> posb,table;
	 

	fin>>a>>b>>c;
	cout<<a<<b<<c;
	for(i=0; i<b; i++)
	{
		fin>>str2;
		table.push_back(str2);
	}
	
	for(i=0; i<c; i++)
	{
		fout<<"Case #"<<(i+1)<<": ";
		cout<<"Case #"<<(i+1)<<": ";
		fin>>str2;
		p =0;
		posb.clear();
		posb = tokenize(str2,a);
		k = table.size();

		for(j=0; j<k; j++)
		{
			if(matched1(table[j], posb))
				p++;
		}
		fout<<p<<endl;
	}

	return 0;
}

vector<string> tokenize(string str, int a)
{
	int i,j,p,q,r;
	vector<string> result;
	string str2;
	j = str.size();
	r =0;

	for(i=0;i<j;i++)
	{
		if(str[i] == '(')
		{
			p = i+1;
			r=1;
		}
		else if(str[i] == ')')
		{
			str2 = str.substr(p,i-p);
			result.push_back(str2);
			r = 0;
		}
		else if(r == 0)
		{
			str2 = str.substr(i,1);
			result.push_back(str2);
		}
	}
	return result;
}

bool matched1(string str, vector<string> table)
{
	int i,j,k;
	k = str.size();
	for(i=0;i<k; i++)
	{
		if(table[i].find(str[i])== string::npos)
			return false;
	}
	return true;
}