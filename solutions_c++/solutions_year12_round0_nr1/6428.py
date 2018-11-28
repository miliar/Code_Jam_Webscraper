#include <map>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	map <char, char> a;
	a['a'] = 'y';
	a['b'] = 'h';
	a['c'] = 'e';
	a['d'] = 's';
	a['e'] = 'o';
	a['f'] = 'c';
	a['g'] = 'v';
	a['h'] = 'x';
	a['i'] = 'd';
	a['j'] = 'u';
	a['k'] = 'i';
	a['l'] = 'g';
	a['m'] = 'l';
	a['n'] = 'b';
	a['o'] = 'k';
	a['p'] = 'r';
	a['q'] = 'z';
	a['r'] = 't';
	a['s'] = 'n';
	a['t'] = 'w';
	a['u'] = 'j';
	a['v'] = 'p';
	a['w'] = 'f';
	a['x'] = 'm';
	a['y'] = 'a';
	a['z'] = 'q';
	a[' '] = ' ';
	int n;
	cin >> n;
	string s;
	for (int i = 0;  i < n+1; i++){
		if (!i){
			getline(cin,s);
			continue;
		}
		cout << "Case #" << i << ": ";
		getline(cin,s);
		for (int j = 0; j < s.length(); j++){
			cout << a[s[j]];
		}
		cout << endl;
	}
	return 0;
}
