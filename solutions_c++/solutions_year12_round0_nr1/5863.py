#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<set>
#include<fstream>
#include<queue>
#include<fstream>
#include<map>
#include<cstring>
#include<sstream>
#include<limits.h>
#include<climits>

using namespace std;

int main()
{
	ifstream cin("A-small-attempt0.in");
	ofstream cout("A-small-attempt0.out");

	map<char,char> m;
	int c='a';
	m[c++]='y';
	m[c++]='h';
	m[c++]='e';
	m[c++]='s';
	m[c++]='o';
	m[c++]='c';
	m[c++]='v';
	m[c++]='x';
	m[c++]='d';
	m[c++]='u';
	m[c++]='i';
	m[c++]='g';
	m[c++]='l';
	m[c++]='b';
	m[c++]='k';
	m[c++]='r';
	m[c++]='z';
	m[c++]='t';
	m[c++]='n';
	m[c++]='w';
	m[c++]='j';
	m[c++]='p';
	m[c++]='f';
	m[c++]='m';
	m[c++]='a';
	m[c++]='q';
	m[' ']=' ';

	int n;
	cin>>n;

	string x;
	getline(cin,x);
	for(int i=0;i<n;i++)
	{	
		getline(cin,x);
		for(int j=0;j<x.size();j++)
		{
			x[j]=m[x[j]];
		}

		cout<<"Case #"<<i+1<<": "<<x<<endl;
	}

	system("pause");
	return 0;
}


