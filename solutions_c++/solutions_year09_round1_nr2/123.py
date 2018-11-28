#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <algorithm>
#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <queue>
#include <string>
#include <set>
#include <bitset>
#include <stack>

#define dbg(a) //cout << #a << " = " << a << endl
#define print(a) //cout << a << endl

using namespace std;

int n, m, casos = 1;
int s[20][20];
int w[20][20];
int t[20][20];
int marcado[20][20][4][4];

enum dir{
	N, S, L, O
};

struct no{
	int i, j;
	dir dv, dh;
	long long tempo;
};

queue<no> fila;

#define mini(a, b) a < b ? a : b

int busca(){
	no temp, atual;
	int minimo = 0x3f3f3f3f;
	long long dif, tem;
	
	atual.i = n-1;
	atual.j = 0;
	atual.dv = N;
	atual.dh = L;
	atual.tempo = 0;
	
	fila.push(atual);
	while(!fila.empty()){
		dbg(atual.i);
		dbg(atual.j);
		dbg(atual.dv);
		dbg(atual.dh);
		dbg(atual.tempo);
		
		atual = fila.front();
		fila.pop();
		
		if(marcado[atual.i][atual.j][atual.dv][atual.dh] > atual.tempo){
			marcado[atual.i][atual.j][atual.dv][atual.dh] = atual.tempo;
			
			if(atual.i == 0 && atual.j == m-1 && atual.dv == S && atual.dh == O){
				minimo = mini(minimo, atual.tempo);
			} else {
				print("entrou");
				dif = atual.tempo - t[atual.i][atual.j];
				
				if(dif < 0){
					tem = -dif;
					dif += (1 + tem/(s[atual.i][atual.j] + w[atual.i][atual.j]))*(s[atual.i][atual.j] + w[atual.i][atual.j]);
				}
				
				dif = dif%(s[atual.i][atual.j] + w[atual.i][atual.j]);
				
				if(atual.dv == N){
					print("N");
					temp.i = atual.i;
					temp.j = atual.j;
					temp.dv = S;
					temp.dh = atual.dh;
					
					temp.tempo = atual.tempo + 1 + (dif < s[atual.i][atual.j] ? 0 : w[atual.i][atual.j]+s[atual.i][atual.j] - dif);
					if(marcado[temp.i][temp.j][temp.dv][temp.dh] > temp.tempo) fila.push(temp);
					
					if(atual.i < n-1){
						temp.i = atual.i+1;
						temp.tempo = atual.tempo + 2;
						
						if(marcado[temp.i][temp.j][temp.dv][temp.dh] > temp.tempo) fila.push(temp);
					}
				} else if(atual.dv == S){
					print("S");
					temp.i = atual.i;
					temp.j = atual.j;
					temp.dv = N;
					temp.dh = atual.dh;
					
					temp.tempo = atual.tempo + 1 + (dif < s[atual.i][atual.j] ? 0 : w[atual.i][atual.j]+s[atual.i][atual.j] - dif);
					if(marcado[temp.i][temp.j][temp.dv][temp.dh] > temp.tempo) fila.push(temp);
					
					if(atual.i > 0){
						temp.tempo = atual.tempo + 2;
						temp.i = atual.i - 1;
						if(marcado[temp.i][temp.j][temp.dv][temp.dh] > temp.tempo) fila.push(temp);
					}
				} 
				
				if(atual.dh == L){
					print("L");
					temp.i = atual.i;
					temp.j = atual.j;
					temp.dv = atual.dv;
					temp.dh = O;
					
					if(atual.j > 0){
						temp.j = atual.j - 1;
						temp.tempo = atual.tempo + 2;
						if(marcado[temp.i][temp.j][temp.dv][temp.dh] > temp.tempo) fila.push(temp);
					}
					
					temp.j = atual.j;
					temp.tempo = atual.tempo + 1 + (dif > s[atual.i][atual.j] ? 0 : s[atual.i][atual.j] - dif);
					if(marcado[temp.i][temp.j][temp.dv][temp.dh] > temp.tempo) fila.push(temp);
					
					
				} else if(atual.dh == O){
					print("O");
					temp.i = atual.i;
					temp.j = atual.j;
					temp.dv = atual.dv;
					temp.dh = L;
					
					if(atual.j < m-1){
						temp.j = atual.j+1;
						temp.tempo = atual.tempo + 2;
						if(marcado[temp.i][temp.j][temp.dv][temp.dh] > temp.tempo) fila.push(temp);					
					}
					
					temp.j = atual.j;
					temp.tempo = atual.tempo + 1 + (dif > s[atual.i][atual.j] ? 0 : s[atual.i][atual.j] - dif);
					if(marcado[temp.i][temp.j][temp.dv][temp.dh] > temp.tempo) fila.push(temp);
				}
			}
		}
	}
	
	return minimo;
}

void process(){
	memset(marcado, 0x3f3f3f3f, sizeof(marcado));
	
	while(!fila.empty()) fila.pop();
	
	printf("Case #%d: %d\n", casos++, busca());
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	
	int c;
	
	scanf("%d", &c);
	
	while(c--){
		scanf("%d %d", &n, &m);
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				scanf("%d %d %d", &s[i][j], &w[i][j], &t[i][j]);
			}
		}
		
		process();
	}
    
    return 0;
}
