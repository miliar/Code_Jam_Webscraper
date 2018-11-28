
#include <cstring>
#include <iostream>
#include <map>

using namespace std;

map<char, char> rb;
int main() {
	rb['a']='y';
	rb['b']='h';
	rb['c']='e';
	rb['d']='s';
	rb['e']='o';
	rb['f']='c';
	rb['g']='v';
	rb['h']='x';
	rb['i']='d';
	rb['j']='u';
	rb['k']='i';
	rb['l']='g';
	rb['m']='l';
	rb['n']='b';
	rb['o']='k';
	rb['p']='r';
	rb['q']='z';
	rb['r']='t';
	rb['s']='n';
	rb['t']='w';
	rb['u']='j';
	rb['v']='p';
	rb['w']='f';
	rb['x']='m';
	rb['y']='a';
	rb['z']='q';
	rb[' ']=' ';
	int t;
	cin>>t;
	char c[100+10];
	cin.getline(c, 1);
	for (int i=0; i<t; ++i) {
		cin.getline(c, 100+5);
		cout<<"Case #"<<i+1<<": ";
		for (int i=0; i<strlen(c); ++i)
			cout<<rb[c[i]];
		cout<<endl;
	}
	return 0;
}
