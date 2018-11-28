#include <iostream>
#include <stdio.h>
#include <cstring>
#include <fstream>

using namespace std;

int t;
char a[30] = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	char b[1000];
	int p = 1;
	freopen("A-small-attempt3.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	gets(b);
	while(t--)
	{
		printf("Case #%d: ",p++);
		gets(b);
		for(int i=0; i<strlen(b); i++)
			if(b[i]==' ')
				printf(" ");
			else
				printf("%c",a[b[i]-'a']);
		puts("");
	}
	return 0;
}
