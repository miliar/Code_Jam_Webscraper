#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

struct Spoj {
	char vysledok;
	int surovina1, surovina2;
};

struct Znic {
	int surovina1, surovina2;
};

int nacislo (char a) {
	int i = -1;
	if (a == 'Q')
		i = 0;
	if (a == 'W')
		i = 1;
	if (a == 'E')
		i = 2;
	if (a == 'R')
		i = 3;
	if (a == 'A')
		i = 4;
	if (a == 'S')
		i = 5;
	if (a == 'D')
		i = 6;
	if (a == 'F')
		i = 7;
	return i;
}

int main () {
	int pocet, i, ii, iii, pocet2, pocet3, pocet4, huh2, posledny, pom, spoj, znic, iiii;
	int c[10];
	struct Spoj a[100];
	struct Znic b[100];
	char vys[200];
	char huh;
	scanf("%d", &pocet);
	for (i = 0; i < pocet; i++) {
		scanf("%d", &pocet2);
		for (ii = 0; ii < pocet2; ii++) {
			huh = getchar();
			a[ii].surovina1 = nacislo(getchar());
			a[ii].surovina2 = nacislo(getchar());
			a[ii].vysledok = getchar();	
		}
		scanf("%d", &pocet3);
		for (ii = 0; ii < pocet3; ii++) {
			huh = getchar();
			b[ii].surovina1 = nacislo(getchar());
			b[ii].surovina2 = nacislo(getchar());
		}
		scanf("%d", &pocet4);
		huh = getchar();
		posledny = -1;
		pom = 0;
		for (ii = 0; ii < 8; ii++) {
			c[ii] = 0;
		}
		for (ii = 0; ii < pocet4; ii++) {
			huh = getchar();
			huh2 = nacislo(huh);
			spoj = 0;
			znic = 0;
			if (ii > 0) {
				for (iii = 0; iii < pocet2; iii++) {
					if ((a[iii].surovina1 == posledny) && (a[iii].surovina2 == huh2)) {
						pom--;
						vys[pom] = a[iii].vysledok;
						pom++;
						posledny = -1;
						spoj = 1;
						c[a[iii].surovina1]--;
					}
					if ((a[iii].surovina2 == posledny) && (a[iii].surovina1 == huh2)) {
						pom--;
						vys[pom] = a[iii].vysledok;
						posledny = -1;
						pom++;
						spoj = 1;
						c[a[iii].surovina2]--;
					}
				}
			}
			if ((ii > 0) && (spoj == 0)) {
				for (iii = 0; iii < pocet3; iii++) {
					if (b[iii].surovina1 == huh2) {
						if (c[b[iii].surovina2] > 0) {
							pom = 0;
							posledny = -1;
							znic = 1;
							for (iiii = 0; iiii < 8; iiii++) {
								c[iiii] = 0;
							}
						}
					}
					if (b[iii].surovina2 == huh2) {
						if (c[b[iii].surovina1] > 0) {
							pom = 0;
							posledny = -1;
							znic = 1;
							for (iiii = 0; iiii < 8; iiii++) {
								c[iiii] = 0;
							}
						}
					}
				}
			}
			if ((spoj == 0) && (znic == 0)) {
				vys[pom] = huh;
				pom++;
				posledny = huh2;
				c[huh2]++;
			}
		}
		printf("Case #%d: [", i + 1);
		for (ii = 0; ii < pom; ii++) {
			if (ii < pom - 1)
				printf("%c, ", vys[ii]);
			else
				printf("%c", vys[ii]);
		}
		printf("]\n");
	}
	return 0;
}
