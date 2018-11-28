#include <stdio.h>
#include <string.h>

int main()
{
	char a[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int t,len,i,j;
	char str[101];
	scanf("%d",&t);
	gets(str);
	for(j = 1;j <=t ;j++)
	{
		
		gets(str);
		len = strlen(str);
		printf("Case #%d: ",j);
		for(i = 0;i < len;i++)
		{
			if(str[i] == ' ')
				printf(" ");
			else
				printf("%c",a[str[i]-97]);
		}
		printf("\n");
	}
	return 0;
}