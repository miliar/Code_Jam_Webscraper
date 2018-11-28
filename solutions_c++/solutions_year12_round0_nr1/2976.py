#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

static const char trans[] = {
		'y', /* 'a' */
		'h', /* 'b' */
		'e', /* 'c' */
		's', /* 'd' */
		'o', /* 'e' */
		'c', /* 'f' */
		'v', /* 'g' */
		'x', /* 'h' */
		'd', /* 'i' */
		'u', /* 'j' */
		'i', /* 'k' */
		'g', /* 'l' */
		'l', /* 'm' */
		'b', /* 'n' */
		'k', /* 'o' */
		'r', /* 'p' */
		'z', /* 'q' */
		't', /* 'r' */
		'n', /* 's' */
		'w', /* 't' */
		'j', /* 'u' */
		'p', /* 'v' */
		'f', /* 'w' */
		'm', /* 'x' */
		'a', /* 'y' */
		'q', /* 'z' */
};

int main(int argc, char *argv[])
{
	char line[256];
	char *s;
	int t = -1;
	int n = 0;
	int i;

	while((s = fgets(line, sizeof(line), stdin)) != NULL) {
		if(t < 0) {
			t = atoi(line);
			continue;
		}

		n++;

		printf("Case #%d: ", n);

		for(i = 0; line[i] >= ' '; i++) {
			if(isalpha(line[i])){
				printf("%c", trans[line[i] - 'a']);
			} else {
				printf("%c", line[i]);
			}
		}

		printf("\n");

		if(n >= t) {
			break;
		}
	}

	return 0;
}
