
	#include <cstdlib>
	#include <cstdio>

	using namespace std;

	char f[26];

	int rep(char x, char y)
	{
		f[y - 'a'] = x;
	}

	int main()
	{
		rep('a', 'y');		rep('b', 'n');		rep('c', 'f');		rep('d', 'i');		rep('e', 'c');		rep('f', 'w');		rep('g', 'l');
		rep('h', 'b');		rep('i', 'k');		rep('j', 'u');		rep('k', 'o');		rep('l', 'm');		rep('m', 'x');		rep('n', 's');
		rep('o', 'e');		rep('p', 'v');		rep('q', 'z');		rep('r', 'p');		rep('s', 'd');		rep('t', 'r');
		rep('u', 'j');		rep('v', 'g');		rep('w', 't');		rep('x', 'h');		rep('y', 'a');		rep('z', 'q');
		freopen("a.in", "r", stdin);
		freopen("a.out", "w", stdout);
		int t;
		scanf("%d\n", &t);
		for (int i = 1; i <= t; i ++)
		{
			printf("Case #%d: ", i);
			while (1)
			{
				char c = getchar();
				if (c == '\n')
					break;
				if (c <= 'z' && c >= 'a')	printf("%c", f[c - 'a']);
				else	printf("%c", c);
			}
			printf("\n");
		}
		return 0;
	}

/*
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv

our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
*/
