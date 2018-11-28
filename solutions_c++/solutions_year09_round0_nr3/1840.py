#include <stdio.h>
#include <string.h>

char line[501];
char* name = "welcome to code jam";

int combinations(int start, int numLetter) {
	if (numLetter == 19)
		return 1;
	if (line[start] == '\0')
		return 0;
	int count = 0;
	for (int i = start; line[i] != '\0'; i++) {
		if (name[numLetter] == line[i]) {
			count += combinations(i + 1, numLetter + 1);
		}
	}
	return count;
}

int main() {
	int n;
	scanf("%d", &n);
	gets(line);
	for (int t = 1; t <= n; t++) {
		gets(line);
		printf("Case #%d: %04d\n", t, combinations(0, 0));
	}

}
