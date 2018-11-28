#include <cstdio>
#include <cstring>

char s[1000];
char mp[] = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
	int cas = 0;
	int T;
	scanf("%d", &T); gets(s);
	while (T--) {
		printf("Case #%d: ", ++cas);
		gets(s);
		for (int i = 0; s[i]; ++i) {
			printf("%c", s[i] == ' ' ? ' ' : mp[s[i] - 'a']);
		}
		puts("");
	}
	return 0;
}
