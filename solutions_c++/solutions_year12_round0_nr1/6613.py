#include "stdio.h"
#include "string.h"

void p(char c)
{
	printf("%c",c);
}
void change(char *a)
{
	int i, len;
	len=strlen(a);
	for(i=0; i<len; i++)
	{
		if(a[i]=='a')
			p('y');
		else if(a[i]=='b')
			p('h');
		else if(a[i]=='c')
			p('e');
		else if(a[i]=='d')
			p('s');
		else if(a[i]=='e')
			p('o');
		else if(a[i]=='f')
			p('c');
		else if(a[i]=='g')
			p('v');
		else if(a[i]=='h')
			p('x');
		else if(a[i]=='i')
			p('d');
		else if(a[i]=='j')
			p('u');
		else if(a[i]=='k')
			p('i');
		else if(a[i]=='l')
			p('g');
		else if(a[i]=='m')
			p('l');
		else if(a[i]=='n')
			p('b');
		else if(a[i]=='o')
			p('k');
		else if(a[i]=='p')
			p('r');
		else if(a[i]=='r')
			p('t');
		else if(a[i]=='s')
			p('n');
		else if(a[i]=='t')
			p('w');
		else if(a[i]=='u')
			p('j');
		else if(a[i]=='v')
			p('p');
		else if(a[i]=='w')
			p('f');
		else if(a[i]=='x')
			p('m');
		else if(a[i]=='y')
			p('a');
		else if(a[i]=='e')
			p('o');
		else if(a[i]=='q')
			p('z');
		else if(a[i]=='z')
			p('q');
		else 
			p(a[i]);
		
	}
	p('\n');
}

int main()
{
	int T;
	int i;
	char a[101];
	freopen("A-small-attempt3.in", "r", stdin);
	freopen("A-small-attempt3.out","w", stdout);
	scanf("%d", &T);
	getchar();
	for(i=1; i<=T; i++)
	{
		gets(a);
		printf("Case #%d: ", i);
		change(a);
	}
	return 0;
}