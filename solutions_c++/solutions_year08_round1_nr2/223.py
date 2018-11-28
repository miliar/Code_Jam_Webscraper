#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <cstdlib>

using namespace std;


int N, M;

struct Sabor {
	int n;
	bool malted;
};

vector<Sabor> lista[2005];
int querMaltado[2005]; // -1 se nao quiser, o N com o sabor do maltado
int qtdSabores[2005];
bool maltado[2005];

vector<int> queremNormal[2005];

void read() {
	int X, Y;
	scanf("%d %d", &N, &M);
	//printf("%d %d\n", N, M);
	
	for (int i = 0 ; i < N ; i++) {
		queremNormal[i].clear();
		maltado[i] = false;
	}
	
	for (int i = 0 ; i < M ; i++) {
		querMaltado[i] = -1;
		scanf("%d", &qtdSabores[i]);
		lista[i].clear();
		for (int j = 0 ; j < qtdSabores[i] ; j++) {
			scanf("%d %d", &X, &Y);
			X--;
			Sabor s;
			s.n = X;
			s.malted = Y == 1;
			if (!s.malted) {
				queremNormal[X].push_back(i);
			} else {
				// o maltado do cara!
				querMaltado[i] = X;
			}
			lista[i].push_back(s);
		}
	}
}



void process(int caso) {
	
	bool vai = true;
	
	while (vai) {
		vai = false;
		for (int i = 0 ; i < M ; i++) {
			//printf("qnt -> %d\n", qtdSabores[i]);
			if (qtdSabores[i] == 0) {
				// acho que deu em merda
				//printf("Case #%d: IMPOSSIBLE\n", caso);
				//return;
				
				// pensando melhor, o cara esta satisfeito
				
			} else if (qtdSabores[i] == 1) {
				// sera que eh maltado?
				//printf("opa? - \n");
				
				if (lista[i][0].malted) {
					//printf("opa! \n");
					// eita, esse cara soh vai querer maltado agora
					// td mundo que queria normal vai se lascar
					vai = true;
					int sabor = lista[i][0].n;

					maltado[sabor] = true;
					qtdSabores[i] = 0; // o cara esta satisfeito
					
					for(vector<int>::iterator it = queremNormal[sabor].begin(); it != queremNormal[sabor].end(); it++) {
						int cliente = *it;
						
						if (querMaltado[cliente] == sabor) {
							// satisfeito!
							qtdSabores[cliente] = 0;
							continue;
						}
						
						 // pula o caso de qtdSabores[cliente == 0, onde o cara estaria satisfeito
						for (int ind = 0 ; ind < qtdSabores[cliente] ; ind++) {
							if (lista[cliente][ind].n == sabor) {
								/*if (lista[cliente][ind].malted) { // isso nao acontece mais
									// satisfeito!
									qtdSabores[cliente] = 0;
									break;
								} else {*/
									lista[cliente].erase(lista[cliente].begin()+ind);
									qtdSabores[cliente]--;
									if (qtdSabores[cliente] == 0) {
										// sempre insatisfeito
										printf("Case #%d: IMPOSSIBLE\n", caso);
										return;
									} else {
										// continua pra ver se ele nao quer o malted
										break; // ja tirou o desmaltado dele
									}
								//}
							}
						}

						
						
					}

					
				}
				
			}
			
		}
		
	}
	
	printf("Case #%d:", caso);
	for (int i = 0 ; i < N ; i++) {
		if (maltado[i]) {
			printf(" 1");
		} else {
			printf(" 0");
		}
	}
	printf("\n");
}

int main () {
	
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	int qnt;
	scanf("%d", &qnt);
	
	for (int iMain = 0 ; iMain < qnt ; iMain++) {
		read();
		process(iMain+1);
	}
	
	return 0;
}
