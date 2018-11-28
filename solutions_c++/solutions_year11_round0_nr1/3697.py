#include <string.h>   // Funcion memset
#include <iostream>   // E/S con cin y cout


using namespace std;

#define MAX 101


///////////////////////////////////////////////////////////
//////////        VARIABLES GLOBALES        ///////////////
///////////////////////////////////////////////////////////

int Ncasos;
int secuencia=0;
char sig;
long long int T, dis, Eo, Eb, Po, Pb;



///////////////////////////////////////////////////////////
//////////     FUNCIONES DEL PROGRAMA       ///////////////
///////////////////////////////////////////////////////////

int abs (int i)
{
    if (i < 0)
        return -i;
    else
        return i;
}

void resolver(){

 

}// end solve





///////////////////////////////////////////////////////////
//////////        PROGRAMA PRINCIPAL        ///////////////
///////////////////////////////////////////////////////////

int main (void)
{
 
cin >> Ncasos;

for(int j=0; j<Ncasos; j++){
 T=Eo=Eb=0;
 Po=Pb=1;
 cin>> secuencia;

 for(int i=0; i<secuencia; i++){
   cin >> sig >> dis;
  if(sig=='O'){
    if(abs(Po-dis)<=Eo){ T+=1;  Eb++; }else{T+=(abs(Po-dis)-Eo)+1; Eb+=(abs(Po-dis)-Eo)+1; }
    Eo=0; Po=dis;
  }
  else if(sig=='B'){
    if(abs(Pb-dis)<=Eb){ T+=1; Eo++;}else{T+=(abs(Pb-dis)-Eb)+1; Eo+=(abs(Pb-dis)-Eb)+1; }
     Eb=0; Pb=dis;
  }

 }//fin solve bucle

  cout<< "Case #" << (j+1) << ": " << T << endl;
  
}


}
