#include <iostream>
#include <string>
#include <map>
using namespace std;

int main(){
	int n;
	cin >> n;
	map<char,char> m;
	m['a'] = 'y';
	m['b'] = 'h';
	m['c'] = 'e';
	m['d'] = 's';
	m['e'] = 'o';
	m['f'] = 'c';
	m['g'] = 'v';
	m['h'] = 'x';
	m['i'] = 'd';
	m['j'] = 'u';
	m['k'] = 'i';
	m['l'] = 'g';
	m['m'] = 'l';
	m['n'] = 'b';
	m['o'] = 'k';
	m['p'] = 'r';
	m['q'] = 'z'; //
	m['r'] = 't';
	m['s'] = 'n';
	m['t'] = 'w';
	m['u'] = 'j';
	m['v'] = 'p';
	m['w'] = 'f';
	m['x'] = 'm';
	m['y'] = 'a';
	m['z'] = 'q';//

	string str;
	getline(cin,str);
	for(int t=1;t<=n;t++){
		string str;
		getline(cin,str);
		for(int i=0;i<str.size();i++){
			if(str[i] >= 'a' && str[i] <= 'z') str[i] = m[str[i]];
		}
		cout << "Case #" << t << ": " << str << endl;
	}
	return 0;
}