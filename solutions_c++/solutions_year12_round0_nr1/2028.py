#include <stdio.h>

char hash[30]="yhesocvxduiglbkrztnwjpfmaq";

char str[110];

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A.txt","w",stdout);
	int ct,caset = 1;
	scanf("%d",&ct);
	gets(str);
	while(ct--)
	{
		printf("Case #%d: ",caset++);
       gets(str);
	   char *p = str;
	   while(*p)
	   {
		   if(*p==' ')
			   printf(" ");
		   else
			   printf("%c",hash[*p-'a']);
		   p++;
	   }
	   printf("\n");
	}
	return 0;
}