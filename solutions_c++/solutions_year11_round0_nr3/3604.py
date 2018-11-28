#include <string.h>   // Funcion memset
#include <iostream>   // E/S con cin y cout


using namespace std;

#define MAX 101


///////////////////////////////////////////////////////////
//////////        VARIABLES GLOBALES        ///////////////
///////////////////////////////////////////////////////////

int Ncasos, secuencia;
long int suma, total, numero;
long int m=0;


///////////////////////////////////////////////////////////
//////////        PROGRAMA PRINCIPAL        ///////////////
///////////////////////////////////////////////////////////

int main (void)
{
 
cin >> Ncasos;

for(int j=0; j<Ncasos; j++){
 suma=total=0;
 m=99999999;
 cin >> secuencia;
 for(int i=0; i<secuencia; i++){
   cin >> numero;
   total+=numero;
   if(numero<m){m=numero;}
   suma = suma^numero;
 }
 if(suma==0){ cout<< "Case #" << (j+1) <<": " << (total-m) << endl; }else{cout << "Case #" << (j+1) <<": " <<  "NO" << endl;}

  
}


}
