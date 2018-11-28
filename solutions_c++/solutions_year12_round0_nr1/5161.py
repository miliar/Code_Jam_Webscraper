#include <cstdio>
#include <cstring>

int main() {
	char a[140];
	a['y'] = 'a';
	a['n'] = 'b';
	a['f'] = 'c';
	a['i'] = 'd';
	a['c'] = 'e';
	a['w'] = 'f';
	a['l'] = 'g';
	a['b'] = 'h';
	a['k'] = 'i';
	a['u'] = 'j';
	a['o'] = 'k';
	a['m'] = 'l';
	a['x'] = 'm';
	a['s'] = 'n';
	a['e'] = 'o';
	a['v'] = 'p';
	a['z'] = 'q';
	a['p'] = 'r';
	a['d'] = 's';
	a['r'] = 't';
	a['j'] = 'u';
	a['g'] = 'v';
	a['t'] = 'w';
	a['h'] = 'x';
	a['a'] = 'y';
	a['q'] = 'z';
	int t, T, l, i;
	char s[10000];
	scanf("%d\n", &T);
	for (t=1;t<=T;t++) {
		scanf("%[^\n]\n", s);
		printf("Case #%d: ", t);
		l = strlen(s);
		for (i=0;i<l;i++)
		if (s[i] == ' ') printf(" ");
		else printf("%c", s[i] = a[s[i]]);
		printf("\n");
	}
	return 0;
}