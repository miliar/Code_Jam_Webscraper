#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

int main () {
	int nbCases = 0, nbGooglers = 0, surprisingCases = 0, p = 0, answer = 0;
	int tmp = 0;
	scanf("%d", &nbCases);
	getchar();
	for (int i = 0; i < nbCases; i++) {
		scanf ("%d %d %d", &nbGooglers, &surprisingCases, &p);
		answer = 0;
		for (int j = 0; j < nbGooglers; j++) {
			scanf("%d", &tmp);
			if (tmp >= 3*p - 2) {
				answer++;
			}
			else if (tmp >= p  && tmp >= 3*p - 4 && surprisingCases > 0) {
				answer++;
				surprisingCases--;
			}
		}
		printf("Case #%d: %d\n", i+1, answer);
	}
	return 0;
}
