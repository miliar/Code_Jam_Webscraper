#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>

#include <vector>
#include <algorithm>
#include <complex>
#include <assert.h>
#include <queue>

using namespace std;

char list[] = {
	'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'
};

int main (void)
{
	int T;
	int i;
	char c;

	scanf ("%d%*c", &T);
	while (1) {
		scanf ("%c", &c);
		if (c == EOF) { exit(1); }
		if (c != '\r' && c != '\n') {
			break;
		}
	}
	for (i = 1; i <= T; i++) {
		printf ("Case #%d: ", i);
		while (1) {
			if (c == ' ') {putchar (' '); }
			else {putchar (list[c-'a']); }
			if (scanf ("%c", &c) == -1) { exit (1); }
			if (c == '\r' || c == '\n') {
				while (1) {
					if (scanf ("%c", &c) == -1) { exit(1); }
					if (c != '\r' && c != '\n') {
						break;
					}
				}
				break;
			}
		}
		putchar ('\n');
	}

	return 0;
}

