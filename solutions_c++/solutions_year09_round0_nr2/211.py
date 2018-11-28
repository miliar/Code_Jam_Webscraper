#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <complex>
#include <iostream>
#include <cmath>
#include <utility>
#include <ctype.h>
#include <cstring>
#include <string>
#include <cassert>
#include <queue>
#include <map>
#include <set>
#include <complex>
using namespace std;

#define REP(_i, _N) for(_i=0;_i<_N;_i++)
#define REC(_i, _N) for(_i=1;_i<=_N;_i++)
#define PF printf
#define SF scanf
#define LIMPIA(_a) memset((_a), 0, sizeof(_a))
#define ANULA(_a) memset((_a), -1, sizeof(_a))

typedef long long ll;
const double EPS=1e-9;
const int INF=1000000000;

int T, F, C;

int Pf[120][120];
int Pc[120][120];
int Mapa[120][120];
char Color[120][120];

int Df[]={-1, 0, 0, 1};
int Dc[]={0, -1, 1, 0};

void ponPadreDirecto(int f, int c){
	int df, dc, i;
	df=f;
	dc=c;
	for(i=0;i<4;i++){
		if(Mapa[f+Df[i]][c+Dc[i]]<Mapa[df][dc]){
			df=f+Df[i];
			dc=c+Dc[i];
		}
	}
	Pf[f][c]=df;
	Pc[f][c]=dc;
}

void obtenPadre(int f, int c){
	int df, dc;
	int i;
	df=Pf[f][c];
	dc=Pc[f][c];
	if(df!=f || dc!=c){
		obtenPadre(df, dc);
	}
	Pf[f][c]=Pf[df][dc];
	Pc[f][c]=Pc[df][dc];
}

int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int i, k, h, cas;
	SF("%d", &T);
	REC(cas, T){
		SF("%d %d", &F, &C);
		LIMPIA(Color);
		REP(i, F+2){
			REP(k, C+2){
				Mapa[i][k]=INF;
			}
		}
		REC(i, F){
			REC(k, C){
				SF("%d", &Mapa[i][k]);
			}
		}
		REC(i, F){
			REC(k, C){
				ponPadreDirecto(i, k);
			}
		}
		char cont='a';
		printf("Case #%d:\n", cas);
		REC(i, F){
			REC(k, C){
				obtenPadre(i, k);
				char* dest=&Color[Pf[i][k]][Pc[i][k]];
				if(*dest==0){
					*dest=cont;
					cont++;
				}
				printf("%c", *dest);
				if(k!=C)
					PF(" ");
			}
			printf("\n");
		}
	}
	return 0;
}
