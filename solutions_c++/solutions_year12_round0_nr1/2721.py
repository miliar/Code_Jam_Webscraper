#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

char s[110], map[200];
int t, cases = 0, l, i;

int main()
{
//	freopen("out.txt", "w", stdout);
	map['a'] = 'y';
	map['b'] = 'h';
	map['c'] = 'e';
	map['d'] = 's';
	map['e'] = 'o';
	map['f'] = 'c';
	map['g'] = 'v';
	map['h'] = 'x';
	map['i'] = 'd';
	map['j'] = 'u';
	map['k'] = 'i';
	map['l'] = 'g';
	map['m'] = 'l';
	map['n'] = 'b';
	map['o'] = 'k';
	map['p'] = 'r';
	map['q'] = 'z';
	map['r'] = 't';
	map['s'] = 'n';
	map['t'] = 'w';
	map['u'] = 'j';
	map['v'] = 'p';
	map['w'] = 'f';
	map['x'] = 'm';
	map['y'] = 'a';
	map['z'] = 'q';
	map[' '] = ' ';
	scanf("%d%*c", &t);
	while (t--)
	{
		gets(s);
		l = strlen(s);
		printf("Case #%d: ", ++cases);
		for (i = 0; i < l; ++i)
			printf("%c", map[s[i]]); 
		printf("\n");
	}
	return 0;
}
