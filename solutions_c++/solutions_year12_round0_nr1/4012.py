#include <fstream>
#include <iostream>
using namespace std;

char map[26], s[200];
int n;

int main() {
map['a' - 'a'] = 'y';
map['b' - 'a'] = 'h';
map['c' - 'a'] = 'e';
map['d' - 'a'] = 's';
map['e' - 'a'] = 'o';
map['f' - 'a'] = 'c';
map['g' - 'a'] = 'v';
map['h' - 'a'] = 'x';
map['i' - 'a'] = 'd';
map['j' - 'a'] = 'u';
map['k' - 'a'] = 'i';
map['l' - 'a'] = 'g';
map['m' - 'a'] = 'l';
map['n' - 'a'] = 'b';
map['o' - 'a'] = 'k';
map['p' - 'a'] = 'r';
map['q' - 'a'] = 'z';
map['r' - 'a'] = 't';
map['s' - 'a'] = 'n';
map['t' - 'a'] = 'w';
map['u' - 'a'] = 'j';
map['v' - 'a'] = 'p';
map['w' - 'a'] = 'f';
map['x' - 'a'] = 'm';
map['y' - 'a'] = 'a';
map['z' - 'a'] = 'q';

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	scanf("%d\n", &n);
	for (int i = 0; i < n; ++i) {
		gets(s);
		for (int j = 0; s[j]; ++j)
			if (s[j] >= 'a' && s[j] <= 'z')
				s[j] = map[s[j] - 'a'];
		printf("Case #%d: %s\n", i + 1, s);
	}
	
	return 0;
}
