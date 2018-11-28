///////////////////////////////////////////////////////////
// Francisco J. Sanchez                                  //
///////////////////////////////////////////////////////////

#include <string.h>   // Funcion memset
#include <iostream>   // E/S con cin y cout
using namespace std;

///////////////////////////////////////////////////////////
//////////        VARIABLES GLOBALES        ///////////////
///////////////////////////////////////////////////////////

long long R;
long long k;
int N;
long long g[1000];
long long solucion;

///////////////////////////////////////////////////////////
//////////     FUNCIONES DEL PROGRAMA       ///////////////
///////////////////////////////////////////////////////////

void lee ()
// Procedimiento para leer desde la entrada estandar
{
  cin >> R >> k >> N;
  for (int i = 0; i < N; ++i)
    {
      cin >> g[i];
    }
}

void algoritmo(){
  long long pos=0;
  solucion=0;
  long long primero;

  long long people;

  for(int i=0; i<R; i++){
    people=0;
    primero=pos;
    do{
      people+=g[pos];
      pos=(pos+1)%N;
    } while(people+g[pos]<=k && pos!=primero);
    solucion+=people;
  }
}

///////////////////////////////////////////////////////////
//////////        PROGRAMA PRINCIPAL        ///////////////
///////////////////////////////////////////////////////////

int main (void)
{
  int ncasos;
  cin >> ncasos;
  for (int i= 0; i<ncasos; i++){
    lee();
    algoritmo();
    cout << "Case #" << i+1 << ": " << solucion << endl;
  }
}
