#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <string>
#include <queue>
#include <cmath>
#include <stack>
#define LG __int64
using namespace std;
const int maxn=100005;
int n,m;
int ch[256];
FILE *fp;
void init()
{
	ch['a']='y';ch['b']='h',ch['c']='e',ch['d']='s',ch['e']='o';
	ch['f']='c',ch['g']='v',ch['h']='x',ch['i']='d',ch['j']='u';
	ch['k']='i',ch['l']='g',ch['m']='l',ch['n']='b',ch['o']='k';
	ch['p']='r',ch['q']='z',ch['r']='t',ch['s']='n',ch['t']='w';
	ch['u']='j',ch['v']='p',ch['w']='f',ch['x']='m',ch['y']='a';
	ch['z']='q';
}
char s[1000000];
int main()
{
	//fp=fopen("1.out","w");
	init();
	int t=1,T;
	scanf("%d",&T);
	gets(s);
	while(T--)
	{
		gets(s);
		int len=strlen(s);
		//fprintf(fp,"Case #%d: ",t);
		printf("Case #%d: ",t++);	
		for(int i=0;i<len;i++)
		{
			if(s[i]<='z'&&s[i]>='a')
			{
				printf("%c",ch[s[i]]);
			//	fprintf(fp,"%c",ch[s[i]]);
			}
			else
			{
					printf("%c",s[i]);
			//		fprintf(fp,"%c",s[i]);
			}
		}
		printf("\n");
		//fprintf(fp,"\n");
	}
	return 0;
}