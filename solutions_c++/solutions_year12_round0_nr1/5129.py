#include <stdio.h>
#include <iostream>
#include <sstream>
#include <map>

using namespace std;

int main(){
	map<char,char> lookup;
	map<char,char>::iterator it;
	int c;
	lookup[' ']=' ';
	lookup['a']='y';
	lookup['b']='h';
	lookup['c']='e';
	lookup['d']='s';
	lookup['e']='o';
	lookup['f']='c';
	lookup['g']='v';
	lookup['h']='x';
	lookup['i']='d';
	lookup['j']='u';
	lookup['k']='i';
	lookup['l']='g';
	lookup['m']='l';
	lookup['n']='b';
	lookup['o']='k';
	lookup['p']='r';
	lookup['q']='z';
	lookup['r']='t';
	lookup['s']='n';
	lookup['t']='w';
	lookup['u']='j';
	lookup['v']='p';
	lookup['w']='f';
	lookup['x']='m';
	lookup['y']='a';
	lookup['z']='q';
	cin >> c;
	cin.ignore();
	for(int i=1;i<=c;i++){
		string s,t;
		stringstream ss;
		ss << "Case #" << i << ": ";
		t = ss.str();
		getline(cin, s, '\n');
		for(int k=0;k<s.length();k++){
			t = t+(lookup.find(s[k])->second);
		}
		cout << t << endl;
	}
	return 0;
}
