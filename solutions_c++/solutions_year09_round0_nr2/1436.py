#include <cstdio>
#include <cstdlib>
#include <cmath>

#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <sstream>

#define dbg(a) cout << #a << " == " << a << endl
#define print(a) cout << a << endl

using namespace std;

int t, h, w;
int casos = 1;

int mapa[110][110];
int marcado[110][110];
char letras[110][110];
int vizinhos[] = {-1, 0, 0, -1, 0, 1, 1, 0};

int busca(int i, int j){
	if(marcado[i][j] >= 0) return marcado[i][j];

	int a, b;
	int minimo = INT_MAX;
	int ma, mb;

	for(int t = 0; t < 8; t += 2){
		a = i+vizinhos[t];
		b = j+vizinhos[t+1];
		
		if(a >= 0 && a < h && b >= 0 && b < w){
			if(mapa[a][b] < minimo) {
				minimo = mapa[a][b];
				ma = a;
				mb = b;
			}
		}
	}
	
	
	if(minimo < mapa[i][j]){
		marcado[i][j] = busca(ma, mb);
	} else {
		marcado[i][j] = i*1000+j;
	}

	return marcado[i][j];
}

map<int, char> m;

void process(){	
	for(int i = 0; i < h; i++){
		for(int j = 0; j < w; j++){
			busca(i, j);
		}
	}
	
	m.clear();
	char letra = 'a';
	
	for(int i = 0; i < h; i++){
		for(int j = 0; j < w; j++){
			if(!m.count(marcado[i][j])){
				m[marcado[i][j]] = letra;
				letras[i][j] = letra;
				letra++;
			} else {
				letras[i][j] = m[marcado[i][j]];
			}
		}
	}
	
	printf("Case #%d:\n", casos++);
	
	for(int i = 0; i < h; i++){
		for(int j = 0; j < w-1; j++){
			printf("%c ", letras[i][j]);
		}
		
		printf("%c\n", letras[i][w-1]);
	}
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	scanf("%d", &t);
	
	while(t--){
		scanf("%d %d", &h, &w);
		for(int i = 0; i < h; i++){
			for(int j = 0; j < w; j++){
				scanf("%d", &mapa[i][j]);
			}
		}
		
		memset(marcado, -1, sizeof(marcado));
		process();
	}
	
	return 0;
}
