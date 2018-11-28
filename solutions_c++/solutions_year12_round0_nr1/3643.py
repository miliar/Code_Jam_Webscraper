#include <cstdio>
#include <cstring>
#include <set>

using namespace std;

int main()
{
	int T;
	static char in[1000];

	scanf("%d\n",&T);

	static char m[600];

	m[' '] = ' ';
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
	m['q'] = 'z';
	m['r'] = 't';
	m['s'] = 'n';
	m['t'] = 'w';
	m['u'] = 'j';
	m['v'] = 'p';
	m['w'] = 'f';
	m['x'] = 'm';
	m['y'] = 'a';
	m['z'] = 'q';


	for (int c = 0; c < T; ++c) {
		printf("Case #%d:", c + 1);

		scanf("%[^\n]\n",in);

		int len = strlen(in);

		for (int i = 0; i < len; ++i) {
			in[i] = m[in[i]];
		}
		printf(" %s\n", in);

	}

	return 0;
}
