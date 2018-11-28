#include <cstdio>

#define MAX_SABORES 10
#define MAX_CLIENTES 100
#define INFINITO 0x3f3f3f3f

using namespace std;

class cliente {

public:
	int qt;
	int sabores[MAX_SABORES];
	int malted[MAX_SABORES];

} clientes[MAX_CLIENTES];

int n_clientes;
int n_sabores;


int satisfaz (int n) {

	int i, j;
       
	for (i=0; i<n_clientes; ++i) {
		for (j=0; j<clientes[i].qt; ++j) {

			if (clientes[i].malted[j]==0 && !( n&(1<<clientes[i].sabores[j]) )) {
				break;
			}
			if (clientes[i].malted[j]==1 && n&(1<<clientes[i].sabores[j])) {
				break;
			}

		}
		if (j==clientes[i].qt)
			return 0;
	}

	return 1;
}

int conta_uns (int n) {
	int i, sum=0;

	for (i=0; i<n_sabores; ++i) {

		if (n&(1<<i))
			sum++;

	}
	return sum;
}

void imprime (int n) {
	int i;

	for (i=n_sabores-1; i>=0; --i) {
		if (n&(1<<(n_sabores-i-1)))
			printf("1");
		else
			printf("0");
		if (i)
			printf(" ");
	}
}

int main (void) {

	int n, m;
	int i, j;
	int casos, k;
	int c;

	scanf("%d", &casos);
	for (k=1; k<=casos; ++k) {

		scanf("%d %d", &n, &m);
		n_sabores=n;
		n_clientes=m;

		for (i=0; i<m; ++i) {

			scanf("%d", &clientes[i].qt);
			for (j=0; j<clientes[i].qt; ++j) {
				scanf("%d %d", &clientes[i].sabores[j], &clientes[i].malted[j]);
				clientes[i].sabores[j]--;
			}

		}

		int qt_malted = INFINITO;
		int escolhido;
		for (i=0; i<(1<<n); ++i) {

			if (satisfaz(i)) {
				c = conta_uns(i);
				if (c<qt_malted) {
					qt_malted=c;
					escolhido=i;
				}
			}

		}

		printf("Case #%d: ", k);
		if (qt_malted < INFINITO)
			imprime (escolhido);
		else
			printf("IMPOSSIBLE");
		printf("\n");

	}

	return 0;
}
