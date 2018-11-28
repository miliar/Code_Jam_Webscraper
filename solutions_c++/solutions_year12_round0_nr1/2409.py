#include <cstdio>

char f[256];

void initf()
{
	char *a =
"ejp mysljylc kd kxveddknmc re jsicpdrysi\n"
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\n"
"de kr kd eoya kw aej tysr re ujdr lkgc jvzq";
	char *b =
"our language is impossible to understand\n"
"there are twenty six factorial possibilities\n"
"so it is okay if you want to just give upqz";
	for (int i=0; a[i]; ++i)
	{
		if (f[a[i]]&&f[a[i]]!=b[i])
			printf("O_o\n");
		f[a[i]]=b[i];
	}
}

char buff[200];

int main()
{
	initf();
	for (int i='a'; i<='z'; ++i)
	{
		int j;
		for (j='a'; j<='z'; ++j)
		if (f[j] == i)
			break;
		if (j > 'z')
			printf("%c", i);
	}
	int n;
	scanf("%d\n",&n);
	for (int i=0; i<n; ++i)
	{
		gets(buff);
		for (int j=0; buff[j]; ++j)
			buff[j] = f[buff[j]];
		printf("Case #%d: %s\n", i+1, buff);
	}
	return 0;
}