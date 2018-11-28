#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int cuk[1100][25];

void nastring(int i, int cislo) {
	int ii, pom;
	for (ii = 0; ii < 22; ii++) {
		pom = cislo % 2;
		cuk[i][21 - ii] = pom;
		cislo = cislo/2;
	}
}

int main () {
	int pocet, i, ii, iii, pocet2, cislo, min, vys, konec;
	int poc[22];
	scanf("%d", &pocet);
	for (i = 0; i < pocet; i++) {
		scanf("%d", &pocet2);
		vys = 0;
		min = 10000001;
		for (ii = 0; ii < pocet2; ii++) {
			scanf("%d", &cislo);
			nastring(ii, cislo);
			vys = vys + cislo;
			if (cislo < min)
				min = cislo;
		}
		for (iii = 0; iii < 22; iii++) {
			poc[iii] = 0;
		}
		for (ii = 0; ii < pocet2; ii++) {
			for (iii = 0; iii < 22; iii++) {
				poc[iii] = poc[iii] + cuk[ii][iii];
			}
		}
		konec = 0;
		for (iii = 0; iii < 22; iii++) {
			if (poc[iii] % 2 == 1)
				konec = 1;
		}
		if (konec == 1)
			printf("Case #%d: NO\n", i + 1);
		else {
			printf("Case #%d: %d\n", i + 1, vys - min);
		}
	}
	return 0;
}
