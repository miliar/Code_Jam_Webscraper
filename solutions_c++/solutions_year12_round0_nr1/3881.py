#include<stdio.h>
char s[27]="yhesocvxduiglbkrztnwjpfmaq";
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int c,t;
	char ch;
	scanf("%d",&t);
	while(getchar()!='\n');
	for(c=1;c<=t;c++)
	{
		printf("Case #%d: ",c);
		while((ch=getchar())!='\n')
		{
			if(ch>='a'&&ch<='z') ch=s[ch-'a'];
			putchar(ch);
		}
		putchar('\n');
	}
	return 0;
}