#include<stdio.h>
#include<string.h>

char pos[30][30];
char dic[20][25];
int usa[30][30];
char palavra[20];
int total;
int tamDic;
int l, d, n;

int comp (char s1[], char s2[], int lim)
{
	for ( int i = 0; s1[i] != '\0' && i < lim; i++)
		if (s1[i] != s2[i])
			return 0;
	return 1;
}

int verifica ( int n ) {
	for ( int i = 0; i < d; i++) {
		if ( comp ( palavra, dic[i], n ) == 1 )
			return 1;
	}
	return 0;
}
	


int procura (void) {
	for ( int i = 0; i < d; i++) {
		if ( strcmp( palavra, dic[i] ) == 0 )
			return 1;
	}
	return 0;
}

void backtracking ( int indice ) {
	if ( indice < l ) {
		for ( int i = 0; pos[indice][i] != '\0' ; i++ ) {
			palavra[indice] = pos[indice][i];
			if (verifica (indice) == 0) continue;
			backtracking ( indice+1 );
		}
	}
	
	else {
		palavra[indice] = '\0';
		int bool1 = procura ();
		total += bool1;
		//printf("%s,",palavra);
	}
}



int main (void)
{
	int indicePos = 0, contador, aux, aberto, p;
	int caracteres[30];
	for ( p = 0; p < 20; p++) caracteres[p] = 0;
    char pega[500];
	scanf("%d %d %d", &l, &d, &n);
	//printf("%d %d %d\n",l,d,n);
	for ( contador = 1; contador <= d; contador++) {
		scanf("%s",pega);
		for ( p = 0; pega[p] != 0; p++ ) 
			if ( pega[p] >='a' && pega[p] <='z' ) caracteres[ pega[p] -'a' ] = 1;  
		//printf("palavra %d. %s\n",contador,pega);
		strcpy(dic[contador-1],pega);
	}

	//for ( contador = 0; contador <d; contador++)
		//printf("%s\n",dic[contador]);

	for ( contador = 1; contador <= n; contador++) {
		aux = 0; indicePos = 0; aberto = 0; total = 0;
		scanf("%s",pega);
		//printf(">> linha: %s... ",pega);
		//printf("%s\n",pega);
		for ( int j = 0; pega[j] != '\0'; j++ ) {
			//printf("%c", pega[j]);
			//printf("pegando... %c\n",pega[j]);
			if ( pega[j] == ')' ) { aberto = 0; }
			else { 
				if (pega[j]=='(') { aberto = 1; continue; }
				//else if ( pega[j] >= 'a' && pega[j]<= 'z') 
				else if ( pega[j] >= 'a' && pega[j]<= 'z' && caracteres[pega[j]-'a'] == 1) 
					{ pos[indicePos][aux] = pega[j];  aux+=1; }
			}
			
			if ( aberto == 0 ) { pos[indicePos][aux] = '\0'; indicePos+=1; aux = 0; }
		}
 

		/*for ( int k = 0; k < indicePos; k++) {
			for ( int r = 0; pos[k][r] !='\0'; r++)
				printf("%c", pos[k][r]);
			printf("|"); }
		printf("\n"); */

		backtracking(0);
		printf("Case #%d: %d\n",contador,total);
					
	}
	
	return 0;
}
		
