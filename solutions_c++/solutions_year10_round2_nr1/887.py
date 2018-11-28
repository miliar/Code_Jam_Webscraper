/*
 *  A.cpp
 *  
 *
 *  Created by Lucas S on 5/22/10.
 *
 */

#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <map>

#define	MAX	200

using namespace std;

int main (void) {
	char linha[MAX];
	char auxiliar[MAX];
	string s;
	map<string, int> mapa;
	int i, j, k, t, n, m, resultado;
	
	scanf("%d", &t);
	for (k=1; k <= t; k++) {
		scanf("%d %d", &n, &m);
		
		mapa.clear();
		auxiliar[0] = 0;
		s = string(auxiliar);
		mapa[s] = 1;
		for (i=0; i < n; i++) {
			scanf(" %s", linha);
			for (j=0; linha[j]; j++) {
				if (linha[j] == '/') {
					strcpy(auxiliar, linha);
					auxiliar[j] = 0;
					s = string(auxiliar);
					mapa[s] = 1;
				}
				if (linha[j+1] == 0) {
					strcpy(auxiliar, linha);
					auxiliar[j+1] = 0;
					s = string(auxiliar);
					mapa[s] = 1;
				}
			}
				
		}
		
		resultado = 0;
		for (i=0; i < m; i++) {
			scanf(" %s", linha);
			for (j=0; linha[j]; j++) {
				if (linha[j] == '/') {
					strcpy(auxiliar, linha);
					auxiliar[j] = 0;
					s = string(auxiliar);
					if(mapa[s] == 0) {
						resultado++;
						mapa[s] = 1;
					}
				}
				if (linha[j+1] == 0) {
					strcpy(auxiliar, linha);
					auxiliar[j+1] = 0;
					s = string(auxiliar);
					if(mapa[s] == 0) {
						resultado++;
						mapa[s] = 1;
					}
				}
			}
		}
		
		printf("Case #%d: %d\n", k, resultado);
	}
	
	
	
	return 0;
}
