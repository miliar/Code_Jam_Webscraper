#include<cstdio>
#include<cstring>

char s[]="yhesocvxduiglbkrztnwjpfmaq";
char S[105];
int n;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d\n",&n);
	for(int i=0;i<n;i++)
	{
		gets(S);
		printf("Case #%d: ",i+1);
		for(int j=0;j<strlen(S);j++)
			if(S[j]==' ')
				putchar(' ');
			else
				putchar(s[S[j]-'a']);
		puts("");
	}
	return 0;
}


