#include <iostream>
#include <string>
using std::cin;
using std::cout;
using std::string;
int n;
char map[200];
string s;
int main(){
	cin >> n;
	getline(cin,s);
	map[' ']=' ';
	map['a']='y';
	map['b']='h';
	map['c']='e';
	map['d']='s';
	map['e']='o';
	map['f']='c';
	map['g']='v';
	map['h']='x';
	map['i']='d';
	map['j']='u';
	map['k']='i';
	map['l']='g';
	map['m']='l';
	map['n']='b';
	map['o']='k';
	map['p']='r';
	map['q']='z';
	map['r']='t';
	map['s']='n';
	map['t']='w';
	map['u']='j';
	map['v']='p';
	map['w']='f';
	map['x']='m';
	map['y']='a';
	map['z']='q';
	for(int i=0;i<n;++i){
		getline(cin,s);
		cout << "Case #" << (i+1) <<": ";
		for(string::iterator j=s.begin();j!=s.end();++j) cout << map[*j];
		cout << "\n";
	}
	return 0;
}