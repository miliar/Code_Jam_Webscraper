#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

const char st[30] = "yhesocvxduiglbkrztnwjpfmaq" ;
char str[105];

int main()
{
	int T;
	scanf("%d",&T);
	getchar();
	for(int k = 1;k <= T;++k)
	{
		memset(str,0,sizeof(str));
		gets(str);
		printf("Case #%d: ",k);
		for(int i = 0;i < strlen(str);++i)
		{
			if(str[i] == ' ') printf(" ");
			else printf("%c",st[str[i] - 'a']);
		}
		printf("\n");
	}
}