#include <iostream>

using namespace std;

int main(){
	char A[200];
	A['a'] = 'y';
	A['b'] = 'h';
	A['c'] = 'e';
	A['d'] = 's';
	A['e'] = 'o';
	A['f'] = 'c';
	A['g'] = 'v';
	A['h'] = 'x';
	A['i'] = 'd';
	A['j'] = 'u';
	A['k'] = 'i';
	A['l'] = 'g';
	A['m'] = 'l';
	A['n'] = 'b';
	A['o'] = 'k';
	A['p'] = 'r';
	A['q'] = 'z';
	A['r'] = 't';
	A['s'] = 'n';
	A['t'] = 'w';
	A['u'] = 'j';
	A['v'] = 'p';
	A['w'] = 'f';
	A['x'] = 'm';
	A['y'] = 'a';
	A['z'] = 'q';
	A[' '] = ' ';
	int nt;
	cin>>nt;
	string s;
	getline(cin, s);
	for (int i = 1; i <= nt; i++){
		getline(cin, s);
		cout<<"Case #"<<i<<": ";
		for (int j = 0; j < s.length(); j++) cout<<A[s[j]];
		cout<<endl;
	}
	return 0;
}
