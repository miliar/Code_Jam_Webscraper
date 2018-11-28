#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

char s[27]={"yhesocvxduiglbkrztnwjpfmaq"};

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.out","w",stdout);
	int t;
	int i;
	int cs=1;
	char inp[105];
	char oup[105];
	scanf("%d",&t);
	getchar();
	while(t--)
	{
		memset(oup,0,sizeof(oup));
		gets(inp);
		int len=strlen(inp);
		for(i=0;i<len;i++)
		{
			if(inp[i]==' ')
				oup[i]=' ';
			else
				oup[i]=s[inp[i]-'a'];
		}
		oup[len]='\0';
		printf("Case #%d: ",cs++);
		puts(oup);
	}
	return 0;
}