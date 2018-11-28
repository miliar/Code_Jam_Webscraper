#include<cstdio>
#include<cstring>
char q[]="yhesocvxduiglbkrztnwjpfmaq";
char x[10001];
int n;
int main()
{
	int k,a;
	scanf("%d",&n);
	gets(x);
	for(int i=1;i<=n;i++)
	{
		gets(x);
		k=strlen(x);
		for(int j=0;j<k;j++)
		{
			if(x[j]!=32)
			{
				a=x[j]-'a';
				x[j]=q[a];
			}
		}
		printf("Case #%d: ",i);
		puts(x);
	}
	return 0;
}
