#include <stdio.h>
#include <stdlib.h>
int main() {
	char map[26];
	map[0] = 'y' - 'a';
	map[1] = 'h' - 'a';
	map[2] = 'e' - 'a';
	map[3] = 's' - 'a';
	map[4] = 'o' - 'a';
	map[5] = 'c' - 'a';
	map[6] = 'v' - 'a';
	map[7] = 'x' - 'a';
	map[8] = 'd' - 'a';
	map[9] = 'u' - 'a';
	map[10] = 'i' - 'a';
	map[11] = 'g' - 'a';
	map[12] = 'l' - 'a';
	map[13] = 'b' - 'a';
	map[14] = 'k' - 'a';
	map[15] = 'r' - 'a';
	map[16] = 'z' - 'a';
	map[17] = 't' - 'a';
	map[18] = 'n' - 'a';
	map[19] = 'w' - 'a';
	map[20] = 'j' - 'a';
	map[21] = 'p' - 'a';
	map[22] = 'f' - 'a';
	map[23] = 'm' - 'a';
	map[24] = 'a' - 'a';
	map[25] = 'q' - 'a';
	int n, i, count = 1;
	char str[110];
	char str1[110];
	gets(str);
	n = atoi(str);
	while(n--) {
		gets(str);
		i = 0;
		while(str[i] != 0) {
			if(str[i] != ' ') {
				str1[i] = map[str[i++] - 'a'] + 'a';
			}
			else
				str1[i++] = ' ';
		}
		str1[i] = 0;
		printf("Case #%d: %s\n", count++, str1);
	}
	return 0;
}