#include <stdio.h>
#include <string.h>
#define maxLen 100
#define N 30
int main()
{	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A.txt", "w", stdout);
	int T;
	char str[maxLen +1];
	scanf("%d", &T);
	getchar();
	for (int t = 1; t <= T; ++t) {
		gets(str);
		printf("Case #%d: ", t);
		int len = strlen(str);
		for (int i = 0; i < len; ++i)
			if (str[i] == 'a')		str[i] = 'y';
			else if (str[i] == 'b') str[i] = 'h';
			else if (str[i] == 'c') str[i] = 'e';
			else if (str[i] == 'd') str[i] = 's';
			else if (str[i] == 'e') str[i] = 'o';
			else if (str[i] == 'f') str[i] = 'c';
			else if (str[i] == 'g') str[i] = 'v';
			else if (str[i] == 'h') str[i] = 'x';
			else if (str[i] == 'i') str[i] = 'd';
			else if (str[i] == 'j') str[i] = 'u';
			else if (str[i] == 'k') str[i] = 'i';
			else if (str[i] == 'l') str[i] = 'g';
			else if (str[i] == 'm') str[i] = 'l';
			else if (str[i] == 'n') str[i] = 'b';
			else if (str[i] == 'o') str[i] = 'k';
			else if (str[i] == 'p') str[i] = 'r';
			else if (str[i] == 'q') str[i] = 'z';
			else if (str[i] == 'r') str[i] = 't';
			else if (str[i] == 's') str[i] = 'n';
			else if (str[i] == 't') str[i] = 'w';
			else if (str[i] == 'u') str[i] = 'j';
			else if (str[i] == 'v') str[i] = 'p';
			else if (str[i] == 'w') str[i] = 'f';
			else if (str[i] == 'x') str[i] = 'm';
			else if (str[i] == 'y') str[i] = 'a';
			else if (str[i] == 'z')	str[i] = 'q';

		puts(str);
	}//scanf(" ");
	return 0;
}
