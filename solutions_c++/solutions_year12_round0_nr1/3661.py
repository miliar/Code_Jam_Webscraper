#include <cstdio>
#include <iostream>
#include <map>
#include <fstream>

using namespace std;

FILE *in;

map<char,char> mp;
ifstream inn("A-small-attempt3.in");

void Prev()
{
	mp['a']='y';
	mp['b']='h';
	mp['c']='e';
	mp['d']='s';
	mp['e']='o';
	mp['f']='c';
	mp['g']='v';
	mp['h']='x';
	mp['i']='d';
	mp['j']='u';
	mp['k']='i';
	mp['l']='g';
	mp['m']='l';
	mp['n']='b';
	mp['o']='k';
	mp['p']='r';
	mp['q']='z';
	mp['r']='t';
	mp['s']='n';
	mp['t']='w';
	mp['u']='j';
	mp['v']='p';
	mp['w']='f';
	mp['x']='m';
	mp['y']='a';
	mp['z']='q';

}


int main()
{
	int N,n,i,j;
	string s;
	Prev();
	freopen("A-small-attempt3.out","w",stdout);
	inn >> N;
	for(i=0;i<=N;i++)
	{
		s="";
		getline(inn,s);
		n=s.size();
		if(!i) continue;
		cout << "Case #" << i << ": ";
		for(j=0;j<n;j++) if(s[j] == ' ') cout << ' '; else cout << mp[s[j]]; cout << endl;
	}
	return 0;
}
