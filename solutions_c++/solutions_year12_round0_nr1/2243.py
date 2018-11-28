#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdio.h>

#define MAX_LINE 1024

#define RN(v) \
({ \
	char line[MAX_LINE]; \
	RL(line); \
	sscanf(line, "%d", &v); \
})

#define RL(line) \
({ \
	int size = -1; \
	if (fgets(line, sizeof(line), stdin)) {; \
		size = strlen(line) - 1; \
		line[size] = 0; \
	} \
	size; \
})

// ejp mysljylc kd kxveddknmc re jsicpdrysi
// our language is impossible to understand
//
// rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
// there are twenty six factorial possibilities
//
// de kr kd eoya kw aej tysr re ujdr lkgc jv
// so it is okay if you want to just give up

char map[] = {
	'y', // a
	'h', // b
	'e', // c
	's', // d
	'o', // e
	'c', // f
	'v', // g
	'x', // h
	'd', // i
	'u', // j
	'i', // k
	'g', // l
	'l', // m
	'b', // n
	'k', // o
	'r', // p
	'z', // q
	't', // r
	'n', // s
	'w', // t
	'j', // u
	'p', // v
	'f', // w
	'm', // x
	'a', // y
	'q', // z
};

int
main(int argc, char *argv[])
{
	char buff[MAX_LINE];

	int T; // # of test cases
	RN(T);

	for (int i = 0; i < T; i++) {
		int size = RL(buff);
		printf("Case #%d: ", i + 1);

		for (int j = 0; j < size; j++) {
			if (buff[j] != ' ') {
				buff[j] = map[buff[j] - 'a'];
			}
		}
		printf("%s\n", buff);
	}
	return 0;
}

