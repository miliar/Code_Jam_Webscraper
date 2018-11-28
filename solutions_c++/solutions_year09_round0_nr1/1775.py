#include <stdio.h>
#include <string.h>

char letter[5000][16];
char line[1001];
char word[16][30];
int l, d, n;

bool contains(int i) {
	for (int j = 0; j < l; j++) {
		bool ok = false;
		for (int k = 0; word[j][k] != '\0'; k++) {
			if (letter[i][j] == word[j][k]) {
				ok = true;
				break;
			}
		}
		if (!ok)
			return false;
	}
	return true;
}

long combination() {
	long count = 0;
	for (int i = 0; i < d; i++)
		if (contains(i))
			count++;
	return count;
}

int main() {

	scanf("%d%d%d", &l, &d, &n);
	for (int i = 0; i < d; i++) {
		scanf("%s", letter[i]);
	}

	for (int i = 1; i <= n; i++) {
		scanf("%s", line);
		int k = 0;
		for (int j = 0; line[j] != '\0'; j++) {
			if (line[j] == '(') {
				j++;
				int count = 0;
				while (line[j] != ')') {
					word[k][count] = line[j];
					j++;
					count++;
				}
				word[k][count] = '\0';
			} else {
				word[k][0] = line[j];
				word[k][1] = '\0';
			}
			k++;
		}

		printf("Case #%d: %ld\n", i, combination());
	}
}
