#include <cstdio>
#include <cstring>
using namespace std;

char stack[1000];
int top;
int instack['Z'+1];
char merge['Z'+1]['Z'+1];
bool destroy['Z'+1]['Z'+1];
char s[1000];

void process_case()
{
	top = -1;
	int n = strlen(s);
	char c;
	bool bad;
	for(int i = 0; i < n; i++)
	{
		c = s[i];
		while(top > -1 && merge[c][stack[top]])
			c = merge[c][stack[top--]];
		stack[++top] = c;
		bad = false;
		for(int i = 0; i < top && !bad; i++)
			if(destroy[stack[i]][stack[top]])
				bad = true;
		if(bad)
			top = -1;
	}
	if(top == -1)
		printf("[]\n");
	else
	{
		printf("[%c", stack[0]);
		for(int i = 1; i <= top; i++)
			printf(", %c", stack[i]);
		printf("]\n");
	}
}


void handle_input()
{
	for(int i = 'A'; i <= 'Z'; i++)
		for(int j = 'A'; j <= 'Z'; j++)
			merge[i][j] = destroy[i][j] = false;
	int n;
	scanf("%d", &n);
	while(n--)
	{
		scanf("%s", s);
		merge[s[0]][s[1]] = merge[s[1]][s[0]] = s[2];
	}
	scanf("%d", &n);
	while(n-- > 0)
	{
		scanf("%s", s);
		destroy[s[0]][s[1]] = destroy[s[1]][s[0]] = true;
	}
	scanf("%d", &n);
	scanf("%s", s);
}



int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
	{
		handle_input();
		printf("Case #%d: ", i);
		process_case();
	}
}