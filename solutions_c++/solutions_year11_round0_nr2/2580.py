/*
 * magicka.cpp
 *
 *  Created on: 07/05/2011
 *      Author: a200810283725
 */
#include <stdio.h>
struct pair {
	char x;
	char y;
	char z;
};

int t, c, d, n;
char invoke[100];
int sinvoke = 0;
struct pair comb[36];
struct pair ops[28];

int main() {
	scanf("%d\n", &t);
	int test = 0;
	while(test++<t) {
		scanf("%d ", &c);
		struct pair alce;
		int pc = -1, pd = -1;
		while(++pc<c)
			scanf("%c%c%c ", &comb[pc].x, &comb[pc].y, &comb[pc].z);
		scanf("%d ", &d);
		while(++pd<d)
			scanf("%c%c ", &ops[pd].x, &ops[pd].y);

		scanf("%d ", &n);
		sinvoke = n;
		char m;
		int j=0, k=0;
		while(j++<n) {
			scanf("%c", &m);
			invoke[k] = m;
			for(int i=0; i<c; i++) {
				if(k>0 && ((invoke[k-1] == comb[i].x && invoke[k] == comb[i].y) || (invoke[k-1] == comb[i].y && invoke[k] == comb[i].x))) {
					invoke[k-1] = comb[i].z;
					k--;
					break;
				}
			}
			int w = k;
			k++;
			for(int i=0; i<w; i++) {
				for(int l=0; l<d; l++) {
					if((invoke[i] == ops[l].x && invoke[w] == ops[l].y)
							|| (invoke[i] == ops[l].y && invoke[w] == ops[l].x)) {
						k=0;
					}
				}
			}
		}
		printf("Case #%d: [", test);
		for(j=0; j<k; j++) {
			printf("%c", invoke[j]);
			if(j<k-1)
				printf(", ");
		}
		printf("]\n");
	}
}



