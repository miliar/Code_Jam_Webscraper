#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
	char trans[128] = {0};
	trans[' '] = ' ';
	trans['\n'] = '\n';
	trans['a'] = 'y';
	trans['b'] = 'h';
	trans['c'] = 'e';
	trans['d'] = 's';
	trans['e'] = 'o';
	trans['f'] = 'c';
	trans['g'] = 'v';
	trans['h'] = 'x';
	trans['i'] = 'd';
	trans['j'] = 'u';
	trans['k'] = 'i';
	trans['l'] = 'g';
	trans['m'] = 'l';
	trans['n'] = 'b';
	trans['o'] = 'k';
	trans['p'] = 'r';
	trans['q'] = 'z';
	trans['r'] = 't';
	trans['s'] = 'n';
	trans['t'] = 'w';
	trans['u'] = 'j';
	trans['v'] = 'p';
	trans['w'] = 'f';
	trans['x'] = 'm';
	trans['y'] = 'a';
	trans['z'] = 'q';

	int T,t;
	scanf("%d", &T);
	char buffer[110];
	char out[110];
	
	fgets(buffer, 110, stdin);
	
	for(t = 1; t <= T; t++)
	{
		fgets(buffer, 110, stdin);
		int len = strlen(buffer);
		for(int i = 0; i <= len; i++)
		{
			out[i] = trans[ buffer[i]];
		}
		printf("Case #%d: %s", t, out);
	}
}
