#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include <iostream>
#include <vector>
using namespace std;

long long int lucro=0;
int T, R, k, N, ktemp;
int fila[1000];
int indice, primeiro;

int main(){
	int i,j, aux;

	scanf("%d",&T);
	for(i=1;i<=T;i++){
		scanf("%d %d %d",&R, &k, &N);
		for(j=0; j<N; j++){
			scanf("%d",&fila[j]);
		}
		indice=0;
		
		for(j=0; j<R; j++){
			ktemp=k;
			primeiro = indice;
			while(fila[indice]<=ktemp){
				ktemp-=fila[indice];
				lucro+=fila[indice];
				indice++;
				if(indice==N)
					indice=0;
				if(primeiro == indice)
					break;
			}
		
		}
		printf("Case #%d: %lld\n",i, lucro);
		lucro=0;
	}
	
    return 0;

}
