#include<cstdio>
#include<cstring>

int T;
char s[500],a[10000];

int main()
{
	s[' '] = ' ';
	s['a'] = 'y';
	s['b'] = 'h';
	s['c'] = 'e';
	s['d'] = 's';
	s['e'] = 'o';
	s['f'] = 'c';
	s['g'] = 'v';
	s['h'] = 'x';
	s['i'] = 'd';
	s['j'] = 'u';
	s['k'] = 'i';
	s['l'] = 'g';
	s['m'] = 'l';
	s['n'] = 'b';
	s['o'] = 'k';
	s['p'] = 'r';
	s['q'] = 'z';
	s['r'] = 't';
	s['s'] = 'n';
	s['t'] = 'w';
	s['u'] = 'j';
	s['v'] = 'p';
	s['w'] = 'f';
	s['x'] = 'm';
	s['y'] = 'a';
	s['z'] = 'q';
	scanf("%d",&T);gets(a);
	for(int i = 0;i < T;i++)
	{
	    gets(a);
	    int len = strlen(a);
	    for(int i = 0;i < len;i++) a[i] = s[a[i]];
	    printf("Case #%d: ",i+1);puts(a);
	}
	return 0;
}
