#include <stdio.h>
#include <iostream>
#include <vector>
#include <stack>
#include <cmath>

#define scand(a) fscanf(in,"%d", &a)
#define scanc(a) fscanf(in, "%c", &a)
#define scans(a) fscanf(in,"%s", &a)
//#define forn(a,b) for(int a = 0; a < n; a++)

using namespace std;


int main() {
	FILE *in = fopen("data.in", "r");
	FILE *out = fopen("saida.in", "w");
	int cases;
	char data[100];
	char seq[1000];
	int btt[1000];
	int subcases;
	int j, k, w;
	int aux;
	int tempo;
	scand(cases);
 
	for(int i = 0;i < cases; i++) {
		scand(subcases);
		j = 0;
		tempo = 0;
		while (j < subcases) {
			scans(data);
			seq[j] = data[0];
			scand(aux);
			btt[j] = aux;
			j++;
		}
		int posb = 1, poso = 1;
		for(int ii = 0; ii < subcases; ii++) {
			if(seq[ii] == 'O') {
				tempo = abs(btt[ii]-poso)+tempo;
				tempo++; aux = poso;
				poso = btt[ii];
				k = ii+1;
				while(k < subcases) {
					if(seq[k] == 'B') {
						if(abs(posb - btt[k]) <= abs(btt[ii]-aux))
							posb = btt[k];
						else {
							if(btt[k] < posb)
								posb = posb - abs(aux-btt[ii]) - 1;
							else if (btt[k] > posb)
								posb = posb + abs(aux-btt[ii]) + 1;
							}
						break;
						}
					k++;
				}
			}
			else {
				tempo = abs(btt[ii] - posb)+ tempo;
				tempo++; aux = posb;
				posb = btt[ii];
				k = ii+1;
				while(k < subcases) {
					if(seq[k] == 'O') {
						if(abs(poso - btt[k]) <= abs(aux-btt[ii]))
							poso = btt[k];
						else {
							if(btt[k] < poso)
								poso = poso - abs(aux-btt[ii]) - 1;
							else if(btt[k] > poso)
								poso = poso + abs(aux-btt[ii]) + 1;
							}
						break;
						}
					k++;
				}
			}
		}
		fprintf(out,"Case #%d: %d\n",i+1,tempo);
	}

	system("pause");
	return 0;
}
