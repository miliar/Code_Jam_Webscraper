#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <algorithm>
#include <hash_map>
#include <hash_set>

using namespace std;

#define FOR(i,n) for((i) = 0; (i) < (n); ++(i))

FILE *fi, *fo;

hash_map<char, char> M;

void mainImpl(int _c)
{
	char T[200];
	fgets(T, 200, fi);
	fprintf(fo, "Case #%d: ", _c);
	for(int i = 0; i < strlen(T); ++i)
	{
		if (T[i] >= 'a' && T[i] <= 'z') fprintf(fo, "%c", M[T[i]]);
		else if (T[i] >= 'A' && T[i] <= 'Z') fprintf(fo, "%c", M[T[i] - 'A' + 'a'] - 'a' + 'A');
		else fprintf(fo, "%c", T[i]);
	}
}


int main()
{
	fi = fopen("a.in", "rt");
	fo = fopen("a.out", "wt");

	int t, tt;
	fscanf(fi, "%d\n", &tt);

	M['a'] = 'y';
	M['b'] = 'h';
	M['c'] = 'e';
	M['d'] = 's';
	M['e'] = 'o';
	M['f'] = 'c';
	M['g'] = 'v';
	M['h'] = 'x';
	M['i'] = 'd';
	M['j'] = 'u';
	M['k'] = 'i';
	M['l'] = 'g';
	M['m'] = 'l';
	M['n'] = 'b';
	M['o'] = 'k';
	M['p'] = 'r';
	M['q'] = 'z';
	M['r'] = 't';
	M['s'] = 'n';
	M['t'] = 'w';
	M['u'] = 'j';
	M['v'] = 'p';
	M['w'] = 'f';
	M['x'] = 'm';
	M['y'] = 'a';
	M['z'] = 'q';

	FOR(t, tt) mainImpl(t + 1);

	fclose(fo);
	fclose(fi);
	return 0;
}