#include <iostream>
#include <stdio.h>

using namespace std;

int pot[] = {2, 4, 8};

int main(int argc, char *argv[]) {
	
	int t, a, b;
	cin >> t;
	
	for(int caso = 1; caso <= t; ++ caso){
		cin >> a >> b;
		float prob_i[a];
		for(int i = 0; i < a ; ++ i)
			cin >> prob_i[i];
		
		float prob_total[pot[a-1]];
		
		//Cargo las probabilidades de cada error
		for(int i = 0; i < pot[a-1]; ++ i){
			int aux = i;
			prob_total[i] = 1;
			for(int j = 0; j < a; ++ j){
				(aux % 2) ? prob_total[i] *= prob_i[a-j-1] : prob_total[i] *= (1 - prob_i[a-j-1]);
				aux = aux >> 1;
			}
		}
		
		//La tabla
		int n = a + 2;
		int m = pot[a-1];
		int tabla[n][m];
		for(int i = 0; i < n - 2; ++ i){
			int j;
			for(j = 0; j < m - 1 - i; ++ j)
				tabla[i][j] = 2*b - a + 2*i + 2;
			for(j; j < m; ++ j)
				tabla[i][j] = b - a + 1 + 2*i;
		}
		for(int j = 0; j < m; ++j)
			tabla[n-2][j] = b - a + 1 + 2*(n-2);
		for(int j = 0; j < m; ++j)
			tabla[n-1][j] = b + 2;
		
		
		//Los totales
		float optimo = 0;
		for(int i  = 0; i < m; ++ i)
			optimo += prob_total[i] * (float) tabla[0][i];
		
		
		float candidato;
		for(int i = 1; i < n; ++ i){
			candidato = 0;
			for(int j = 0; j < m; ++ j)
				candidato += prob_total[j] * (float) tabla[i][j];

			if(candidato < optimo)
				optimo = candidato;
		}
		
		printf("Case #%d: %.6f\n",caso, optimo);
		
	}
	
	
	return 0;
}

