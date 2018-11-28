#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstring>
using namespace std;

char Dict[26];
void solve_problem()
{
	int n, i, j;
	char s[128];
	scanf("%[^\n]",s);
	scanf("%*c");
	for(i=0;s[i]!='\0';i++)
	{
		if(s[i] >= 'a' && s[i] <= 'z')
			printf("%c", Dict[s[i]-'a']);
		else
			printf("%c", s[i]);
	}
	puts("");
}

int main(void)
{
	int ct, tc;
	scanf("%d",&tc);
	scanf("%*c");
	Dict['a'-'a'] = 'y';
	Dict['b'-'a'] = 'h';
	Dict['c'-'a'] = 'e';
	Dict['d'-'a'] = 's';
	Dict['e'-'a'] = 'o';
	Dict['f'-'a'] = 'c';
	Dict['g'-'a'] = 'v';
	Dict['h'-'a'] = 'x';
	Dict['i'-'a'] = 'd';
	Dict['j'-'a'] = 'u';
	Dict['k'-'a'] = 'i';
	Dict['l'-'a'] = 'g';
	Dict['m'-'a'] = 'l';
	Dict['n'-'a'] = 'b';
	Dict['o'-'a'] = 'k';
	Dict['p'-'a'] = 'r';
	Dict['q'-'a'] = 'z';
	Dict['r'-'a'] = 't';
	Dict['s'-'a'] = 'n';
	Dict['t'-'a'] = 'w';
	Dict['u'-'a'] = 'j';
	Dict['v'-'a'] = 'p';
	Dict['w'-'a'] = 'f';
	Dict['x'-'a'] = 'm';
	Dict['y'-'a'] = 'a';
	Dict['z'-'a'] = 'q';
	for(ct=1;ct<=tc;ct++)			
	{
		printf("Case #%d: ", ct);	
		solve_problem();
	}
	return 0;
}
