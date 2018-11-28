#include<stdio.h>
char arr[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char str[109];
int main()
{
	int t;
	scanf("%d%*c",&t);
	for(int tc=1; tc<=t; tc++)
	{
		gets(str);
		printf("Case #%d: ",tc);
		for(int i=0; str[i]; i++)
		printf("%c",str[i]>='a'&&str[i]<='z'?arr[str[i]-'a']:str[i]);
		printf("\n");
	}
	return 0;
}
