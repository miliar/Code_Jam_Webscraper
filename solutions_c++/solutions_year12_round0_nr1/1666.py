#include <cstdio>
///////////////////abcdefghijklmnopqrstuvwxyz
const char mp[] = "yhesocvxduiglbkrztnwjpfmaq";
int main() {
	int n;
	scanf("%d ", &n);
	for (int i = 1; i <= n; ++i) {
		printf("Case #%d: ", i);
		char c;
		while (c = getchar()) {
			if (c == ' ') {
				putchar(c);
			} else if (c == '\n') {
				putchar(c);
				break;
			} else {
				putchar(mp[c - 'a']);
			}
		}
	}
	return 0;
}