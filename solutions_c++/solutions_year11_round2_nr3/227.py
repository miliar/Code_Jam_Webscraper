#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <set>

using namespace std;

int T,N,M;
int meeste = 0;
int beste[8];
int U[8];
int V[8];
int huidige[8];
set<int> verzamelingen[10];
int kamers[10][10];

bool iselement(int i, int el) {
	int aantal = verzamelingen[i].count(el);
	return (aantal > 0);
}

void swap(int &a, int &b) {
	int temp = a;
	a = b;
	b = temp;
}

void muren() {
	for (int i = 0; i < 10; i++)
		verzamelingen[i].clear();
	for (int i = 0; i < N; i++)
		verzamelingen[0].insert(i + 1);
	for (int i = 0; i < M; i++) {
		bool gevonden = false;
		int j;
		int a = U[i];
		int b = V[i];
		if (a > b)
			swap(a,b);
		for (j = 0; j < i + 1; j++) {
			if (iselement(j, a) && iselement(j, b)) {
				gevonden = true;
				break;
			}
		}
		if (!gevonden) {
			/*printf("%d %d\n", a, b);
			set<int>::iterator it;
			for (int j = 0; j < i + 1; j++) {
				for (it = verzamelingen[j].begin(); it != verzamelingen[j].end(); it++) {
					printf("%s%d", (it == verzamelingen[j].begin() ? "" : " "), *it);
				}
				printf("\n");
			}
			printf("\n");*/
			throw 'c';
		}
		set<int>::iterator it;
		bool verwijderen[8];
		for (int k = 0; k < 8; k++)
			verwijderen[k] = false;
		for (it = verzamelingen[j].begin(); it != verzamelingen[j].end(); it++) {
			if (*it > a && *it < b) {
				int value = *it;
				verwijderen[value] = true;
			}
		}
		for (int k = 0; k < 8; k++) {
			if (verwijderen[k]) {
				verzamelingen[j].erase(k);
				verzamelingen[i + 1].insert(k);
			}
			verzamelingen[i + 1].insert(a);
			verzamelingen[i + 1].insert(b);
		}
	}
	/*for (int i = 0; i < M + 1; i++) {
		set<int>::iterator it;
		for (it = verzamelingen[i].begin(); it != verzamelingen[i].end(); it++) {
			printf("%s%d", (it == verzamelingen[i].begin() ? "" : " "), *it);
		}
		printf("\n");
	}*/
	memset(kamers,0,sizeof kamers);
	for (int i = 0; i < M + 1; i++) {
		set<int>::iterator it;
		for (it = verzamelingen[i].begin(); it != verzamelingen[i].end(); it++) {
			kamers[i][*it] = 1;
		}
	}
	/*for (int i = 0; i < M + 1; i++) {
		bool eerste = true;
		for (int j = 1; j <= N; j++) {
			if (kamers[i][j] != 0) {
				printf("%s%d", (eerste ? "" : " "), j);
				eerste = false;
			}
		}
		printf("\n");
	}*/
}

void check() {
	// controleer of dit een geldige configuratie is
	int kleur[10];
	memset(kleur, 0, sizeof kleur);
	for (int i = 0; i < N; i++) {
		kleur[huidige[i]]++;
	}
	int som = 0;
	for (int i = 0; i < N; i++) {
		if (kleur[i] != 0)
			som++;
	}
	for (int i = 0; i < M + 1; i++) {
		memset(kleur, 0, sizeof kleur);
		for (int j = 0; j < N; j++) {
			if (kamers[i][j + 1] != 0)
				kleur[huidige[j]]++;
		}
		int deze = 0;
		for (int i = 0; i < N; i++) {
			if (kleur[i] != 0)
				deze++;
		}
		if (deze != som)
			return;
	}
	if (som > meeste) {
		meeste = som;
		for (int i = 0; i < N; i++) {
			beste[i] = huidige[i];
		}
	}
}

void recurs(int diepte) {
	if (diepte == N) {
		check();
		return;
	}
	for (int i = 0; i < N; i++) {
		huidige[diepte] = i;
		recurs(diepte + 1);
		// neem aan dat huidige[0] = 0
		if (diepte == 0)
			return;
	}
}

void probeerAlles() {
	recurs(0);
}

int main() {
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		meeste = 0;
		scanf("%d %d", &N, &M);
		for (int j = 0; j < M; j++) {
			scanf("%d", &(U[j]));
		}
		for (int j = 0; j < M; j++) {
			scanf("%d", &(V[j]));
		}
		muren();
		probeerAlles();
		printf("Case #%d: %d\n", i + 1, meeste);
		for (int i = 0; i < N; i++) {
			printf("%s%d", (i == 0 ? "" : " "), beste[i] + 1);
		}
		printf("\n");
	}
	return 0;
}

