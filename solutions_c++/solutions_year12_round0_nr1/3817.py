#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<cctype>
#include<map>
#include<fstream>

using namespace std;

int main()
{
	map <char,char> st;
	st['y']='a';
	st['n']='b';
	st['f']='c';
	st['i']='d';
	st['c']='e';
	st['w']='f';
	st['l']='g';
	st['b']='h';
	st['k']='i';
	st['u']='j';
	st['o']='k';
	st['m']='l';
	st['x']='m';
	st['s']='n';
	st['e']='o';
	st['v']='p';
	st['z']='q';
	st['p']='r';
	st['d']='s';
	st['r']='t';
	st['j']='u';
	st['g']='v';
	st['t']='w';
	st['h']='x';
	st['a']='y';
	st['q']='z';
	st[' ']=' ';
	int T;
	cin>>T;
	cin.get();
	int P=T;
	ofstream fout("out.txt");
	while(T--){
		string s;
		getline(cin,s);
		for(int i=0;i<s.size();i++)
			s[i]=st[s[i]];	  
		fout<<"Case #"<<P-T<<": "<<s<<endl;
	}	 
	return 0;
}

