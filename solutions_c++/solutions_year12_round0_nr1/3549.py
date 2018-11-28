#include<cstdio>
#include<cstring>
#include<map>
using namespace std;

map<char,char> m;
void pre()
{
	m[' '] = ' ';
	m['a'] = 'y';
	m['c'] = 'e';
	m['b'] = 'h';
	m['e'] = 'o';
	m['d'] = 's';
	m['g'] = 'v';
	m['f'] = 'c';
	m['i'] = 'd';
	m['h'] = 'x';
	m['k'] = 'i';
	m['j'] = 'u';
	m['m'] = 'l';
	m['l'] = 'g';
	m['o'] = 'k';
	m['n'] = 'b';
	m['p'] = 'r';
	m['q'] = 'z';
	m['s'] = 'n';
	m['r'] = 't';
	m['u'] = 'j';
	m['t'] = 'w';
	m['w'] = 'f';
	m['v'] = 'p';
	m['y'] = 'a';
	m['x'] = 'm';
	m['z'] = 'q';
}

int main()
{
	pre();

	int t;
	char inp[110];
	
	scanf("%d ",&t);
	for(int cases=1; cases<=t; cases++)
	{
		scanf("%[^\n] ",inp);
		printf("Case #%d: ",cases);
		
		int l = strlen(inp);
		for(int i=0; i<l; i++) { printf("%c",m[inp[i]]); }
		printf("\n");
	}
	return 0;
}
