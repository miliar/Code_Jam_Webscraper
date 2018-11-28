#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
	freopen("a.in","r",stdin);
	freopen("out.txt","w",stdout);
	char arr[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int n;
	scanf("%d", &n);	
	getchar();
	int i = 1;
	while (n--)
	{
		printf("Case #%d: ",i++);
		char buf1[105];
		gets(buf1);
		char *p = buf1;
		while ( *p )
		{
			char ret = ' ';
			if ( *p != ret)
			{
				int index = *p - 'a';				
				ret = arr[index];
			}
			printf("%c",ret);
			++p;
		}
		printf("\n");
	}
	return 0;
}