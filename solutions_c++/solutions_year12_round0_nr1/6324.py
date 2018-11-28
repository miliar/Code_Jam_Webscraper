#include <cstdio>
#include <cstring>

using namespace std;

char table[200];
char line[200];

int main(void) {

table['a'] = 'y';
table['b'] = 'h';
table['c'] = 'e';
table['d'] = 's';
table['e'] = 'o';
table['f'] = 'c';
table['g'] = 'v';
table['h'] = 'x';
table['i'] = 'd';
table['j'] = 'u';
table['k'] = 'i';
table['l'] = 'g';
table['m'] = 'l';
table['n'] = 'b';
table['o'] = 'k';
table['p'] = 'r';
table['q'] = 'z';
table['r'] = 't';
table['s'] = 'n';
table['t'] = 'w';
table['u'] = 'j';
table['v'] = 'p';
table['w'] = 'f';
table['x'] = 'm';
table['y'] = 'a';
table['z'] = 'q';

	int n;
	scanf("%d\n", &n);
	
	for(int i = 1; i <= n; ++i) {
		gets(line);
		printf("Case #%d: ", i);
		for(int j = 0; j < strlen(line); ++j) {
			if(line[j] < 'a' || line[j] > 'z') printf("%c", line[j]); else
				printf("%c", table[line[j]]);
		}
		printf("\n");
	}

    return 0;

}
