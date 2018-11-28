#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <queue>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int P;
int times;
int M[3100];
int precos[12][3100];

int pd[12][3100][12];

int calc(int nivel, int jogo, int jaJogou) {
	if (pd[nivel][jogo][jaJogou] == -1) {
		if (nivel == P) {
			if (jaJogou >= P-M[jogo]) {
				pd[nivel][jogo][jaJogou] = 0;
			} else {
				pd[nivel][jogo][jaJogou] = -2; // inf
			}
		} else {
			
			pd[nivel][jogo][jaJogou] = -2;
			
			int a,b,c;
			// jogando
			a = calc(nivel+1, jogo*2, jaJogou+1);
			b = calc(nivel+1, jogo*2+1, jaJogou+1);
			c = precos[nivel][jogo];
			if (a!= -2 && b!= -2) {
				c+= a+b;
				if (pd[nivel][jogo][jaJogou] == -2 || pd[nivel][jogo][jaJogou] > c) {
					pd[nivel][jogo][jaJogou] = c;
				}
			}
			
			// nao jogando
			a = calc(nivel+1, jogo*2, jaJogou);
			b = calc(nivel+1, jogo*2+1, jaJogou);
			c = 0;
			if (a!= -2 && b!= -2) {
				c+= a+b;
				if (pd[nivel][jogo][jaJogou] == -2 || pd[nivel][jogo][jaJogou] > c) {
					pd[nivel][jogo][jaJogou] = c;
				}
			}
			
		}
	}
	return pd[nivel][jogo][jaJogou];
}

int process() {
	scanf("%d", &P);
	times = 1<<P;
	
	for (int i = 0 ; i < times; i++) {
		scanf("%d", &M[i]);
	}
	
	int temp;
	for (int i = P-1 ; i >= 0 ; i--) {
		temp = 1<<i;
		for (int j = 0 ; j < temp ; j++) {
			scanf("%d", &precos[i][j]);
		}
	}
	
	memset(pd, -1, sizeof(pd));
	
	return calc(0,0,0);
}

int main() {
	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int i = 0 ; i < T ; i++) {
		printf("Case #%d: %d\n", i+1, process());
	}
	
	return 0;
}
