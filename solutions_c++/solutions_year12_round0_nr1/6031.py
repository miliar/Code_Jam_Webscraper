#include <cstdio>
#include <cstring>

int T;
char dict[256];

void load(char *a, char *b) {
	for(char *p = a, *q = b; *p && *q; p++, q++)
		dict[*p] = *q;
}

int main(void) {
	load("abcdefghijklmnopqrstuvwxyz \n", "yhesocvxduiglbkrztnwjpfmaq \n");
	scanf("%d\n", &T);
	for(int C = 1; C <= T; C++) {
		char line[128];
		fgets(line, sizeof(line), stdin);
		printf("Case #%d: ", C);
		for(char *p = line; *p; p++) putchar(dict[*p]);
	}

	return 0;
}
