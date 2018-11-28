#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<cstdio>

using namespace std;

int prime[1100000];
int primelist[1100000];
int pn;
int passed[1100000];
int fila[1100000];
int pos, filasize;

int main() {
	long long a, b, p, aux;
	long long aux2;
	int n;
	int minimump;
	int resp;
	int teste, t;
	int i, j;
	
	for (i=0; i<=1000000; i++){
		prime[i] = 1;
	}
	prime[0] = 0;
	prime[1] = 0;
	for (i=2; i<=1000; i++){
		if (prime[i] == 1) {
			j = 2*i;
			while (j<=1000000) {
				prime[j] = 0;
				j += i; 
			}
		}
	}
	pn = 0;
	for (i=2; i<=1000000; i++) {
		if (prime[i]) {
			primelist[pn++] = i;
		}
	}
	
	scanf("%d", &teste);
	for (t=0; t<teste; t++){
		scanf("%I64d %I64d %I64d", &a, &b, &p);
		minimump = 0;
		while(primelist[minimump] < p && minimump < pn){
			minimump++;
		}
		n = b - a + 1;
		for (i=0; i<n; i++){
			passed[i] = 0;
		}
	   	resp = 0;
		for (i=0; i<n; i++){
			if (passed[i] == 1) continue;
			filasize = 1;
			fila[0] = i;
			pos = 0;
			while(pos < filasize) {
				aux = fila[pos];
				passed[fila[pos]] = 1;
				aux = aux + a;
    			for (j=0; j<minimump; j++) {
					while(aux%primelist[j]==0)
						aux /= primelist[j];
				}
				for (j=minimump; j<pn; j++){
					aux2 = primelist[j];
	   				if (aux < aux2 * aux2) {
						if (aux == 1) break;
						if (fila[pos]>=aux){
							if (passed[fila[pos]-aux] == 0){
								fila[filasize++] = fila[pos]-aux;
							}
						}
						if (fila[pos]+aux<n){
	   	   	   	   	   	   	if (passed[fila[pos]+aux] == 0){
								fila[filasize++] = fila[pos]+aux;
							}
						}
						break;
    				}
					if (aux%aux2==0){
						while(aux%aux2==0)
							aux /= aux2;
						if (fila[pos]>=aux2){
	   	   	   	   	   	   	   if (passed[fila[pos]-aux2] == 0){
								fila[filasize++] = fila[pos]-aux2;
							}
						}
						if (fila[pos]+aux2<n){
	   	   	   	   	   	   	   if (passed[fila[pos]+aux2] == 0){
								fila[filasize++] = fila[pos]+aux2;
							}
						}
	      	   	   	}
				}
				pos++;
			}
			resp++;
		}
		printf("Case #%d: %d\n", t+1, resp);
    }
	return 0;

}

