#include <cstdio>
#include <cstring>

using namespace std;

char hash[256];

void init() {
	hash['a'] = 'y';
	hash['b'] = 'h';
	hash['c'] = 'e';
	hash['d'] = 's';
	hash['e'] = 'o';
	hash['f'] = 'c';
	hash['g'] = 'v';
	hash['h'] = 'x';
	hash['i'] = 'd';
	hash['j'] = 'u';
	hash['k'] = 'i';
	hash['l'] = 'g';
	hash['m'] = 'l';
	hash['n'] = 'b';
	hash['o'] = 'k';
	hash['p'] = 'r';
	hash['q'] = 'z';
	hash['r'] = 't';
	hash['s'] = 'n';
	hash['t'] = 'w';
	hash['u'] = 'j';
	hash['v'] = 'p';
	hash['w'] = 'f';
	hash['x'] = 'm';
	hash['y'] = 'a';
	hash['z'] = 'q';
}

int main() {
	init();

	int T; scanf("%d\n", &T);
	for (int i = 1; i <= T; i++) {
		char line[300]; fgets(line, 300, stdin);
		int ll = strlen(line);

		printf("Case #%d: ", i);
		for (int j = 0; j < ll; j++)
			if (line[j] >= 'a' && line[j] <= 'z') {
				int k = hash[line[j]];
				putchar(hash[line[j]]);
			} else {
				putchar(line[j]);
			}
	}

	return 0;
}
