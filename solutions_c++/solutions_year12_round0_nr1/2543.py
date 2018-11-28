#include <stdio.h>
#include <string.h>

char mp[]="yhesocvxduiglbkrztnwjpfmaq";
int main()
{
	int n, d, i;
	char ip[200];
	scanf("%d", &n);
	getchar();
	for(d=1; d<=n; d++)
	{
		gets(ip);
		for(i=0; ip[i]; i++)
			if(ip[i]!=' ')
				ip[i] = mp[ip[i]-'a'];
		printf("Case #%d: %s\n", d, ip);
	}
	return 0;
}
