#include <stdio.h>
#include <string.h>

char wel[] = "welcome to code jam";

int main()
{
	int t, nt;
	char buf[512];
	scanf("%d", &nt);
	gets(buf);
	for(t = 1; gets(buf); t++)
	{
		int pd[32], len = strlen(buf);
		memset(pd, 0, sizeof(pd));
		pd[0] = 1;
		for(int i = 0; i < len; i++)
			for(int j = 18; j >= 0; j--)
				if(wel[j] == buf[i])
					pd[j+1] = (pd[j+1] + pd[j])%10000;
		printf("Case #%d: %04d\n", t, pd[19]);
	}
	return 0;
}
