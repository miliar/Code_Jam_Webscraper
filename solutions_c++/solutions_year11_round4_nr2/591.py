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

struct Ponto {
	double x,y;
	
	Ponto(double x = 0, double y = 0) : x(x) , y(y) {}
	Ponto operator + (Ponto p){	return Ponto(x+p.x, y+p.y);}
	Ponto operator - (Ponto p){return Ponto(x-p.x, y-p.y);}
	//cuidado com overflow daqui pra baixo
	Ponto operator * (double a){return Ponto(x*a, y*a);}
	double norma2(){return x*x + y*y;}
	double dist(Ponto p){return (x-p.x)*(x-p.x) + (y-p.y)*(y-p.y);}
	Ponto operator / (double a){return Ponto(x/a, y/a);}
};


int R,C,D;
char matrix[600][600];
Ponto sumall[600][600];
long long pesoall[600][600];

Ponto getpontocommassa(int i, int j) {
	long long peso = matrix[i][j];
	return Ponto(peso*(i+1), peso*(j+1));
}

bool zero(double x) {
	return x < 1E-9 && x > -1E-9;
}

bool ok(int i, int j, int k) {
	Ponto ps = sumall[i+k][j+k];
	if (i-k > 0) ps = ps - sumall[i-k-1][j+k];
	if (j-k > 0) ps = ps - sumall[i+k][j-k-1];
	if (i-k > 0 && j-k > 0) ps = ps + sumall[i-k-1][j-k-1];
	
	ps = ps - getpontocommassa(i+k,j+k);
	ps = ps - getpontocommassa(i+k,j-k);
	ps = ps - getpontocommassa(i-k,j+k);
	ps = ps - getpontocommassa(i-k,j-k);
	
	long long todamassa = pesoall[i+k][j+k];
	if (i-k > 0) todamassa -= pesoall[i-k-1][j+k];
	if (j-k > 0) todamassa -= pesoall[i+k][j-k-1];
	if (i-k > 0 && j-k > 0) todamassa += pesoall[i-k-1][j-k-1];
	
	todamassa -=  matrix[i+k][j+k];
	todamassa -=  matrix[i+k][j-k];
	todamassa -=  matrix[i-k][j+k];
	todamassa -=  matrix[i-k][j-k];
	
	Ponto cs = Ponto(i+1,j+1)*todamassa;
	
	
	Ponto answer = ps - cs;
	//printf("(%d,%d), k = %d -> (%lld,%lld)\n", i,j,k,answer.x,answer.y);
	//printf("   ps (%lld, %lld), cs (%lld, %lld), todamassa %d\n",ps.x,ps.y,cs.x, cs.y, todamassa);
	
	return zero(answer.x) && zero(answer.y);
}

bool ok2(int i, int j, int k) {
	Ponto ps = sumall[i+k-1][j+k-1];
	if (i-k > 0) ps = ps - sumall[i-k-1][j+k-1];
	if (j-k > 0) ps = ps - sumall[i+k-1][j-k-1];
	if (i-k > 0 && j-k > 0) ps = ps + sumall[i-k-1][j-k-1];
	
	ps = ps - getpontocommassa(i+k-1,j+k-1);
	ps = ps - getpontocommassa(i+k-1,j-k);
	ps = ps - getpontocommassa(i-k  ,j+k-1);
	ps = ps - getpontocommassa(i-k  ,j-k);
	
	long long todamassa = pesoall[i+k-1][j+k-1];
	if (i-k > 0) todamassa -= pesoall[i-k-1][j+k-1];
	if (j-k > 0) todamassa -= pesoall[i+k-1][j-k-1];
	if (i-k > 0 && j-k > 0) todamassa += pesoall[i-k-1][j-k-1];
	
	todamassa -=  matrix[i+k-1][j+k-1];
	todamassa -=  matrix[i+k-1][j-k];
	todamassa -=  matrix[i-k][j+k-1];
	todamassa -=  matrix[i-k][j-k];
	
	Ponto cs = Ponto(i+0.5,j+0.5)*todamassa;
	
	
	Ponto answer = ps - cs;
	//printf("(%d,%d), k = %d -> (%lf,%lf)\n", i,j,k,answer.x,answer.y);
	//printf("   ps (%lf, %lf), cs (%lf, %lf), todamassa %d\n",ps.x,ps.y,cs.x, cs.y, todamassa);
	
	return zero(answer.x) && zero(answer.y);
}



void process() {
	scanf("%d%d%d", &R, &C, &D);
	for (int i = 0; i < R; i++) scanf("%s", matrix[i]);
	
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			matrix[i][j] -= '0';
		}
	}
	
	sumall[0][0] = Ponto(matrix[0][0], matrix[0][0]);
	pesoall[0][0] = matrix[0][0];
	
	long long peso;
	for (int i = 1; i < R; i++) {
		peso = matrix[i][0];
		sumall[i][0] = sumall[i-1][0] + Ponto(peso * (i+1), peso);
		pesoall[i][0] = peso + pesoall[i-1][0];
	}
	for (int j = 1; j < C; j++) {
		peso = matrix[0][j];
		sumall[0][j] = sumall[0][j-1] + Ponto(peso, peso*(j+1));
		pesoall[0][j] = peso + pesoall[0][j-1];
	}
	
	for (int i = 1; i < R; i++) {
		for (int j = 1; j < C; j++) {
			peso = matrix[i][j];
			sumall[i][j] = Ponto(peso*(i+1), peso*(j+1)) - sumall[i-1][j-1] + sumall[i][j-1] + sumall[i-1][j];
			pesoall[i][j] = peso - pesoall[i-1][j-1] + pesoall[i][j-1] + pesoall[i-1][j];
		}
	}

	
	int melhor = 0;
	for (int i = 1; i < R-1; i++) {
		for (int j = 1; j < C-1; j++) {
			for (int k = melhor+1; i-k >= 0 && i+k < R && j-k >= 0 && j+k < C; k++) {
				if (ok(i,j,k)) {
					melhor = k;
				}
			}
		}
	}
	
	int melhor2 = 0;
	for (int i = 2; i < R-1; i++) {
		for (int j = 2; j < C-1; j++) {
			for (int k = max(2, melhor2+1); i-k >= 0 && i+k <= R && j-k >= 0 && j+k <= C; k++) {
				if (ok2(i,j,k)) {
					melhor2 = k;
				}
			}
		}
	}
	
	if (melhor) melhor = 1+2*melhor;
	if (melhor2) melhor2 = 2*melhor2;
	
	if (melhor || melhor2) printf("%d\n", max(melhor, melhor2));
	else printf("IMPOSSIBLE\n");
	
}

int main() {
	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int i = 0 ; i < T ; i++) {
		printf("Case #%d: ", i+1);
		process();
	}
	
	return 0;
}
