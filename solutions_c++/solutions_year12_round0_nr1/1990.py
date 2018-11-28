#include <stdio.h>

char s[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
int t,T;
char x[1000];

int main()
{
	freopen("D:\\A-small-attempt0.in", "r", stdin);
	freopen("D:\\A-small-attempt0.out", "w", stdout);

	scanf("%d", &T);
	gets(x);
	for (t=1; t<=T; t++)
	{
		gets(x);
		for (int i=0; x[i]!=0; i++)
		{
			if (x[i]>='a' && x[i]<='z')
			{
				x[i]=s[x[i]-'a'];
			}
		}
		printf("Case #%d: %s\n", t, x);
	}

	return 0;
}