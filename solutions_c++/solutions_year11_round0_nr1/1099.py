#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <map>
#include <algorithm>
#include <utility>
#include <cmath>

using namespace std;


int mark[101][101][101], n, ps[101], cn, range[3] = {0, 1, -1};
char ac[101];
struct state{
	int seq, ato, atb, passos;
	state(){}
	state(int seq, int ato, int atb, int passos):seq(seq), ato(ato), atb(atb), passos(passos){}
}atual;

int bfs(){
	queue<state> fila;
	
	mark[0][1][1] = cn;
	fila.push(state(0, 1, 1, 0));
	int auxo, auxb;
	while(!fila.empty()){
		atual = fila.front();
		if(atual.seq == n) return atual.passos;
		fila.pop();
		
		if(ac[atual.seq] == 'O'){
			if(atual.ato == ps[atual.seq]){
				for(int i = 0; i < 3; ++i){
					auxb = atual.atb + range[i];
					if(auxb >= 1 && auxb <= 100 && mark[atual.seq+1][atual.ato][auxb] != cn){
						mark[atual.seq+1][atual.ato][auxb] = cn;
						fila.push(state( atual.seq+1, atual.ato, auxb, atual.passos+1 ));
					}
				}
				goto cont;
			}
		} else if( ac[atual.seq] == 'B' ) {
			if(atual.atb == ps[atual.seq]){
				for(int i = 0; i < 3; ++i){
					auxo = atual.ato + range[i];
					if(auxo >= 1 && auxo <= 100 && mark[atual.seq+1][auxo][atual.atb] != cn){
						mark[atual.seq+1][auxo][atual.atb] = cn;
						fila.push(state( atual.seq+1, auxo, atual.atb, atual.passos+1 ));
					}
				}
				goto cont;
			}
		}
		
		for(int i = 0; i < 3; ++i){
			auxo = atual.ato + range[i];
			if(auxo >= 1 && auxo <= 100){
				for(int j = 0; j < 3; ++j){
					auxb = atual.atb + range[j];
					if(auxb >= 1 && auxb <= 100){
						if(mark[atual.seq][auxo][auxb] != cn){
							mark[atual.seq][auxo][auxb] = cn;
							fila.push(state(atual.seq, auxo, auxb, atual.passos+1));
						}
						
						
					}
				}
			}
		}
		
		
		cont:;
	}
	
	
	
}


int main(){
	int caso = 0;
	int casos; scanf("%d", &casos);
	char in[10];
	while(casos--){
		scanf("%d", &n);
		for(int i = 0; i < n; ++i){
			scanf("%s %d", in, &ps[i]);
			ac[i] = in[0];
		}
		++cn;
		printf("Case #%d: %d\n", ++caso, bfs());
	}
	
	
	return 0;
}