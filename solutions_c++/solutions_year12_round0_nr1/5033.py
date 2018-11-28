#include <cstdio>
#include <algorithm>
using namespace std;

int qt;
char znak[30]="yhesocvxduiglbkrztnwjpfmaq";
char s[200];

int main()
{
	scanf("%d ", &qt);
	for(int i=1; i<=qt; i++)
	{
		gets(s);
		printf("Case #%d: ", i);
		for(int j=0; s[j]; j++)
			if(s[j]!=' ') printf("%c", znak[s[j]-97]);
			else printf(" ");
		printf("\n");
	}
	
	return 0;
}
