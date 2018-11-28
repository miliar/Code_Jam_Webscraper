#include <iostream>
#include <cstring>

using namespace std;

char map[256];
char buff[123];

void init() {
	map[' '] = ' ';
	map['a'] = 'y';
	map['b'] = 'h';
	map['c'] = 'e';
	map['d'] = 's';
	map['e'] = 'o';
	map['f'] = 'c';
	map['g'] = 'v';
	map['h'] = 'x';
	map['i'] = 'd';
	map['j'] = 'u';
	map['k'] = 'i';
	map['l'] = 'g';
	map['m'] = 'l';
	map['n'] = 'b';
	map['o'] = 'k';
	map['p'] = 'r';
	map['q'] = 'z';
	map['r'] = 't';
	map['s'] = 'n';
	map['t'] = 'w';
	map['u'] = 'j';
	map['v'] = 'p';
	map['w'] = 'f';
	map['x'] = 'm';
	map['y'] = 'a';
	map['z'] = 'q';
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	init();
	int n;
	cin.getline(buff, 123);
	sscanf(buff, "%d", &n);
	for (int i=0; i<n; i++) {
		cout << "Case #" << i+1 << ": ";
		cin.getline(buff, 123);
		int len = strlen(buff);
		for (int j=0; j<len; j++) {
			buff[j] = map[buff[j]];
			cout<<buff[j];
		}
		cout << endl;
	}
	return 0;
}