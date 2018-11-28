#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>

char map[26] = {
	'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'
};

int main() {
	FILE *fr = fopen("A-small-attempt1.in", "r");
	FILE *fw = fopen("A-small-attempt1.out", "w");

	int max;
	char s[1024] = { 0 }, temp[1024];

	fgets(s, 10, fr);
	max = atoi(s);

	int i, j;
	for(i=0; i<max; i++)  {
		fgets(s, sizeof(s), fr);
		for (j=0; j<strlen(s); j++) {
			if (s[j] >= 'a' && s[j] <= 'z') {
				s[j] = map[s[j]-'a'];
			}
		}
		sprintf(temp, "Case #%d: %s", i+1, s);
		fputs(temp, fw);
	}

	fclose(fw);
	fclose(fr);

	exit(0);
}