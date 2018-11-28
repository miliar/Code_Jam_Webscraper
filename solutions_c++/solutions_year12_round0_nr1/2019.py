#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <memory.h>

int main(int argc, char **argv) {

	int nbTests;
	char dico[256];
	char in[101], out[101];

	dico['y']='a'; dico['n']='b'; dico['f']='c';
	dico['i']='d'; dico['c']='e'; dico['w']='f';
	dico['l']='g'; dico['b']='h'; dico['k']='i';
	dico['u']='j'; dico['o']='k'; dico['m']='l';
	dico['x']='m'; dico['s']='n'; dico['e']='o';
	dico['v']='p'; dico['z']='q'; dico['p']='r';
	dico['d']='s'; dico['r']='t'; dico['j']='u';
	dico['g']='v'; dico['t']='w'; dico['h']='x';
	dico['a']='y'; dico['q']='z'; dico[' ']=' ';

	scanf("%d", &nbTests);
	char dump;
	std::cin.getline(&dump, 1);

	for(int n=1; n<=nbTests; ++n) {
		memset(in, 0, sizeof(in));
		memset(out, 0, sizeof(out));

		std::cin.getline(in, 101);

		for(int i=0; i<strlen(in); ++i) {
			out[i] = dico[in[i]];
		}

		printf("Case #%d: %s\n", n, out);
	}

	return 0;
}