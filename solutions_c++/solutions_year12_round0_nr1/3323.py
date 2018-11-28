#include <cstdio>

char buf[128];

char a[120];
char b[120];

int main(int argc, char const *argv[])
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int j, n, s;
	buf[' '] = ' ';
buf['a'] = 'y';
buf['b'] = 'h';
buf['c'] = 'e';
buf['d'] = 's';
buf['e'] = 'o';
buf['f'] = 'c';
buf['g'] = 'v';
buf['h'] = 'x';
buf['i'] = 'd';
buf['j'] = 'u';
buf['k'] = 'i';
buf['l'] = 'g';
buf['m'] = 'l';
buf['n'] = 'b';
buf['o'] = 'k';
buf['p'] = 'r';
buf['r'] = 't';
buf['s'] = 'n';
buf['t'] = 'w';
buf['u'] = 'j';
buf['v'] = 'p';
buf['w'] = 'f';
buf['x'] = 'm';
buf['y'] = 'a';
//////////////////
buf['q'] = 'z';
buf['z'] = 'q';
	scanf("%d\n", &n);
	s = 0;
	while (s++ < n) {
		gets(a);
		j = 0;
		while(a[j]) {
			b[j] = buf[a[j]];
			j++;
		}
		b[j] = 0;
		printf("Case #%d: %s\n", s, b);
	}
	return 0;
}