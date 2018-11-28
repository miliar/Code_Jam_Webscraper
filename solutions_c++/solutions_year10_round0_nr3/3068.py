#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int main(){

  int ncasos = 0;
  long int k, r, N;
  long int grupos[10];
  long int caja;
  long int indice, indicea;
  bool pasa = true;

  cin >> ncasos;
  for (int i=0; i<ncasos; i++){
    cin >> r >> k >> N;

    for (int j=0; j<N; j++){
      cin >> grupos[j];
    }
    caja = 0;
    indice = 0;
    for (int j=0; j<r; j++){
      int aux = 0;
      indicea = indice;
      while (aux<k && pasa){
        if ((aux + grupos[indice]) <= k){
          aux += grupos[indice];
          indice = (indice+1)%N;
          if (indicea == indice){
            pasa = false;
          }
        }
        else{
          pasa = false;
        }
      }
      pasa = true;
      caja +=aux;
    }
    cout << "Case #" << i+1 << ": " << caja << endl;
  }
  return 0;
}
