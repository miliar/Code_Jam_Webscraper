#include <cstdio>
#include <cstring>

char nomes[105][105];
bool marcados[105];
int S, Q;

void read() {
	scanf("%d ", &S);
	for (int i = 0 ; i < S ; i++) {
		gets(nomes[i]);
	}
}

char query[105];
int index() {
	int i = 0;
	while (strcmp(query, nomes[i]) != 0 && i < S) i++;
	return i;
}

int marquei;
int indice;
int resposta;

void process() {
	memset(marcados, false, sizeof(marcados));
	
	scanf("%d ", &Q);
	marquei = 0;
	resposta = 0;
	
	for (int i = 0 ; i < Q ; i++) {
		gets(query);
		indice = index();
		if (!marcados[indice]) {
			
			if (marquei == S - 1) {
			
				resposta++;
				marquei = 1;
				memset(marcados, false, sizeof(marcados));
				marcados[indice] = true;
			
			} else {
			
				marcados[indice] = true;
				marquei++;
			}
			
		}
	}
	printf("%d\n", resposta);
}

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	//freopen("A.in", "r", stdin);
	//freopen("A.out", "w", stdout);
	
	int qnt;
	scanf("%d ", &qnt);
	
	for (int i = 1 ; i <= qnt ; i++) {
		read();
		printf("Case #%d: ", i);
		process();
	}
	
	return 0;
}
