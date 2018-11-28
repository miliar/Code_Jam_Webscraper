#include <stdio.h>

#define MAX 1024

int n;
char *map = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
	char ch;

	scanf("%d ", &n);
	for(int i = 1; i <= n; i++) {
		printf("Case #%d: ", i);
		scanf("%c", &ch);
		while(ch != '\n') {
			if(ch >= 'a' && ch <= 'z')
				printf("%c", map[ch - 'a']);
			else printf("%c", ch);
			scanf("%c", &ch);
		}
		printf("\n");
	}

	return 0;
}
