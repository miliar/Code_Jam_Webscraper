#include <iostream>
#include <string>
using namespace std;
int main() {
	int t, i, n, j;
	cin>>t;
	string s[t];
	i = 0;
	char swp[int('z')+1];
	swp['a'] = 'y';
	swp['b'] = 'h';
	swp['c'] = 'e';
	swp['d'] = 's';
	swp['e'] = 'o';
	swp['f'] = 'c';
	swp['g'] = 'v';
	swp['h'] = 'x';
	swp['i'] = 'd';
	swp['j'] = 'u';
	swp['k'] = 'i';
	swp['l'] = 'g';
	swp['m'] = 'l';
	swp['n'] = 'b';
	swp['o'] = 'k';
	swp['p'] = 'r';
	swp['q'] = 'z';
	swp['r'] = 't';
	swp['s'] = 'n';
	swp['t'] = 'w';
	swp['u'] = 'j';
	swp['v'] = 'p';
	swp['w'] = 'f';
	swp['x'] = 'm';
	swp['y'] = 'a';
	swp['z'] = 'q';
	
	getline(cin, s[0]);
	
	while(i < t) {
		getline(cin, s[i]);
		j = 0;
		while(j < s[i].length()) {
			if(s[i][j] != ' ')
				s[i][j] = swp[int(s[i][j])];
			j++;
		}
		i++;
	}
	i = 0;
	while(i < t) {
		cout<<"Case #"<<i+1<<": "<<s[i]<<endl;
		i++;
	}
}
