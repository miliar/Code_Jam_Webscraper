#include <cstdio>
#include <cstring>


int L,D,N;

struct No {
	int filhos[28];
};

No arvore[760000];
int qtdNos;

int novoNo() {
	memset(arvore[qtdNos].filhos, -1, sizeof(arvore[qtdNos].filhos));
	return qtdNos++;
}

char input[10000];

int calc(int letra, int i, int no) {
	if (letra == L) {
		return 1;
	} else {
		// verifica se tem a letra-ésima letra na posição i
		if (input[i] == '(') {
			int i2 = i+1;
			while (input[i2] != ')') {
				i2++;
			}
			
			int res = 0;
			for (int k = i+1 ; k < i2 ; k++) {
				if (arvore[no].filhos[input[k]-'a'] != -1) {
					res += calc(letra+1, i2+1, arvore[no].filhos[input[k]-'a']);
				}
			}
			
			
			return res;
			
		} else {
			
			if (arvore[no].filhos[input[i]-'a'] != -1) {
				int res = calc(letra+1, i+1, arvore[no].filhos[input[i]-'a']);
				
				return res;
			} else {
				return 0;
			}
			
		}
	}
	
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	scanf("%d%d%d", &L, &D, &N);
	qtdNos = 0;
	novoNo(); // o primeiro nó é a raiz
	int no;
	for (int i = 0 ; i < D ; i++) {
		scanf("%s", input);
		no = 0;
		for (int j = 0 ; input[j] ; j++) {
			if (arvore[no].filhos[input[j]-'a'] == -1) {
				arvore[no].filhos[input[j]-'a'] = novoNo();
			}
			no = arvore[no].filhos[input[j]-'a'];
		}
	}
	
	int resposta;
	for (int i = 1 ; i <= N ; i++) {
		scanf("%s", input);
		resposta = calc(0,0,0);
		
		printf("Case #%d: %d\n", i, resposta);
	}
	
	return 0;
}
