#include <iostream>
#include <cstdio>
#include <map>
using namespace std;
int main()
{
	map<char,char> ch;
	char i='a';
	ch['y'] = i++;
	ch['n'] = i++;
	ch['f'] = i++;
	ch['i'] = i++;
	ch['c'] = i++;
	ch['w'] = i++;
	ch['l'] = i++;
	ch['b'] = i++;
	ch['k'] = i++;
	ch['u'] = i++;
	ch['o'] = i++;
	ch['m'] = i++;
	ch['x'] = i++;
	ch['s'] = i++;
	ch['e'] = i++;
	ch['v'] = i++;
	ch['z'] = i++;
	ch['p'] = i++;
	ch['d'] = i++;
	ch['r'] = i++;
	ch['j'] = i++;
	ch['g'] = i++;
	ch['t'] = i++;
	ch['h'] = i++;
	ch['a'] = i++;
	ch['q'] = i++;
	ch[' '] = ' ';
	int t;
	scanf("%d",&t);
	getchar();
	for(int i=1;i<=t;i++)
	{
		char G[102];
		cin.getline(G,102);
		printf("Case #%d: ",i);
		for(int j=0;G[j]!='\0';j++)
		{
			printf("%c",ch[G[j]]);
		}
		printf("\n");
	}
	return 0;
}
