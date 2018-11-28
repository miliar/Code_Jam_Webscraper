#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const char s1[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
const char s2[] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

char f[256], str[256];

int main() {
	int l = min(strlen(s1), strlen(s2)), n;
	f['q'] = 'z'; f['z'] = 'q';
	for (int i = 0; i < l; i++)
		f[s1[i]] = s2[i];
	gets(str);
	sscanf(str, "%d", &n);
	for (int i = 0; i < n; i++) {
		gets(str);
		for (int j = 0; str[j]; j++)
			str[j] = f[str[j]];
		printf("Case #%d: %s\n", i + 1, str);
	}
	return 0;
}
