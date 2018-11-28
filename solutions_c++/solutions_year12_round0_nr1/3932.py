#include<stdio.h>
#include<string.h>
const char trans[51]={"yhesocvxduiglbkrztnwjpfmaq"};
char s[100001];
int main()
{
	int t,bk,i,j,n;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d%*c",&t);
	for(bk=0;bk<t;++bk)
	{
		gets(s);
		n=strlen(s);
		printf("Case #%d: ",bk+1);
		for(i=0;i<n;++i)
			if(s[i]==' ')
				printf(" ");
			else
				printf("%c",trans[s[i]-'a']);
		printf("\n");
	}
	return 0;
}
