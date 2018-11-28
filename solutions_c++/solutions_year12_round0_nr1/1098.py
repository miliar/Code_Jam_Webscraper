#include <cstdio>

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	char map[] = "yhesocvxduiglbkrztnwjpfmaq";
	char c;
	int T;
	scanf("%d\n", &T);
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		while ((c = getchar()) != '\n' && c != EOF)
			if (c >= 'a' && c <= 'z')
				putchar(map[c - 'a']);
			else if (c >= 'A' && c <= 'Z')
				putchar(map[c - 'A'] + 'A' - 'a');
			else
				putchar(c);
		putchar('\n');
	}
	return 0;
}