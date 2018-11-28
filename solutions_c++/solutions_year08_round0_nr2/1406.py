//Codejam 2008
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <math.h>
#include <utility>
#include <ctype.h>
#include <string.h>
#include <string>
#include <assert.h>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define REP(_i, _N) for(_i=0;_i<_N;_i++)
#define REC(_i, _N) for(_i=1;_i<=_N;_i++)
#define all(_e) _e.begin(), _e.end()
#define PF printf
#define SF scanf
#define LIMPIA(_a) memset((_a), 0, sizeof(_a))
#define ANULA(_a) memset((_a), -1, sizeof(_a))
#define EPS 0.00000001
#define INF 1000000000

int T, NA, NB, Espera;
typedef priority_queue<int, vector<int>, greater<int> > Cola;

struct viaje{
	int salida, llegada;
	bool operator < (viaje b) const{
		return salida<b.salida;
	}
};
viaje A[200];
viaje B[200];
Cola ColaA;
Cola ColaB;

int saca(int &index, viaje Ar[200], Cola &cola, Cola &otro){
	int aux;
	int r, llega;
	if(!cola.empty()>0){
		aux=cola.top();
		if(aux<=Ar[index].salida){
			cola.pop();
			r=0;
		}else{
			r=1;
		}
	}else{
		r=1;
	}
	llega=Ar[index].llegada+Espera;
	otro.push(llega);
	index++;
	return r;
}

int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int i, k, h;
	int a, b, c, d, ra=0, rb=0;
	SF("%d", &T);
	int caso=0;
	REC(caso, T){
		ra=0, rb=0;
		ColaA=Cola();
		ColaB=Cola();
		SF("%d", &Espera);
		SF("%d %d", &NA, &NB);
		REP(i, NA){
			SF("%d:%d %d:%d", &a, &b, &c, &d);
			A[i].salida=a*60+b;
			A[i].llegada=c*60+d;
		}
		sort(A, A+NA);
		REP(i, NB){
			SF("%d:%d %d:%d", &a, &b, &c, &d);
			B[i].salida=a*60+b;
			B[i].llegada=c*60+d;
		}
		sort(B, B+NB);
		for(i=0, k=0; i<NA || k<NB; ){
			if(i<NA && k<NB){
				if(A[i]<B[k]){
					ra+=saca(i, A, ColaA, ColaB);
				}else{
					rb+=saca(k, B, ColaB, ColaA);
				}
			}else if(i<NA){
				ra+=saca(i, A, ColaA, ColaB);
			}else{
				rb+=saca(k, B, ColaB, ColaA);
			}
		}
		PF("Case #%d: %d %d\n", caso, ra, rb);
	}
	return 0;
}
