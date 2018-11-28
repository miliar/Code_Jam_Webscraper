#include <stdio.h>

int translate[1000];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

		translate['a'] = 'y';
		translate['b'] = 'h';
		translate['c'] = 'e';
		translate['d'] = 's';
		translate['e'] = 'o';
		translate['f'] = 'c';
		translate['g'] = 'v';
		translate['h'] = 'x';
		translate['i'] = 'd';
		translate['j'] = 'u';
		translate['k'] = 'i';
		translate['l'] = 'g';
		translate['m'] = 'l';
		translate['n'] = 'b';
		translate['o'] = 'k';
		translate['p'] = 'r';
		translate['q'] = 'z';
		translate['r'] = 't';
		translate['s'] = 'n';
		translate['t'] = 'w';
		translate['u'] = 'j';
		translate['v'] = 'p';
		translate['w'] = 'f';
		translate['x'] = 'm';
		translate['y'] = 'a';
		translate['z'] = 'q';
		
		int T, Case, i;
		char tmp;
		scanf("%d", &T);
		while(true){
			scanf("%c",&tmp);
			if(tmp == '\n') break;
		}
		for(Case=1;Case<=T;Case++)
		{
			printf("Case #%d: ", Case);
			while(true){
				scanf("%c",&tmp);
				if(tmp == '\n') break;

				if(tmp >= 'a' && tmp <= 'z') printf("%c", translate[tmp]);
				else if(tmp == ' ') printf(" ");
			}
			printf("\n");
		}
		
		return 0;
}