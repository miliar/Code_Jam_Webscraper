#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>
#include <vector>
#include <map>
#include <queue>

#define num(a) ((int)(a)-48)
#define chr(a) ((char)(a+48))

using namespace std;

int nMinta[1000];
int Mintax[1000][100], Mintay[1000][100];

int main() {
	int nTC;
	int v[15];
	scanf("%d", &nTC);
	for (int kasus=1; kasus<=nTC; kasus++) {
		int nCustomer, nMilkshake;
		scanf("%d %d", &nMilkshake, &nCustomer);
		for (int i=0; i<nCustomer; i++) {
			scanf("%d", &nMinta[i]);
			for (int j=0; j<nMinta[i]; j++) {
				scanf("%d", &Mintax[i][j]);
				Mintax[i][j]--;
				scanf("%d", &Mintay[i][j]);
			}
		}
		bool finish=false;
		for (int i=0; i<=nMilkshake; i++) {
			if (finish) break;
			for (int j=0; j<nMilkshake-i; j++)
				v[j]=0;
			for (int j=nMilkshake-i; j<nMilkshake; j++)
				v[j]=1;
			do {
				if (finish) break;
				bool found=true;
				for (int j=0; j<nCustomer; j++) {
					if (!found) break;
					found=false;
					for (int k=0; k<nMilkshake; k++) {
						for (int l=0; l<nMinta[j]; l++) {
							if (Mintax[j][l]==k && Mintay[j][l]==v[k]) {
								found=true;
								break;
							}
						}
					}
				}
				if (found) {
					printf("Case #%d:", kasus);
					for (int k=0; k<nMilkshake; k++)
						printf(" %d", v[k]);
					printf("\n");
					finish=true;
					break;
				}
			} while (next_permutation(v, v+nMilkshake));
		}
		if (!finish)
			printf("Case #%d: IMPOSSIBLE\n", kasus);
	}
	return 0;
}
