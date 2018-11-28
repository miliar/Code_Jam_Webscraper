#include <cstdio>
#include <cstring>
#include <cctype>

//                ABCDEFGHIJKLMNOPQRSTUVWXYZ
char mapping[] = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
	int n;
	scanf("%d ", &n);

	for (int i = 0; i < n; i++) {

		printf("Case #%d: ", i + 1);
		char in[105];

		fgets(in, 105, stdin);

		for (int j = 0; j < strlen(in); j++) {
			if (islower(in[j])) {
				printf("%c", mapping[in[j] - 'a']);
			} else {
				printf("%c", in[j]);
			}
		}
	}

	return 0;
}
