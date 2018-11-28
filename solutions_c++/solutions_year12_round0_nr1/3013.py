#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cctype>

using namespace std;

char s[1000] = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv",
r[1000] = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
int m[1000];
char ans[1000];
int t;

int main() {
	memset(m, -1, sizeof(m));

	for (int i = 0; s[i]; ++i)
		if (isalpha(s[i])) m[s[i] - 'a'] = r[i] - 'a';

	m['q' - 'a'] = 'z' - 'a', m['z' - 'a'] = 'q' - 'a';

	scanf("%d", &t); gets(ans);
	for (int cases = 1; cases <= t; ++cases) {
		gets(ans);
		for (int i = 0; ans[i]; ++i) if (isalpha(ans[i])) ans[i] = 'a' + m[ans[i] - 'a'];
		printf("Case #%d: %s\n", cases, ans);
	}

	return 0;
}
