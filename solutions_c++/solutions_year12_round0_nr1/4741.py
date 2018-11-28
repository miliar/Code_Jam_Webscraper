#include<stdio.h>


char s[105];
char a[256];

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("a.out", "w", stdout);
	for(int i = 0; i < 256; i++)
		a[i] = i;

	a['a'] = 'y';
	a['b'] = 'h';
	a['c'] = 'e';
	a['d'] = 's';
	a['e'] = 'o';
	a['f'] = 'c';
	a['g'] = 'v';
	a['h'] = 'x';
	a['i'] = 'd';
	a['j'] = 'u';
	a['k'] = 'i';
	a['l'] = 'g';
	a['m'] = 'l';
	a['n'] = 'b';
	a['o'] = 'k';
	a['p'] = 'r';
	a['q'] = 'z';
	a['r'] = 't';
	a['s'] = 'n';
	a['t'] = 'w';
	a['u'] = 'j';
	a['v'] = 'p';
	a['w'] = 'f';
	a['x'] = 'm';
	a['y'] = 'a';
	a['z'] = 'q';

	int t;
	scanf("%d ", &t);

	for(int tt = 0; tt < t; tt++)
	{
		gets(s);
		for(int i = 0; s[i]; i++)
			s[i] = a[s[i]];
		printf("Case #%d: %s\n", tt+1, s);
	}

	return 0;
}


/*
Input
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv


Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up


*/
/*
ejp mysljylc kd kxveddknmc re jsicpdrysi
our language is impossible to understand

rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
there are twenty six factorial possibilities

de kr kd eoya kw aej tysr re ujdr lkgc jv
so it is okay if you want to just give up

qvz
*/