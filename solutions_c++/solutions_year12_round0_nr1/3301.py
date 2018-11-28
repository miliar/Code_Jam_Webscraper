#include <iostream>
#include <cctype>
#include <cstdio>
#include <cstring>
using namespace std;

char hash[1000];
void work(const char * const a, const char * const b)
{
	for (int i=0; a[i]!='$'; i++)
		if (isalpha(a[i]))
			hash[a[i]-'a'] = b[i];
}
int main(void)
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);

	work("ejp mysljylc kd kxveddknmc re jsicpdrysi$", "our language is impossible to understand$");
	work("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd$", "there are twenty six factorial possibilities$");
	work("de kr kd eoya kw aej tysr re ujdr lkgc jv$", "so it is okay if you want to just give up$");

	hash['q'-'a'] = 'z';
	hash['z'-'a'] = 'q';

	int T;
	char s[111];
	scanf("%d", &T);
	gets(s);
	for (int i=1; i<=T; i++)
	{
		char s[111];
		gets(s);
		for (int j=0; s[j]; j++)
			if (isalpha(s[j]))
				s[j] = hash[s[j] - 'a'];
		printf("Case #%d: %s\n", i, s);
	}
	return 0;
}
