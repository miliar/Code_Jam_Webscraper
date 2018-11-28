#include <cstdlib>
#include <iostream>
#include <fstream>
#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"

using namespace std;

int candyList[200]; int N;
int pertenencia[200];
// (Toma valores 0 o 1 si los caramelos pertenecen a uno u otro hermano)


int calculaPert(int bro) {
    int aux=0;
    for (int i=0; i<N; i++)
        if (pertenencia[i]==bro) {
           aux=aux^candyList[i]; // Exclusive OR... I hope...
           }
    return aux;
}

int evaluaSalida() {
   int suma=0;
    for (int i=0; i<N; i++) {
        if (pertenencia[i]==0)
           suma+=candyList[i];
    }
    return suma;
}

int main(int argc, char *argv[])
{
    if (argc<2) {
        printf("\n...input file needed...\r\n");
    system("PAUSE");
		exit(-1);
    }
    int T=-1, P=100; // , C=-1, D=-1, N=-1;
    FILE *outputF, *inputF;

    ifstream entrada(argv[1]); 
    ofstream salida("output.out");
    entrada >> T;
    cout << T << " test cases." << endl;
    for (int j=1; j<=T; j++) {
              cout << "*** ** *" << endl;
          entrada >> N; cout << N << " candies ." << endl;
          for (int i=0; i<N; i++) {
              entrada >> candyList[i];
              pertenencia[i]=0;
              cout << candyList[i] << " ";
          }
          int comb=(int)pow(2.0,N), sean=-1, patrick=-2, mejor=-1;
          // Try all the combinations from the bottom up
          //since the candies seem to be sorted
          for (int i=1; i<comb; i++) {
              int aux=i;
              for (int j=0; j<N; j++) {
                  pertenencia[j]=(aux%2);
                  aux=aux/2;
              }
              sean=calculaPert(0);
              patrick=calculaPert(1);
              if (sean==patrick) {
                int aux=evaluaSalida();
                  if (aux>mejor)
                     mejor=aux;
              }
                 
          }

          salida << "Case #" << j << ": ";
          if (mejor<0)
             salida << "NO" << endl;
          else {
//               int suma=evaluaSalida();
                salida << mejor << endl;
          }
    }
    
    
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
