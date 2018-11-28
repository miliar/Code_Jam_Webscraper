#include<iostream>
#include<queue>
#include<new>
#include<cstdio>
#include<algorithm>
#include<list>
#include<vector>
#include<map>
#include<utility>
#include<cstring>
#include<climits>
#include<cmath>
#include<stack>
using namespace std;

char a[200];
int main()
{
	a['e'] = 'o';
	a['j'] = 'u';
	a['p'] = 'r';
	a['m'] = 'l';
	a['y'] = 'a';
	a['s'] = 'n';
	a['l'] = 'g';
	a['c'] = 'e';
	a['k'] = 'i';
	a['d'] = 's';
	a['x'] = 'm';
	a['v'] = 'p';
	a['n'] = 'b';
	a['r'] = 't';
	a['i'] = 'd';
	a['b'] = 'h';
	a['t'] = 'w';
	a['a'] = 'y';
	a['h'] = 'x';
	a['w'] = 'f';
	a['f'] = 'c';
	a['o'] = 'k';
	a['u'] = 'j';
	a['g'] = 'v';
	a['q'] = 'z';
	a['z'] = 'q';


	int T, i, j;
	scanf("%d", &T);
	getchar();
	char G[120];
	for(i = 1; i < T + 1; i++)
	{
		scanf("%[^\n]", G);
		getchar();
		printf("Case #%d: ", i);
		for(j = 0; G[j] != '\0'; j++)
		{
			if(G[j] != ' ')
			{
				printf("%c", a[G[j]]);
			}
			else
			{
				printf(" ");
			}
		}
		printf("\n");
	}
	return 0;
}
