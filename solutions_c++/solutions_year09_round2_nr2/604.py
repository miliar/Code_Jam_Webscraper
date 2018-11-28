#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;
char line[25];

int main(int argc, char **argv) {
	int nTests;
	scanf("%d", &nTests);
	fgets(line, 22, stdin);
	for (int i = 1; i <= nTests; ++i) {
		fgets(line, 23, stdin);
		line[strlen(line)-1] = 0;
		if (!next_permutation(line, line+strlen(line))) {
			int zeroes = 0;
			while (line[zeroes] == '0') {
				++zeroes;
			}
			printf("Case #%d: ", i);
			printf("%c", line[zeroes]);
			for (int i = 0; i <= zeroes; ++i) {
				printf("%d", 0);
			}
			printf("%s\n", line+zeroes+1);
		} else {
			printf("Case #%d: %s\n", i, line);
		}
	}
}
