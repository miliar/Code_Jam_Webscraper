

#include <string.h>   // Funcion memset
#include <iostream>   // E/S con cin y cout
#include <math.h>
#include <queue>
#include <list>


using namespace std;


#define MAX 100

///////////////////////////////////////////////////////////
//////////        VARIABLES GLOBALES        ///////////////
///////////////////////////////////////////////////////////


//long long int grupo[MAX];
long long int T;
long long int tim, per, gru;
long long int total;
 list<long long int> grupo;
///////////////////////////////////////////////////////////
//////////     FUNCIONES DEL PROGRAMA       ///////////////
///////////////////////////////////////////////////////////
 


//######################################################################################################

void solucion(void)
{
long long int s, p, grup;
bool salida= false;

 for(long long int i=0; i<tim; i++){
  s=0;
  salida= false;
  grup=0;
 
   while(!salida && grup< gru){
    p=grupo.back();
    if(p+s <= per){
       s = s + p;
       grup++;
       grupo.push_front(p);
       grupo.pop_back();
    }
    else {
     salida = true;
     
    }
     
   }//fin while
   total = total + s ;

 }//fin for
 
 

}//fin metodo 
//######################################################################################################
///////////////////////////////////////////////////////////
//////////        PROGRAMA PRINCIPAL        ///////////////
///////////////////////////////////////////////////////////

  int main (void)
{
 long long int a;
 cin >> T;
  
  for(long long int i=0; i<T; i++){
    grupo.clear();
    total=0;
    
    cin >> tim >> per >> gru;

    for(long long int j=0; j<gru; j++){
      cin >> a;
      grupo.push_front(a);
    }
    solucion();
    cout << "Case #" << i+1 <<": "  << total << "\n";

  }
   
}//FIN
