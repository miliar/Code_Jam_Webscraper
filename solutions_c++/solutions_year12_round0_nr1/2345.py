#include <cstring>
#include <cstdio>

using namespace std;

char s[1000];
int n, map[1000];

int main()
{
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
//   freopen("input.txt", "r", stdin);
//   freopen("output.txt", "w", stdout);
   int i, t, cnt = 0;
   scanf("%d%*c", &t);
   for (i = 0;i < t;i++)
	{
		gets(s);
		++cnt;
		printf("Case #%d: ", cnt);
		int n = strlen(s);
		int i;
		for (i = 0;i < n;i++)
			printf("%c", map[s[i]]);
		printf("\n");
	}
//    fclose(stdout);
	return 0;
}
