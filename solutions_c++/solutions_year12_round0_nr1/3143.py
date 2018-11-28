#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

char map[26][3]={"ay","bh","ce","ds","eo","fc","gv","hx","id","ju","ki","lg","ml","nb","ok","pr","qz","rt","sn","tw","uj","vp","wf","xm","ya","zq"}; 

int main()
{
	int t;
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d\n",&t);
	for(int i=1;i<=t;i++)
	{
		char text[105];
		char ans[105];
		gets(text);
		int len=strlen(text);
		int j;
		for(j=0;j<len;j++)
		{
			if(text[j]==' ')
			ans[j]=text[j];
			else 
			ans[j]=map[text[j]-'a'][1];
		}
		ans[j]='\0';
		printf("Case #%d: %s\n",i,ans);
	}	
	return 0;
}
