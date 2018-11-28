#include <cstdio>

using namespace std;
char rijeci[5001][16];
bool ima[15][200];
char trenutna[1000];
int l, d, n;

int main() {
	scanf("%d %d %d", &l, &d, &n);
	for (int i = 0; i < d; i++) scanf(" %s", rijeci[i]);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < 15; j++)
			for (int k = 0; k < 200; k++) ima[j][k] = false;
		scanf(" %s", trenutna);
		int pok = 0;
		for (int j = 0; j < l; j++) {
			if (trenutna[pok] != '(') {
				ima[j][ trenutna[pok] ] = true;
				pok++;
				continue;
			}
			pok++;
			while (trenutna[pok] != ')') {
				ima[j][ trenutna[pok] ] = true;
				pok++;
			}
			pok++;
		}
		int brojac = 0;
		for (int j = 0; j < d; j++) {
			brojac++;
			for (int k = 0; k < l; k++) if (!ima[k][ rijeci[j][k] ]) {brojac--; break;}
		}
		printf("Case #%d: %d\n", i+1, brojac);
	}

	return 0;
}