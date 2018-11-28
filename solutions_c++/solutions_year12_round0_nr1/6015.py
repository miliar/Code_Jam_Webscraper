#include <stdio.h>
#include <string.h>
#include <string>

using namespace std;


char decode[27];

int main()
{
	decode['e'-'a'] = 'o';
	decode['j'-'a'] = 'u';
	decode['p'-'a'] = 'r';
	decode['m'-'a'] = 'l';
	decode['y'-'a'] = 'a';
	decode['s'-'a'] = 'n';
	decode['l'-'a'] = 'g';
	decode['j'-'a'] = 'u';
	decode['c'-'a'] = 'e';
	decode['k'-'a'] = 'i';
	decode['d'-'a'] = 's';
	decode['x'-'a'] = 'm';
	decode['v'-'a'] = 'p';
	decode['n'-'a'] = 'b';
	decode['r'-'a'] = 't';
	decode['i'-'a'] = 'd';
	decode['t'-'a'] = 'w';
	decode['h'-'a'] = 'x';
	decode['w'-'a'] = 'f';
	decode['u'-'a'] = 'j';
	decode['g'-'a'] = 'v';
	decode['f'-'a'] = 'c';
	decode['b'-'a'] = 'h';
	decode['a'-'a'] = 'y';
	decode['o'-'a'] = 'k';	
	decode['z'-'a'] = 'q';
	decode['q'-'a'] = 'z';

	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("salida.out", "w", stdout);
	char buff[102];

	int T; scanf("%d\n", &T);
	for(int i = 1; i <= T; i++)
	{
		gets(buff);
		printf("Case #%d: ", i);
		string str(buff);
		for (int j = 0; j < str.size(); ++j)
		{
			if (str[j] == ' ')
				printf(" ");
			else
				printf("%c", decode[str[j] - 'a']);
		}
		printf("\n");
	}

	


	return 0;
}