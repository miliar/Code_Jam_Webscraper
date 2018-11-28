#include <stdio.h>
#include <string.h>
#include <queue>

using namespace std;

int main(){
	queue <int> Fila, Q;
	int T, R, k, N, G;
	int caso = 1, i, j, monedas, temp;
	
	scanf("%d", &T);
	while(T > 0){
		scanf("%d %d %d", &R, &k, &N);
		for(i = 0; i < N; i++){
			scanf("%d", &G);
			Fila.push(G);
		}
		monedas = temp = 0;
		for(i = 0; i < R; i++){
			G = Fila.front();
			temp = 0;
			while(!Fila.empty() && temp + G <= k){
				Fila.pop();
				Q.push(G);
				temp += G;
				monedas += G;
				G = Fila.front();
			}
			while(!Q.empty()){
				Fila.push(Q.front());
				Q.pop();
			}
		}
		printf("Case #%d: %d\n", caso++, monedas);
		T--;
		while(!Fila.empty()) Fila.pop();
	}
	return 0;
}
