//Codejam 2011
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

int S[2000];
bool V[2000];
double E[2000];
int N;
int T;
const int SAMPLES=100000000;
int Perm[200];

double getExpected(int perm[], int n){
	int i, k;
	memset(V, 0, n);
	double r=0.0;
	int usados=0;
	REP(i, n){
		if(!V[i]){
			int tam=0;
			k=i;
			do{
				tam++;
				V[k]=true;
				k=perm[k];
			}while(!V[k]);
			if(tam==n){
				random_shuffle(perm, perm+n);
				return getExpected(perm, n)+1.0;
			}
			r+=E[tam];
			usados+=tam;
			if(usados==n){
				return r;
			}
		}
	}
	return r;
}

double getExpected(int n){
	int i;
	int k;
	for(i=1;i<=n;i++){
		Perm[i-1]=i;
	}
	k=SAMPLES;
	double r=0;
	while(k--){
		random_shuffle(Perm, Perm+n);
		r+=(getExpected(Perm, n)+1.0)/SAMPLES;
	}
	E[n]=r;
	return E[n];
}

int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int i, k, h;
	int caso;
	int Ciclos=0;
	/*E[1]=0.0;
	E[2]=2.0;
	for(i=3;i<=100;i++){
		printf("%d %lf\n", i, getExpected(i));
	}
	return 0;*/

	SF("%d", &T);
	REC(caso, T){
		SF("%d", &N);
		LIMPIA(S);
		LIMPIA(V);
		REP(i, N){
			SF("%d", &k);
			S[i]=k-1;
		}
		Ciclos=0;
		double r=0.0;
		REP(i, N){
			if(!V[i]){
				Ciclos++;
				k=i;
				int tam=0;
				do{
					V[k]=true;
					tam++;
					k=S[k];
				}while(!V[k]);
				if(tam>1){
					r+=tam;
				}
			}
		}
		PF("Case #%d: %.6lf\n", caso, r);
	}
	return 0;
}
