#include <cstdio>
#include <cstring>

const char ex[27] = "yhesocvxduiglbkrztnwjpfmaq";

char s[1012];

int main() {
	int T; scanf("%d", &T);
	for (int Case = 1; Case <= T; Case ++) {
		gets(s);
		while (strlen(s) == 0) gets(s);

		int l = strlen(s);
		for (int i = 0; i < l; i ++)
			if (s[i] != ' ') s[i] = ex[s[i] - 'a'];

		printf("Case #%d: %s\n", Case, s);
	}

	return 0;
}
