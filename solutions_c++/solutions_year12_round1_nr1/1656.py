#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#define FOR(i, a, b) for(int i = a; i < b; ++i)
using namespace std;

double prob[3];
double matriz2[4][4], matriz3[5][8];

//a = 1
double func1(int a, int b) {
	double res = 0., aux;
	res = (double(b-a+1))*prob[0] + (double(2*b-a+2))*(1.-prob[0]);
	res = min(res, double(b+2));
	return res;
}

//a = 2
double func2(int a, int b) {
	double res = 0., aux = 0., aux2;
	FOR(i, 0, 4) {
		aux = 0.;
		FOR(j, 0, 4) {
			switch(j) {
				case 0: aux2 = prob[0]*prob[1];break;
				case 1: aux2 = prob[0]*(1.-prob[1]);break;
				case 2: aux2 = (1.-prob[0])*prob[1];break;
				case 3: aux2 = (1.-prob[0])*(1.-prob[1]);break;
				default: break;
			}
			aux += matriz2[i][j]*aux2;
		}
		if(i == 0)
			res = aux;
		else {
			res = min(res, aux);
		}
	}
	return res;
}

//a = 3
double func3(int a, int b) {
	double res = 0., aux = 0., aux2;
	FOR(i, 0, 5) {
		aux = 0.;
		FOR(j, 0, 8) {
			switch(j) {
				case 0: aux2 = prob[0]*prob[1]*prob[2];break;
				case 1: aux2 = prob[0]*prob[1]*(1.-prob[2]);break;
				case 2: aux2 = prob[0]*(1.-prob[1])*prob[2];break;
				case 3: aux2 = prob[0]*(1.-prob[1])*(1.-prob[2]);break;
				case 4: aux2 = (1.-prob[0])*prob[1]*prob[2];break;
				case 5: aux2 = (1.-prob[0])*prob[1]*(1.-prob[2]);break;
				case 6: aux2 = (1.-prob[0])*(1.-prob[1])*prob[2];break;
				case 7: aux2 = (1.-prob[0])*(1.-prob[1])*(1.-prob[2]);break;
				default: break;
			}
			aux += matriz3[i][j]*aux2;
		}
		if(i == 0)
			res = aux;
		else {
			res = min(res, aux);
		}
	}
	return res;
}

void preencherMatriz(int a, int b) {
	if(a == 2) {
		matriz2[0][0] = double(b-a+1);
		matriz2[0][1] = double(2*b-a+2);
		matriz2[0][2] = double(2*b-a+2);
		matriz2[0][3] = double(2*b-a+2);

		matriz2[1][0] = double(b-a+3);
		matriz2[1][1] = double(b-a+3);
		matriz2[1][2] = double(2*b-a+4);
		matriz2[1][3] = double(2*b-a+4);

		matriz2[2][0] = double(b+3);
		matriz2[2][1] = double(b+3);
		matriz2[2][2] = double(b+3);
		matriz2[2][3] = double(b+3);

		matriz2[3][0] = double(b+2);
		matriz2[3][1] = double(b+2);
		matriz2[3][2] = double(b+2);
		matriz2[3][3] = double(b+2);
	}
	else {
		matriz3[0][0] = double(b-a+1);
		matriz3[0][1] = double(2*b-a+2);
		matriz3[0][2] = double(2*b-a+2);
		matriz3[0][3] = double(2*b-a+2);
		matriz3[0][4] = double(2*b-a+2);
		matriz3[0][5] = double(2*b-a+2);
		matriz3[0][6] = double(2*b-a+2);
		matriz3[0][7] = double(2*b-a+2);

		matriz3[1][0] = double(b-a+3);
		matriz3[1][1] = double(b-a+3);
		matriz3[1][2] = double(2*b-a+4);
		matriz3[1][3] = double(2*b-a+4);
		matriz3[1][4] = double(2*b-a+4);
		matriz3[1][5] = double(2*b-a+4);
		matriz3[1][6] = double(2*b-a+4);
		matriz3[1][7] = double(2*b-a+4);

		matriz3[2][0] = double(b-a+5);
		matriz3[2][1] = double(b-a+5);
		matriz3[2][2] = double(b-a+5);
		matriz3[2][3] = double(b-a+5);
		matriz3[2][4] = double(2*b-a+6);
		matriz3[2][5] = double(2*b-a+6);
		matriz3[2][6] = double(2*b-a+6);
		matriz3[2][7] = double(2*b-a+6);
		
		matriz3[3][0] = double(b+4);
		matriz3[3][1] = double(b+4);
		matriz3[3][2] = double(b+4);
		matriz3[3][3] = double(b+4);
		matriz3[3][4] = double(b+4);
		matriz3[3][5] = double(b+4);
		matriz3[3][6] = double(b+4);
		matriz3[3][7] = double(b+4);

		matriz3[4][0] = double(b+2);
		matriz3[4][1] = double(b+2);
		matriz3[4][2] = double(b+2);
		matriz3[4][3] = double(b+2);
		matriz3[4][4] = double(b+2);
		matriz3[4][5] = double(b+2);
		matriz3[4][6] = double(b+2);
		matriz3[4][7] = double(b+2);

	}
}

int main() {
	int t, a, b;
	double ans;
	scanf("%d", &t);
	FOR(i, 0, t) {
		scanf("%d %d", &a, &b);
		preencherMatriz(a, b);
		FOR(j, 0, a) {
			scanf("%lf", &prob[j]);
		}
		if(a == 1)
			ans = func1(a, b);
		else if(a == 2)
			ans = func2(a, b);
		else ans = func3(a, b);
		printf("Case #%d: %.6lf\n", i+1, ans);
	}
}
