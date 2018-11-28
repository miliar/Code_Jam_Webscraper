#include<cstdio>
#include<cstring>
#include<iostream>
#include<map>
using namespace std;

map<char, char> dic;
void init()
{
dic['a']='y';
dic['b']='h';
dic['c']='e';
dic['d']='s';
dic['e']='o';
dic['f']='c';
dic['g']='v';
dic['h']='x';
dic['i']='d';
dic['j']='u';
dic['k']='i';
dic['l']='g';
dic['m']='l';
dic['n']='b';
dic['o']='k';
dic['p']='r';
dic['q']='z';
dic['r']='t';
dic['s']='n';
dic['t']='w';
dic['u']='j';
dic['v']='p';
dic['w']='f';
dic['x']='m';
dic['y']='a';
dic['z']='q';
}
char s1[1000];
char s2[1000];
int main()
{
	init();
	int t;	
	char junk;
	scanf("%d%c", &t, &junk);
	for(int T=1; T<=t; T++)
	{
		printf("Case #%d: ", T);
		gets(s1);
		int n = strlen(s1);
		for(int i=0; i<n; i++)
		{
			if(s1[i] == ' ') putchar(' ');
			else putchar(dic[s1[i]]);
		}
		putchar('\n');
	}
}