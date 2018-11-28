#include <stdio.h>
#include <string.h>

char array[26]= {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l','b', 'k', 'r', 'z',	't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q',};

int main()
{
	int n;
	char str[300];
	
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	scanf("%d", &n);
	gets(str);
	for (int i=0; i<n; ++i)
	{
		gets(str);
		for (int j=0; j<strlen(str); ++j)
		{
			if (str[j]<='z' && str[j]>='a')
				str[j] = array[str[j]-'a'];
		}
		printf("Case #%d: ", i+1);
		printf("%s\n",str);
	}
	return 0;
}
