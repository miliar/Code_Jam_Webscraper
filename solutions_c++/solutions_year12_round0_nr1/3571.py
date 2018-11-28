/*
 *@File  A.cpp
 *@Descritpion   
 *@Date Sat 14 Apr 2012 08:49:52 AM CST
 *@Author zirui <zirui.dream@gmail.com>
 *@Website zirui.tk
 **/

#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

char table[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l',\
			'b','k','r','z','t','n','w','j','p','f','m','a','q'};
char s[102];

void Solve(int n)
{
	//printf("%s\n",s);
	printf("Case #%d: ",n);
	int len=strlen(s);
	char ch;
	for(int i=0;i<len;i++)
	{
		if(s[i]>='a' && s[i]<='z')
			ch=table[s[i]-'a'];
		else
			ch=s[i];
		putchar(ch);
	}
	putchar('\n');
}
int main(int argc, char* argv[])
{
	//freopen("A-small-attempt1.in","r",stdin);
	//freopen("A-small-attempt1.out","w",stdout);
	int T;
	scanf("%d",&T);
	getchar();
	for(int i=1;i<=T;i++)
	{
		gets(s);
		Solve(i);
	}
	//
	return 0;
}

