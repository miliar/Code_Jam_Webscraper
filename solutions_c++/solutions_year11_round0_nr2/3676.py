#include <stdio.h>
#include <string.h>

int t;
int c, d, n;
char combA, combB, combC;
char temp;

char combinaciones[100][100];
char contrarios[100];
char utilizados[100];

char lista[102];
int nLista;

bool huboCombinacion;
bool huboContrario;

int convertirLetraANumero(char dato){
	return dato - 'A' + 1;
}

char convertirNumeroALetra(int dato){
	return dato + 'A' - 1;
}


void limpiar(){
	memset(combinaciones, 0, 10000);
	memset(contrarios, 0, 100);
	memset(utilizados, 0, 100);
	nLista = 0;
}

int main(){
	scanf("%d", &t);
	for(int i = 1; i <= t; i++){
		limpiar();
		scanf("%d", &c);
		for(int j = 1; j <= c; j++){
			scanf(" %c%c%c", &combA, &combB, &combC);
			combinaciones[combA][combB] = combC;
			combinaciones[combB][combA] = combC;
		}
		scanf("%d", &d);
		for(int j = 1; j <= d; j++){
			scanf(" %c%c", &combA, &combB);
			contrarios[combA] = combB;
			contrarios[combB] = combA;
		}
		scanf("%d", &n);
		for(int j = 1; j <= n; j++){
			huboCombinacion = false;
			huboContrario = false;
			scanf(" %c", &temp);
			//checamos combinaciones
			if(nLista > 0 && combinaciones[temp][lista[nLista]] != 0){
				utilizados[lista[nLista]]--;
				lista[nLista] = combinaciones[temp][lista[nLista]];
				huboCombinacion = true;
			}
			//checamos contrarios
			if(!huboCombinacion && utilizados[contrarios[temp]] > 0){
				huboContrario = true;
				memset(utilizados, 0, 100);
				nLista = 0;
			}
			//añadimos a la lista
			if(!huboCombinacion && !huboContrario){
				lista[++nLista] = temp;
				utilizados[temp]++;
			}
		}
		
		printf("Case #%d: [", i);
		for(int j = 1; j < nLista; j++){
			printf("%c, ", lista[j]);
		}
		if(nLista > 0)
			printf("%c", lista[nLista]);
		printf("]\n");
	}
	return 0;
}