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

struct nodoDic{
	//int cont;
	int clave;
	int s[95];
};

class Diccionario{
	private:
	nodoDic vDatos[10000];
	int vNodos;
	int vA;
	public:
	Diccionario(){
		vA=' ';
		vNodos=2;
		//vDatos[1].cont=0;
		memset(vDatos[1].s, 0, sizeof(vDatos[1].s));
	}
	void insertar(char palabra[], int n, int clave, int p=0, int a=1){
		int k;
		if(n==p){
			vDatos[a].clave=clave;
			//vDatos[a].cont++;
			return;
		}
		k=palabra[p]-vA;
		if(vDatos[a].s[k]==0){
			//vDatos[vNodos].cont=0;
			memset(vDatos[vNodos].s, 0, sizeof(vDatos[vNodos].s));
			vDatos[a].s[k]=vNodos++;
		}
		insertar(palabra, n, clave, p+1, vDatos[a].s[k]);
	}
	int buscar(char palabra[], int n, int p=0, int a=1) const{
		int k;
		if(n==p)
			return vDatos[a].clave;
		k=palabra[p]-vA;
		if(vDatos[a].s[k]==0)
			return -1;
		return buscar(palabra, n, p+1, vDatos[a].s[k]);		
	}
};

Diccionario Buscadores;
int T, N, Q;
char Cadena[200];
char Query[1100][200];
int O[1100][200];

int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int i, k, h, r;
	int a, b;
	int Caso=1;
	gets(Cadena);
	sscanf(Cadena, "%d", &T);
	while(T--){
		r=INF;
		Buscadores=Diccionario();
		//Leer
		gets(Cadena);
		sscanf(Cadena, "%d", &N);
		REC(i, N){
			gets(Cadena);
			Buscadores.insertar((char*) Cadena, strlen(Cadena), i);
		}
		gets(Cadena);
		sscanf(Cadena, "%d", &Q);
		REC(i, Q){
			gets(Query[i]);
		}
		if(Q==0)
			r=0;
		//Procesa
		REC(i, Q){
			h=Buscadores.buscar(Query[i], strlen(Query[i]));
			b=-1;
			REC(k, N){
				if(h!=k && (b==-1 || O[i-1][k]<O[i-1][b])){
					b=k;
				}
			}
			REC(k, N){
				if(h!=k){
					O[i][k]=O[i-1][k];
				}else{
					O[i][k]=INF;
				}
				O[i][k]=min(O[i][k], O[i-1][b]+1);
				if(i==Q){
					r=min(r, O[i][k]);
				}
			}
		}
		//Salida
		PF("Case #%d: %d\n", Caso, r);
		Caso++;	
	}
	return 0;
}
