#include <stdio.h>
#include <string.h>

char table[26] = {
	'y', // 'a'
	'h',
	'e',
	's',
	'o',
	'c',
	'v',
	'x',
	'd',
	'u',
	'i',
	'g',
	'l',
	'b', // 'n'
	'k',
	'r',
	'z',
	't',
	'n',
	'w',
	'j',
	'p',
	'f',
	'm',
	'a',
	'q'
};
char buffer[101];

int main(void)
{
	int T_;
	scanf("%d ", &T_);
	for (int i_ = 1; i_ <= T_; ++i_) {
		printf("Case #%d: ", i_);
		char c;
		while ((c = getchar()) != '\0' && c != '\n') {
			if ('a' <= c && c <= 'z') {
				putchar(table[c - 'a']);
			} else {
				putchar(c);
			}
		}
		printf("\n");
	}
	return 0;
}
