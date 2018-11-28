#include <iostream>
#include <map>

using namespace std;

FILE *f = fopen("input.in", "r");
FILE *g = fopen("output.out", "w");

int N;
char sir[200];

map<char, char> m;
map<char, char>::iterator it;

int main()
{
	m['q'] = 'z';
	m['w'] = 'f';
	m['e'] = 'o';
	m['r'] = 't';
	m['t'] = 'w';
	m['y'] = 'a';
	m['u'] = 'j';
	m['i'] = 'd';
	m['o'] = 'k';
	m['p'] = 'r';
	m['l'] = 'g';
	m['k'] = 'i';
	m['j'] = 'u';
	m['h'] = 'x';
	m['g'] = 'v';
	m['f'] = 'c';
	m['d'] = 's';
	m['s'] = 'n';
	m['a'] = 'y';
	m['z'] = 'q';
	m['x'] = 'm';
	m['c'] = 'e';
	m['v'] = 'p';
	m['b'] = 'h';
	m['n'] = 'b';
	m['m'] = 'l';
	m[' '] = ' ';
	m['\n'] = '\n';

	fscanf(f, "%d\n", &N);
	for (int i = 0; i < N; ++i)
	{
		fgets(sir, 200, f);
		int p = strlen(sir);
		for (int j = 0; j < p; ++j)
		{
			it = m.find(sir[j]);
			sir[j] = it->second;
		}
		fprintf(g, "Case #%d: %s", i + 1, sir);
	}

	fclose(g);
	fclose(f);

	return 0;
}