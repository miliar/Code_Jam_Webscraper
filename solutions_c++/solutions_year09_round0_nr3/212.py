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

int N;
char Cad[1000];
char Frase[]="welcome to code jam";
int Cont[1000][23];

int cuenta(int a, int i){
	int r;
	if(Frase[i]==0)
		return 1;
	if(Cad[a]==0){
		return 0;
	}else{
		r=cuenta(a+1, i);
		r%=10000;
		if(Cad[a]==Frase[i])
			r+=cuenta(a+1, i+1);
		r%=10000;
	}
	return r;
}

int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int i, k, h, l;
	l=strlen(Frase);
	int cas;
	int r=0;
	gets(Cad);
	sscanf(Cad, "%d", &N);
	REC(cas, N){
		gets(Cad);
		LIMPIA(Cont);
		Cont[0][0]=1;
		r=0;
		for(i=1;Cad[i-1]!=0;i++){
			for(k=0;k<=l;k++){
				Cont[i][k]=Cont[i-1][k];
				//Cont[i][k]+=Cont[i][k-1];
				//Cont[i][k]%=10000;
				if(k>=1 && Cad[i-1]==Frase[k-1]){
					Cont[i][k]+=Cont[i-1][k-1];
					Cont[i][k]%=10000;
				}
			}
			//r+=Cont[i][l];
			//r%=10000;
		}
		//r=cuenta(0, 0);
		//assert(r==Cont[i-1][l]);
		printf("Case #%d: %04d\n", cas, Cont[i-1][l]);
	}
	return 0;
}
