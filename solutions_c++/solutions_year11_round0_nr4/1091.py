#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <map>
#include <algorithm>
#include <utility>
#include <cmath>

using namespace std;

int cont, fim;
double di, d;
double sim(double a){
	++cont;
	if(cont == fim) return a*di;
	return a*di + (sim(a+1.0))*d;
}

int grafo[1010], n, mark[1010], cn;

int tamCicle(int at){
	if(mark[at] == cn) return 0;
	mark[at] = cn;
	return tamCicle(grafo[at]) + 1;
}

int main(){
	/*cont = 0;
	fim = 20;
	di = 1/3.0;
	d = 1.0-di;
	printf("%lf\n", sim(1.0));
	*/
	int at;
	int casos; scanf("%d", &casos);
	int caso = 1;
	while(casos--){
		++cn;
		scanf("%d", &n);
		for(int i = 1; i <= n; ++i){
			scanf("%d", &at);
			grafo[i] = at;
		}
		double saida =0;
		int aux;
		for(int i = 1; i <= n; ++i){
			if(mark[i] != cn){
				aux = tamCicle(i);
				if(aux != 1){
					saida += aux;
				}
			}
		}
		printf("Case #%d: %.6lf\n", caso++, saida);
		
	}
	
	
	
	return 0;
}