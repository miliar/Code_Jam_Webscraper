#include <stdio.h>
#include <string.h>
char pre[27]="yhesocvxduiglbkrztnwjpfmaq";
int main()
{
	freopen("1.txt","r",stdin);
	freopen("3.txt","w",stdout);
	int i,j=0,k,l,n;
	char a[100000];
	scanf("%d",&n);
	getchar();
	while(n--)
	{
		gets(a);
		l=strlen(a);
		printf("Case #%d: ",++j);
		for(i=0;i<l;i++)
		{
			if(a[i]==' ')
				printf(" ");
			else
				printf("%c",pre[a[i]-'a']);
		}
		printf("\n");
	}
}