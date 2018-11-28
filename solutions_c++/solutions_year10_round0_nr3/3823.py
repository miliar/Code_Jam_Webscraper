#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int t, r, k, n;
     ifstream f;

      ofstream f2;
  f2.open ("output");


  f.open ("teste");
  f >> t ;
  for (int i = 0; i < t; i++){

      f >> r >> k >> n;
      int * fila = new int[n];
      for (int m = 0; m < n; m++){
          f >> fila[m];
          }
      int posicao = 0;
      int din = 0;
      int pos = posicao % n;
      int posIn = 0;
      for (int j = 0; j < r; j++){
          int corrida = 0;
          while (corrida + fila[pos] <= k){
              corrida += fila[pos];
              din += fila[pos];
              posicao++;
              pos = posicao % n;
              if (pos == posIn)
                 break;

              }
          posIn = pos;


          }


      f2 << "Case #" << i+1 << ": " << din << endl;

     delete[] fila;


      }
 // cout << r << k << n;

  f.close();
   f2.close();

    return 0;
}
