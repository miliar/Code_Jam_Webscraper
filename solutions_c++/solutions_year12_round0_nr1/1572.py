#include <cstdio>
#include <cstring>
#include <cctype>

char trans	[128];
char buf[10000];

int main()
{
	char src[3][128] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	char dst[3][128] = {"our language is impossible to understand",
		"there are twenty six factorial possibilities",
		"so it is okay if you want to just give up"};

	
	memset(trans, 0xff, sizeof(trans));
	
	for (int i = 0; i < 3; i ++)
	{
		int len = strlen(src[i]);
		for (int j = 0; j < len; j ++)
			if (isalpha(src[i][j]))
			{
				trans[src[i][j]] = dst[i][j];
			}
	}
	
	trans['z'] = 'q';
	
	int v = 0;
	for (int x = 'a'; x <= 'z'; x ++)
	{
		v += x;
		if (trans[x] >= 0) v -= trans[x];
//		printf("%c -> %c\n", x, trans[x] < 0 ? '?' : trans[x]);
	}
	trans['q'] = v;
	int x = 'q';
//	printf("%c -> %c\n", x, trans[x] < 0 ? '?' : trans[x]);
	
	int n;
	
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	fgets(buf, 10000, stdin);
	sscanf(buf, "%d", &n);
	
	for (int t = 1; t <= n; t ++)
	{
		fgets(buf, 10000, stdin);
		printf("Case #%d: ", t);
			

		for (int i = 0; buf[i] != '\n'; i ++)
			if (isalpha(buf[i]))
				buf[i] = trans[buf[i]];
				
			printf("%s", buf);
	}
	
		
	return 0;
}