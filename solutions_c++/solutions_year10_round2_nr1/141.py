#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <string>
#include <map>
#include <sstream>

using namespace std;

int N, M;
string dirAntes[210][210];
int qtdDirAntes[210];
string dirDepois[210][210];
int qtdDirDepois[210];

struct No {
	string nome;
	map<string,int> filhos;
};

char temp[210];
string tempStr;
No arv[4000100];
int prox;

int total;

void tiraTracos() {
	int tam = strlen(temp);
	for (int i = 0; i < tam; i++) {
		if (temp[i] == '/') {
			temp[i] = ' ';
		}
	}
}

void read() {
	scanf("%d%d", &N, &M);
	
	for (int i = 0; i < N; i++) {
		scanf("%s", temp);
		tiraTracos();
		
		qtdDirAntes[i] = 0;
		istringstream s(temp);
		while (s >> tempStr) {
			dirAntes[i][qtdDirAntes[i]++] = tempStr;
		}
	}
	
	for (int i = 0; i < M; i++) {
		scanf("%s", temp);
		tiraTracos();
		
		qtdDirDepois[i] = 0;
		istringstream s(temp);
		while (s >> tempStr) {
			dirDepois[i][qtdDirDepois[i]++] = tempStr;
		}
	}
}

void criarArvore() {
	arv[0].nome = "";
	arv[0].filhos.clear();
	
	prox = 1;
	
	for (int i = 0; i < N; i++) {
		int ind = 0;
		for (int j = 0; j < qtdDirAntes[i]; j++) {
			
			if (arv[ind].filhos.find(dirAntes[i][j]) == arv[ind].filhos.end()) {
			    //printf("criando %d %s\n", i, dirAntes[i][j].c_str());
				arv[ind].filhos[dirAntes[i][j]] = prox;
				
				arv[prox].nome = dirAntes[i][j];
				arv[prox++].filhos.clear();
				
			}
			ind = arv[ind].filhos[dirAntes[i][j]];
			
		}
	}
}

void contar() {
	total = 0;
	
	for (int i = 0; i < M; i++) {
		int ind = 0;
		for (int j = 0; j < qtdDirDepois[i]; j++) {
			
			if (arv[ind].filhos.find(dirDepois[i][j]) == arv[ind].filhos.end()) {
			    //printf("criando depois %d %s\n", i, dirDepois[i][j].c_str());
				arv[ind].filhos[dirDepois[i][j]] = prox;
				
				arv[prox].nome = dirDepois[i][j];
				arv[prox++].filhos.clear();
				total++;
			}
			ind = arv[ind].filhos[dirDepois[i][j]];
			
		}
	}
}

void process() {
	criarArvore();
	
	contar();
	printf("%d\n", total);
}

int main() {
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int casos;
	scanf("%d", &casos);
	
	for (int i = 1; i <= casos; i++) {
		printf("Case #%d: ", i);
		read();
		process();
	}
	
	return 0;
}

