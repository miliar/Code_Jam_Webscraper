#include <iostream>
#include <map>
#include <cstdlib>
using namespace std;

int main(){
	map<char,char> a;
	a['a']='y';
	a['b']='h';
	a['c']='e';
	a['d']='s';
	a['e']='o';
	a['f']='c';
	a['g']='v';
	a['h']='x';
	a['i']='d';
	a['j']='u';
	a['k']='i';
	a['l']='g';
	a['m']='l';
	a['n']='b';
	a['o']='k';
	a['p']='r';
	a['q']='z';
	a['r']='t';
	a['s']='n';
	a['t']='w';
	a['u']='j';
	a['v']='p';
	a['w']='f';
	a['x']='m';
	a['y']='a';
	a['z']='q';
	a[' ']=' ';
	int T;
	string line;
	getline(cin,line);
	T=atoi(line.c_str());
	for(int i=0;i<T;i++){
		getline(cin,line);
		cout<<"Case #"<<i+1<<": ";
		for(int i=0;i<line.length();i++){
			cout<<a[line[i]];
		}
		cout<<endl;
	}
	return 0;
}
