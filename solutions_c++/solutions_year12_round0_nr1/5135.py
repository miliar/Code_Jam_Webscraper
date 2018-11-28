#include <cstdio>

using namespace std;

char g[111],s[111];
char trans[256];

int f()
{
	trans[' '] = ' ';
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
	return 0;
}

int main()
{
	int t;
	scanf("%d%*c",&t);
	f();
	for(int j=1; j<=t; j++ )
	{
		scanf("%[^\n]s",g);
		for( int i=0; g[i]; i++ )
		{
			s[i]   = trans[ g[i] ];
			s[i+1] = 0;
		}
		scanf("%*c");
		printf("Case #%d: %s\n",j,s);
	}
	return 0;
}

