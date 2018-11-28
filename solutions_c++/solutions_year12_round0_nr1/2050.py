#include <cstdio>

char mapp[128], input[128];

int main() {
	int test, cs, i;
	mapp[' '] = ' '; mapp['a'] = 'y'; mapp['b'] = 'h';
	mapp['c'] = 'e'; mapp['d'] = 's'; mapp['e'] = 'o';
	mapp['f'] = 'c'; mapp['g'] = 'v'; mapp['h'] = 'x';
	mapp['i'] = 'd'; mapp['j'] = 'u'; mapp['k'] = 'i';
	mapp['l'] = 'g'; mapp['m'] = 'l'; mapp['n'] = 'b';
	mapp['o'] = 'k'; mapp['p'] = 'r'; mapp['q'] = 'z';
	mapp['r'] = 't'; mapp['s'] = 'n'; mapp['t'] = 'w';
	mapp['u'] = 'j'; mapp['v'] = 'p'; mapp['w'] = 'f';
	mapp['x'] = 'm'; mapp['y'] = 'a'; mapp['z'] = 'q';
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	scanf("%d", &test);
	fgets(input, 127, stdin);
	for(cs = 1; cs <= test; cs++) {
		fgets(input, 127, stdin);
		for(i = 0; input[i] >= 32; i++) {
			input[i] = mapp[input[i]];
		}
		input[i] = 0;
		printf("Case #%d: %s\n", cs, input);
	}
	return 0;
}