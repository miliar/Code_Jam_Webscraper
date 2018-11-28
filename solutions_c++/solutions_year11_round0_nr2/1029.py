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
int C, D, N, T;
char In[10000];
char Combine[200][200];
char Pila[1000];
int Tam;
bool Op[200][200];

int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int i, k, h;
	SF("%d", &T);
	int caso;
	REC(caso, T){
		LIMPIA(Combine);
		LIMPIA(Op);
		SF("%d", &C);
		REP(i, C){
			SF("%s", In);
			Combine[In[0]][In[1]]=In[2];
			Combine[In[1]][In[0]]=In[2];
		}
		SF("%d", &D);
		REP(i, D){
			SF("%s", In);
			Op[In[0]][In[1]]=true;
			Op[In[1]][In[0]]=true;
		}
		SF("%d", &N);
		SF("%s", In);
		Tam=0;
		REP(i, N){
			bool pudoCombinar=false;
			Pila[Tam++]=In[i];
			do{
				pudoCombinar=false;
				if(Tam>=2 && Combine[Pila[Tam-2]][Pila[Tam-1]]!=0){
					Pila[Tam-2]=Combine[Pila[Tam-2]][Pila[Tam-1]];
					Tam--;
					pudoCombinar=true;
				}
			}while(pudoCombinar);
			char aux=Pila[Tam-1];
			REP(k, Tam-1){
				if(Op[Pila[k]][aux]){
					Tam=0;
					break;
				}
			}
		}
		printf("Case #%d: [", caso);
		REP(i, Tam){
			printf("%c", Pila[i]);
			if(i+1!=Tam)
				printf(", ");
		}
		printf("]\n");
	}
	return 0;
}
