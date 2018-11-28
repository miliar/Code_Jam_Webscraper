#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int main () {
	int pocet, i, y, x, ii, iii, zle;
	char c;
	char a[100][100];
	scanf("%d", &pocet);
	for (i = 0; i < pocet; i++) {
		scanf("%d %d", &y, &x);
		c = getchar();
		for (ii = 0; ii < y+3; ii++) {
			for (iii = 0; iii < x+3; iii++) {
				a[ii][iii] = '.';
			}
		}
		for (ii = 0; ii < y; ii++) {
			for (iii = 0; iii < x; iii++) {
				scanf("%c", &a[ii][iii]);
			}
			c = getchar();
		}
		zle = 0;
		for (ii = 0; ii < y; ii++) {
			for (iii = 0; iii < x; iii++) {
				if (a[ii][iii] == '#') {
					if (a[ii][iii+1] == '#') {
						if (a[ii+1][iii] == '#') {
							if (a[ii+1][iii+1] == '#') {
								a[ii][iii] = '/';
								a[ii+1][iii] = '\\';
								a[ii+1][iii+1] = '/';
								a[ii][iii+1] = '\\';
							} else {
								zle = 1;
							}
						} else {
							zle = 1;
						}
					} else {
						zle = 1;
					}
				}
			}
		}
		printf("Case #%d:\n", i+1);
		if (zle == 1) 
			printf("Impossible\n");
		else {
			for (ii = 0; ii < y; ii++) {
				for (iii = 0; iii < x; iii++) {
					printf("%c", a[ii][iii]);
				}
				printf("\n");
			}
		}
	}
	return 0;
}
