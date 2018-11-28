#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char str[110];
const char *rule = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	int T, t, i;

	scanf("%d", &T);
	getchar();
	for (t = 1; t <= T; t++) {
		gets(str);
		for (i = 0; str[i]; i++) {
			if (str[i] == ' ') continue;
			str[i] = rule[str[i] - 'a'];
		}
		printf("Case #%d: %s\n", t, str);
	}

	return 0;
}
