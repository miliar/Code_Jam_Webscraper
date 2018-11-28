#include<iostream>
#include<cstdio>
#include<string>
#include<ctype.h>
using namespace std;
int main()
{
	int t,t1;
	scanf("%d",&t);
	t1=t;
	string ref="yhesocvxduiglbkrztnwjpfmaq";
	while(t--)
	{
		cin.get();
		char s[102];
		scanf("%[^\n]",s);
		printf("Case #%d: ",t1-t);
		for(int i=0;s[i]!='\0';i++)
		{
			if(isalpha(s[i]))
				printf("%c",ref[(int)s[i]%97]);
			else
				printf("%c",s[i]);
		}	
		printf("\n");
	}
	return 0;
}
