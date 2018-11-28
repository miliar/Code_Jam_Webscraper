#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

int main () {
	char tab[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	int nbCases = 0;
	char tmp = 'a';
	scanf("%d", &nbCases);
	getchar();
	for (int ij = 0; ij < nbCases; ij++) {
		tmp = 'a';
		cout << "Case #" << ij + 1 << ": ";
		while (tmp != '\n' && tmp != EOF) {
			tmp = getchar();
			if (tmp == EOF) {
				cout << '\n';
			}
			else if (tmp == ' ' || tmp == '\n') {
				cout << tmp;
			}
			else {
				tmp -= 'a';
				cout << tab[tmp];
				tmp += 'a';
			}
		}
	}
	return 0;
}
