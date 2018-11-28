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
	int pocet, i, pocet2, L, H, ii, konec, iii, zle, vys;
	int a[1000];
	scanf("%d", &pocet);
	for (i = 0; i < pocet; i++) {
		scanf("%d %d %d", &pocet2, &L, &H);
		for (ii = 0; ii < pocet2; ii++) {
			scanf("%d", &a[ii]);
		}
		konec = 0;
		vys = -1;
		for (ii = L; ii <= H; ii++) {
			zle = 0;
			if (konec == 0) {
				for (iii = 0; iii < pocet2; iii++) {
					if ((a[iii] % ii != 0) && (ii % a[iii] != 0)) {
						zle = 1;
						break;
					}
				}
			}
			if (zle == 0) {
				konec = 1;
				vys = ii;
				break;
			}
		}
		if (vys == -1) {
			printf("Case #%d: NO\n", i+1);
		} else {
			printf("Case #%d: %d\n", i+1, vys);
		}
	}
	return 0;
}
