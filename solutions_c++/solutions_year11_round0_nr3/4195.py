#include<iostream>
#include<stdio.h>
#define maximo 1500

using namespace std;

int main(){

 int t,n,vet[maximo]; 
 int estado,menor;
 long soma;
 
 scanf("%d",&t);
 
 for (int i = 0; i < t; i++){
 	
	scanf("%d",&n);
	scanf("%d",&vet[0]);
	scanf("%d",&vet[1]);
		
	if (vet[0] - vet[1] > 0) menor = vet[1];
	else menor = vet[0];
	
	estado = vet[0] ^ vet[1];
	soma = vet[0]+vet[1];
	
	for (int j = 2; j < n; j++){
		scanf("%d",&vet[j]);
		estado = estado ^ vet[j];
		soma += vet[j];
		if (menor > vet[j])menor = vet[j];					
	}
	if (estado == 0){
		cout << "Case #" << i+1 << ": " << soma - menor << endl;
	}
	else cout << "Case #" << i+1 << ": " << "NO" << endl;
 }

 return 0;
}
