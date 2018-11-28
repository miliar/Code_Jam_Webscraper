#include<iostream>
#include<map>
#include<cstdio>
using namespace std;
map<char,char> M;
void Map()
{
		M['a']='y';
		M['b']='h';
		M['c']='e';
		M['d']='s';
		M['e']='o';
		M['f']='c';
		M['g']='v';
		M['h']='x';
		M['i']='d';
		M['j']='u';
		M['k']='i';
		M['l']='g';
		M['m']='l';
		M['n']='b';
		M['o']='k';
		M['p']='r';
		M['q']='z';
		M['r']='t';
		M['s']='n';
		M['t']='w';
		M['u']='j';
		M['v']='p';
		M['x']='m';
		M['w']='f';
		M['y']='a';
		M['z']='q';
		M[' ']=' ';
}
void readNsolve()
{
		int i,j,N;
		string s;
		cin>>N;
		getline(cin,s);
		for(i=1;i<=N;i++)
		{
				getline(cin,s);
				cout<<"Case #"<<i<<": ";
				for(j=0;j<s.length();j++)
						cout<<M[s[j]];
				cout<<endl;
		}
}
int main()
{
		Map();
		readNsolve();
}
