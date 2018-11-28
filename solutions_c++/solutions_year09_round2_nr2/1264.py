#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
char buffer[1000];
char neu[1000];

int
main(int argc, char **argv)
{
	int numCases;
	scanf("%d", &numCases);
	for (int i = 0; i < numCases; i++) {
		scanf("%s", buffer);
		strcpy(neu, buffer);
		if (next_permutation(buffer, buffer + strlen(buffer))) {
		} else {
			strcpy(buffer, neu);
			buffer[strlen(buffer) + 1] = '\0';
			buffer[strlen(buffer)] = '0';
			next_permutation(buffer, buffer + strlen(buffer));
			while (buffer[0] == '0') {
				next_permutation(buffer, buffer + strlen(buffer));
			}
		}
		printf("Case #%d: %s\n", i + 1, buffer);
	}

	return 0;
}
