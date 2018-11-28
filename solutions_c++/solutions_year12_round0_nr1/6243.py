// 2.zadanie z TEAP 

#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <map>
// dlzka riadku
#define LEN 102
using namespace std;



int main(void){
	unsigned int n,i,j, l;
	char riadok[LEN+1];
	map<int, int> mapa;
	map<int, int>::iterator it;
	
	mapa['a'] = 'y';
	mapa['b'] = 'h';
	mapa['c'] = 'e';
	mapa['d'] = 's';
	mapa['e'] = 'o';
	mapa['f'] = 'c';
	mapa['g'] = 'v';
	mapa['h'] = 'x';
	mapa['i'] = 'd';
	mapa['j'] = 'u';
	mapa['k'] = 'i';
	mapa['l'] = 'g';
	mapa['m'] = 'l';
	mapa['n'] = 'b';
	mapa['o'] = 'k';
	mapa['p'] = 'r';
	mapa['q'] = 'z';
	mapa['r'] = 't';
	mapa['s'] = 'n';
	mapa['t'] = 'w';
	mapa['u'] = 'j';
	mapa['v'] = 'p';
	mapa['x'] = 'm';
	mapa['y'] = 'a';
	mapa['z'] = 'q';
	mapa['w'] = 'f';
	
	char **polex, **poley;
	scanf("%d",&n);
	// cyklus cez jednotlive testy
	fgets(riadok, LEN, stdin);    // zereme koniec riadku		
	polex = (char**)malloc((n+1) * sizeof(char*));
	for(j = 1; j <= n; ++j){	
		polex[j] = (char*)malloc((LEN+1) * sizeof(char));
		fgets(polex[j], LEN, stdin);
		// odstranenie znaku noveho riadku
		l = strlen(polex[j])-1;
		if(polex[j][l] == '\n')
		polex[j][l] = '\0';
		else ++l;
		//printf("Case #%d: %s\n", j, polex[j]);
		for(i = 0; i < l; ++i)
		if(polex[j][i] > 96 && polex[j][i] < 123){
		//putchar(polex[j][i]);	
		polex[j][i] = mapa[polex[j][i]];
		}
		printf("Case #%d: %s\n", j, polex[j]);
	}		
	
	return 0;
}
/*
int main(void){
	unsigned int n, i, j, c;
	scanf("%lld", &n);
	for(j = 0; j <= n; ){
		c = getchar();
		if(j == '\n'){
			printf("Case #%lld: ", j+1 );
			++j;
		}
		putchar(c);
	}		
	return 0;
}*/
