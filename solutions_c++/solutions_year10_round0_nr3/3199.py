#include <cstdio>
#include <utility>
#include <vector>
#include <string>
#include <map>
#include <iostream>
#include <fstream>

using namespace std;

int main(){
	
ifstream entrada("C-large.in");
ofstream salida("C-large.out");

unsigned int t=0;
entrada>> t ;

for(unsigned int casos=1;casos<=t;++casos){
unsigned long long int vueltas;
unsigned long long int capacidad;
unsigned long long int cant_grupos;
entrada >> vueltas;
entrada >> capacidad;
entrada >> cant_grupos;

unsigned long long int grupos[cant_grupos];


unsigned long long int suma=0;
for(unsigned long long int i=0; i <cant_grupos; i++){
	 entrada >> grupos[i];
	suma+= grupos[i];
 }
 
unsigned long long int res=0;

// si la capacidad es mayor o igual a la cantidad de pasajeros en la fila
if (suma<=capacidad) res= vueltas* suma;
else{
	
	unsigned int indice=0;
	unsigned int nindice=0;
	bool b=true;
	unsigned long long int s=0;
	unsigned long long int siempieza[cant_grupos];
	unsigned long long int siempieza_va_hasta[cant_grupos];
	
	
	//Seteo el array que me dice cuanto vale una vuelta cuando empieza por un determinado grupo
	for(unsigned long long int i=0; i<cant_grupos;i++){
				unsigned long long int parcial=0;
				b=true;
				for(unsigned long long int j=i; j<i+cant_grupos && b;j++){
					if( parcial+grupos[j%cant_grupos] > capacidad )b=false;
					else {
						parcial+=grupos[j%cant_grupos];				
						siempieza_va_hasta[i] = (j+1)%cant_grupos;
					}
				}
				siempieza[i]=parcial;	
	}
	res=0;
	indice=0;
	
	
	for(unsigned long long int i=0; i<vueltas;i++){
		res+= siempieza[indice];
		indice= siempieza_va_hasta[indice];
		
	}
	

	
	
	
	
	
	
}

	salida<<"Case #"<<casos;
	salida<<": "<<res<<endl;
	
	
	


	
	
}


return 0;
}
