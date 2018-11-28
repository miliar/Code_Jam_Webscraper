#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int main() {
	char* number = new char[25];
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%s", number);
		int len = strlen(number);
		printf("Case #%d: ", i);
		if (next_permutation(number, number + len)) {
			printf("%s\n", number);
		} else {
			number[len] = '0';
			len++;
			number[len] = '\0';
			sort(number, number + len);
			int j = 0;
			while (number[j] == '0') {
				j++;
			}
			char aux = number[0];
			number[0] = number[j];
			number[j] = aux;
			printf("%s\n", number);
		}

	}
}
