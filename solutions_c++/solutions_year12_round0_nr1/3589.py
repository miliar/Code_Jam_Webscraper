#include<iostream>
using namespace std;
char map[255];

void init()
{
	map['y']='a';
	map['n']='b';
	map['f']='c';
	map['i']='d';
	map['c']='e';
	map['w']='f';
	map['l']='g';
	map['b']='h';
	map['k']='i';
	map['u']='j';
	map['o']='k';
	map['m']='l';
	map['x']='m';
	map['s']='n';
	map['e']='o';
	map['v']='p';
	map['z']='q';
	map['p']='r';
	map['d']='s';
	map['r']='t';
	map['j']='u';
	map['g']='v';
	map['t']='w';
	map['h']='x';
	map['a']='y';
	map['q']='z';
	map[' ']=' ';
}

int main()
{
	init();
	int n, m, i;
	char goo_text[110], c;
	
	scanf("%d \n", &n);
	
	for(m=1; m<=n; m++)
	{
		printf("Case #%d: ", m);
		
		cin.getline(goo_text, 110);
		
		for(i=0;i<=strlen(goo_text);i++)
		{
			c=goo_text[i];
			if(c>='a' && c<='z')
				printf("%c", map[c]);
			else
				printf("%c", c);
		}
		printf("\n");
	}
}