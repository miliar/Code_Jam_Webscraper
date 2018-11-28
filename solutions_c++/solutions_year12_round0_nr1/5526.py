#include<iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>
#include <vector>
#include <cstdio>
#include <string>
using namespace std;
map<char,char>m;
char s[105];
int main()
{
	m['a']='y';m['b']='h';m['c']='e';m['d']='s';m['e']='o';m['f']='c';
	m['g']='v';m['h']='x';m['i']='d';m['j']='u';m['q']='z';m['t']='w';
	m['k']='i';m['l']='g';m['m']='l';m['n']='b';m['o']='k';m['p']='r';
	m['r']='t';m['u']='j';m['x']='m';m['s']='n';m['v']='p';m['y']='a';
	m['w']='f';m['z']='q';
	freopen("d:\\test.txt","w",stdout);
	int t,n,i,count=1;
	scanf("%d",&t);
	getchar();
	while(t--)
	{
		gets(s);
		n=strlen(s);
		printf("Case #%d: ",count++);
		for(i=0;i<n;i++)
		{
			if(s[i]>='a'&&s[i]<='z')
				printf("%c",m[s[i]]);
			else
				printf("%c",s[i]);
		}
		printf("\n");
	}
	return 0;
}