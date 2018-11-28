#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <set>
#include <vector>
#include <map>
using namespace std;

int main()
{
	char m[255];
	ifstream cin("input.txt");
	ofstream cout("out.txt");
	m[' ']=' ';
	m['y']='a';//
	m['n']='b';//
	m['f']='c';//
	m['i']='d';//
	m['c']='e';//
	m['w']='f';//
	m['l']='g';//
	m['b']='h';//
	m['k']='i';//
	m['u']='j';//
	m['o']='k';//
	m['m']='l';//
	m['x']='m';//
	m['s']='n';//
	m['e']='o';//
	m['v']='p';//

	m['z']='q';//

	m['p']='r';//
	m['d']='s';//
	m['r']='t';//
	m['j']='u';//
	m['g']='v';//
	m['t']='w';//
	m['h']='x';//
	m['a']='y';//
	m['q']='z';//
	int T,Ti,i=0;
	char t[1001];
	cin>>T;
	cin.get();
	for(Ti=1;Ti<=T;Ti++)
	{
		cout<<"Case #"<<Ti<<": ";
		cin.getline(t,1001);
		for(i=0;i<strlen(t);i++)
			cout<<m[t[i]];
		cout<<'\n';
	}

}