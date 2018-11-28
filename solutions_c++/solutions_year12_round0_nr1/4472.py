#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int t;
char str[105], ans[105];
string alph;
int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	alph = "yhesocvxduiglbkrztnwjpfmaq";

	scanf("%d", &t);
	gets(str);
	for(int tt = 0; tt < t; ++tt)
	{
		gets(str);
		int l = strlen(str);
		for(int j = 0; j < l; ++j)
			if(str[j] != ' ')
				ans[j] = alph[str[j] - 'a'];
			else
				ans[j] = ' ';
		ans[l] = 0;
		printf("Case #%d: %s\n", tt + 1, ans);
	}
	return 0;
}

/*
yhesocvxduiglbkrztnwjpfma
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
*/