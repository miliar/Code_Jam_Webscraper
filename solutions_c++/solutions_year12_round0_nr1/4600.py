#include<cstdio>
#include<algorithm>
#include<cstring>
#define M 100020
using namespace std;
int trans[129];
char s[111];
int main()
{
	freopen("A-small-attempt0.in","r", stdin);
	freopen("A-small-attempt0.out","w", stdout);
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

	int t;
	scanf("%d",&t);
	gets(s);
	for(int o=1; o<=t; o++)
	{
		gets(s);
		printf("Case #%d: ",o);
		for(int i=0; i<strlen(s); i++)
			if(s[i]==' ')
				printf(" ");
			else
				printf("%c",trans[s[i]]);
		printf("\n");
	}
}
