#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#define str(a) cha[a-97]
using namespace std;
const char cha[10000]="yhesocvxduiglbkrztnwjpfmaq";
int main()
{
	int T,len;
	char s[200];
	scanf("%d\n",&T);
	for(int i=1,;i<=T;i++)
	{
	    gets(s);
		printf("Case #%d: ",i);
		len=strlen(s);
		for(int i=0;i<len;i++)
		    printf("%c", str(s[i]) );
		printf("\n");
	}
	return 0;
}

