#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

struct Button {
	int cislo;
	int farba;
};

int main () {
	int pocet, i, ii, pocet2, cislo, poslednyO, poslednyB, rozdielB, rozdielO, vys, pom;
	struct Button a[100];
	char farba[2];
	scanf("%d", &pocet);
	for (i = 0; i < pocet; i++) {
		scanf ("%d", &pocet2);
		for (ii = 0; ii < pocet2; ii++) {
			scanf("%s", &farba);
			scanf("%d", &cislo);
			if (farba[0] == 'O')
				a[ii].farba = 1;
			else
				a[ii].farba = 2;
			a[ii].cislo = cislo;
		}
		poslednyO = 1;
		poslednyB = 1;
		rozdielB  = 0;
		rozdielO = 0;
		vys = 0;
		for (ii = 0; ii < pocet2; ii++) {
			if (a[ii].farba == 1) {
				pom = a[ii].cislo;
				if (a[ii].cislo > poslednyO) {
					if (a[ii].cislo - rozdielO <= poslednyO)
						a[ii].cislo = poslednyO;
					else
						a[ii].cislo = a[ii].cislo - rozdielO;
					rozdielB = rozdielB + a[ii].cislo - poslednyO;
					vys = vys + a[ii].cislo - poslednyO;
					poslednyO = pom;
					rozdielO = 0;
				} else {
					if (a[ii].cislo + rozdielO >= poslednyO)
						a[ii].cislo = poslednyO;
					else
						a[ii].cislo = a[ii].cislo + rozdielO;
					rozdielB = rozdielB + poslednyO - a[ii].cislo;
					vys = vys + poslednyO - a[ii].cislo;
					poslednyO = pom;
					rozdielO = 0;
				}
				rozdielB++;
				vys++;
			}
			if (a[ii].farba == 2) {
				pom = a[ii].cislo;
				if (a[ii].cislo > poslednyB) {
					if (a[ii].cislo - rozdielB <= poslednyB)
						a[ii].cislo = poslednyB;
					else
						a[ii].cislo = a[ii].cislo - rozdielB;
					rozdielO = rozdielO + a[ii].cislo - poslednyB;
					vys = vys + a[ii].cislo - poslednyB;
					poslednyB = pom;
					rozdielB = 0;
				} else {
					if (a[ii].cislo + rozdielB >= poslednyB)
						a[ii].cislo = poslednyB;
					else
						a[ii].cislo = a[ii].cislo + rozdielB;
					rozdielO = rozdielO + poslednyB - a[ii].cislo;
					vys = vys + poslednyB - a[ii].cislo;
					poslednyB = pom;
					rozdielB = 0;
				}
				rozdielO++;
				vys++;
			}
		}
		printf("Case #%d: %d\n", i + 1, vys);
	}
	return 0;
}
