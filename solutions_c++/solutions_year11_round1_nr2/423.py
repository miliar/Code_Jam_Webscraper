#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <map>
#include <algorithm>
#include <utility>
#include <cmath>

using namespace std;

#define MAXN 10010

int mapa[MAXN][26];
int n, m, tam[10][MAXN], proxVaga[11], pqp[MAXN];
char in[MAXN][12], l[30];
int aindapode[MAXN], qnt, cn, letras[30];


int main(){
	int casos; scanf("%d", &casos);
	int caso = 1, passos;
	int aux, melhor, ind, novoqnt, at;
	while(casos--){
		printf("Case #%d:", caso++);
		scanf("%d%d", &n, &m);
		memset(proxVaga, 0, sizeof(proxVaga));
		for(int i = 0; i < n; ++i){
			scanf("%s", in[i]);
			aux = strlen(in[i])-1;
			pqp[i] = aux;
			tam[aux][proxVaga[aux]++] = i;
			memset(mapa[i], 0, sizeof(mapa[i]));
			for(int j = 0; j <= aux; ++j){
				mapa[i][ in[i][j]-'a' ] |= 1<<j;
			}
		}
		
		int mask;
		for(int i = 0; i < m; ++i){
			scanf("%s", l); melhor = -1;
			for(int j = 0; j < n; ++j){
				passos = 0;
				memset(letras, 0, sizeof(letras));
			//	printf("Iniciando com in[j] = %s\n", in[j]);
				qnt = 0;
				for(int k = 0; k < proxVaga[pqp[j]]; ++k) {
					if(tam[pqp[j]][k] == j) continue;
					aindapode[qnt++] = tam[pqp[j]][k];
					//printf("aindadpode[%d] = %d ", qnt, aindapode[qnt]);
				}
			//	printf("\n");
				
			//	printf("j= %d, qnt = %d\n", j, qnt);
				for(int k = 0; l[k] && qnt > 0; ++k){
				
					at = l[k]-'a';
					mask = mapa[j][at];
					novoqnt = 0;
				//	printf("letra %c\n", l[k]);
					for(int g = 0; g < qnt; ++g){
						if(mapa[aindapode[g]][at] == mask){
				//			printf("[era aindapode[%d] = %d] ",g, aindapode[g]);
							aindapode[novoqnt++] = aindapode[g];
				//			printf("aindapode[%d] = %d ", novoqnt-1, aindapode[novoqnt-1]);
						}
					}
				//	printf("fim do ainda pode\n");
					if(mask == 0 && qnt != novoqnt) ++passos;
					
				//	if(qnt != novoqnt){
				//		printf("%d: %d %d %c %d\n", j, novoqnt, passos, l[k], mask);
				//		for(int x = 0; x < novoqnt; ++x) printf("aindapode= %d;\n", aindapode[x]);
				//	}
					qnt = novoqnt;
				}
				//printf("%d: %d\n", j, passos);
				if(passos > melhor){
					melhor = passos;
					ind = j;
				}
			}
			printf(" %s", in[ind]);
		}
		printf("\n");
	}
	
	return 0;
}