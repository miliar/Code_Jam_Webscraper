#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

int mapa[300];

void pre(){
	for(int i = 0; i < 300; ++i) mapa[i] = i;
	
	mapa['y'] = 'a'; mapa['n'] = 'b'; mapa['f'] = 'c';
	mapa['i'] = 'd'; mapa['c'] = 'e'; mapa['w'] = 'f';
	mapa['l'] = 'g'; mapa['b'] = 'h'; mapa['k'] = 'i';
	mapa['u'] = 'j'; mapa['o'] = 'k'; mapa['m'] = 'l';
	mapa['x'] = 'm'; mapa['s'] = 'n'; mapa['e'] = 'o';
	mapa['v'] = 'p'; mapa['z'] = 'q'; mapa['p'] = 'r';
	mapa['d'] = 's'; mapa['r'] = 't'; mapa['j'] = 'u';
	mapa['g'] = 'v'; mapa['t'] = 'w'; mapa['h'] = 'x';
	mapa['a'] = 'y'; mapa['q'] = 'z';
}

void ig(){
	while(cin.peek() == '\n') cin.ignore();
}

char linha[300];
char resp[300];

int main(){
	pre();
	int casos;
	scanf( "%d", &casos );
	for(int i = 1; i <= casos; ++i ){
		ig();
		gets(linha);
		int j;
		for(j = 0; linha[j]; ++j) resp[j] = mapa[linha[j]];
		resp[j] = 0;
		
		printf( "Case #%d: %s\n", i, resp );
		
	}
	
	
}

