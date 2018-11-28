#include <iostream>
#include <stdio.h>
#include <memory.h>
#include <string.h>

using namespace std;

const char str[] = "yhesocvxduiglbkrztnwjpfmaq";
char ss[105];
char ans[105];

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, ca = 1;
	scanf("%d", &T);
	gets(ss);
	while (T --)
	{
		gets(ss);
		int i = 0;
		while (ss[i])
		{
			if (ss[i] == ' ')
				ans[i] = ss[i];
			else
				ans[i] = str[ss[i]-'a'];
			i ++;
		}
		ans[i] = '\0';
		printf("Case #%d: %s\n", ca++, ans);
	}
	return 0;
}

