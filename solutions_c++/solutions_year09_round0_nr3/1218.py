#include <stdio.h>
#include <string.h>

#define UNKNOWN -1

char buffer[10245];
int len;
int patternLen;
const char * pattern = "welcome to code jam";
int table[1024][50];

int total;

int
recur(int curPos, int curPattern)
{
	int ret = 0;

	if (curPattern > patternLen) {
		return 1;
	}
	if (curPos > len) {
		return 0;
	}

	if (table[curPos][curPattern] != UNKNOWN) {
		return table[curPos][curPattern];
	}

	ret += recur(curPos + 1, curPattern);
	if (buffer[curPos] == pattern[curPattern]) {
		ret += recur(curPos + 1, curPattern + 1);
	}

	table[curPos][curPattern] = ret % 10000;
	return table[curPos][curPattern];
}


int
main(int argc, char **argv)
{
	patternLen = strlen(pattern);

	int numLines;
	scanf("%d", &numLines);
	fgets(buffer, sizeof(buffer), stdin);

	for (int i = 0; i < numLines; i++) {
		for (int j = 0; j < 1024; j++) {
			for (int k = 0; k <= patternLen; k++) {
				table[j][k] = UNKNOWN;
			}
		}
		fgets(buffer, sizeof(buffer), stdin);
		len = strlen(buffer);
		total = recur(0, 0);

		printf("Case #%d: %04d\n", i + 1, total % 10000);
	}

	return 0;
}
