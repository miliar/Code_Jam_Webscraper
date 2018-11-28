#include <iostream>
#include <cstdio>

char conv[500];
char input[10000];
int N;
int main(void)
{
	int i;
	char ch;
	conv['a'] = 'y';
	conv['b'] = 'h';
	conv['c'] = 'e';
	conv['d'] = 's';
	conv['e'] = 'o';
	conv['f'] = 'c';
	conv['g'] = 'v';
	conv['h'] = 'x';
	conv['i'] = 'd';
	conv['j'] = 'u';
	conv['k'] = 'i';
	conv['l'] = 'g';
	conv['m'] = 'l';
	conv['n'] = 'b';
	conv['o'] = 'k';
	conv['p'] = 'r';
	conv['q'] = 'z';
	conv['r'] = 't';
	conv['s'] = 'n';
	conv['t'] = 'w';
	conv['u'] = 'j';
	conv['v'] = 'p';
	conv['w'] = 'f';
	conv['x'] = 'm';
	conv['y'] = 'a';
	conv['z'] = 'q';
	scanf("%d\n",&N);
	i=1;
	printf("Case #1: ");
	while(1)
	{
		if(scanf("%c",&ch)==EOF) break;
		if(ch=='\n')
		{
			i++;
			if(i<=N) printf("%cCase #%d: ",ch,i);
			else printf("\n");
			continue;
		}
		if(ch==' ')
		{
			printf(" ");
			continue;
		}
		printf("%c",conv[ch]);
	}
	return 0;
}
	
