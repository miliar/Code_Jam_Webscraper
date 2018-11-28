#include <cstdio>

int M;
int V;
int limite;
int G[100000];
int C[100000];

int rec(int v, int b) { // vertice com booleano desejado

	int retorno;

	if (v < limite) {
		// eh interno
		//printf("%d interno", v);
		
		if (G[v] == 1) {
			// porta AND
			
			if (b == 0) {
				// quero falso, ao menos um dos meus filhos tem que ser falso
				//printf(" and e quero falso\n");
				int ret1 = rec(v*2+1, 0);
				int ret2 = rec(v*2+2, 0);
				
				if (ret1 >= 0 && ret2 >= 0) {
					//os dois podem ser falsos
					retorno = ret1<ret2?ret1:ret2; // minimo
				} else if (ret1 >= 0) {
					retorno = ret1;
				} else if (ret2 >= 0) {
					retorno = ret2;
				} else {
					// e se eu mudar para or? adianta nada, nenhum dos dois pode ser falso...
					retorno = -1;
				}
				
			} else {
				// quero verdadeiro, ambos devem ser verdadeiros
				//printf(" and e quero verdadeiro\n");
				int ret1 = rec(v*2+1, 1);
				int ret2 = rec(v*2+2, 1);
				if (ret1 >= 0 && ret2 >= 0) {
					//os dois podem ser verdadeiros
					retorno = ret1 + ret2; // mudancas necessarias
				} else if ((ret1 >= 0 || ret2 >= 0) && C[v] == 1) {
					// basta mudar para OR
					retorno = 1 + (ret1>ret2?ret1:ret2);
				} else {
					retorno = -1;
				}
			}
			
		} else {
			// porta or
			
			if (b == 1) {
				// quero verdadeiro, ao menos um dos meus filhos tem que ser verdadeiro
				//printf(" or e quero verdadeiro\n");
				int ret1 = rec(v*2+1, 1);
				int ret2 = rec(v*2+2, 1);
				
				if (ret1 >= 0 && ret2 >= 0) {
					//os dois podem ser verdadeiros
					retorno = ret1<ret2?ret1:ret2; // minimo
				} else if (ret1 >= 0) {
					retorno = ret1;
				} else if (ret2 >= 0) {
					retorno = ret2;
				} else {
					// e se eu mudar para and? adianta nada, nenhum dos dois pode ser verdadeiro...
					retorno = -1;
				}
				
			} else {
				// quero falso, ambos devem ser falso
				//printf(" or e quero falso\n");
				int ret1 = rec(v*2+1, 0);
				int ret2 = rec(v*2+2, 0);
				if (ret1 >= 0 && ret2 >= 0) {
					//os dois podem ser falso
					retorno = ret1 + ret2; // mudancas necessarias
				} else if ((ret1 >= 0 || ret2 >= 0) && C[v] == 1) {
					// basta mudar para AND
					retorno = 1 + (ret1>ret2?ret1:ret2);
				} else {
					retorno = -1;
				}
			}
			
		}
		
	} else {
		// eh folha
		//printf("  folha (%d)  ", v);
		if (b == G[v]) {
			retorno = 0; // 0 modificacoes para atingir o que se quer
		} else {
			retorno = -1; // impossivel atingir esse valor
		}
	}
	
	//printf("%d retorna %d\n", v, retorno);
	return retorno; // so para ficar
}

void process() {
	
	int r = 0;
	r = rec(0, V);
	if (r == -1) {
		printf("IMPOSSIBLE\n");
	} else {
		printf("%d\n", r);
	}
	
}

void read() {
	scanf("%d %d", &M, &V);
	//printf("M %d  V %d\n", M, V);
	
	limite = (M-1)/2;
	for (int i = 0 ; i < limite ; i++) {
		scanf("%d %d", &G[i], &C[i]);
	}
	for (int i = limite ; i < M ; i++) {
		scanf("%d", &G[i]);
	}
	
}

int main() {
	
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("A.out", "w", stdout);
	//printf("opa\n");
	
	
	int qnt;
	scanf("%d", &qnt);
	
	for (int iM = 1 ; iM <= qnt ; iM++) {
		read();
		printf("Case #%d: ", iM);
		process();
	}

	return 0;
}
