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

int listaAuxiliar[200]; int nInvoked;
char combinaciones[50][3]; int C;
char oposiciones[50][2]; int D;
char invocaciones[200]; int N;

bool capLetter(char c) {
     if (c>='A' && c<='Z')
        return true; // It IS a cap
     return false;
}

char combine(char c1, char c2) {
     if (nInvoked<2)
        return false;
    for (int i=0; i<C; i++)
        if ((combinaciones[i][0]==c1 && combinaciones[i][1]==c2) || (combinaciones[i][0]==c2 && combinaciones[i][1]==c1))
           return combinaciones[i][2];
    return 0;
}

bool isOpposed(char c1) {
     if (nInvoked<2)
        return false;
    for (int i=0; i<D; i++) { // Para cada oposicion
        char c2=0;
        // Se averigua si C1 es uno de los 2 componentes
        if (oposiciones[i][0]==c1)
           c2=oposiciones[i][1];
        else if (oposiciones[i][1]==c1)
           c2=oposiciones[i][0];
        else continue;
// Si lo es, c2 es el otro y se comprueba si está en la lista:
// ( ¿What if c1==c2... it should appear two times, i guess )
       for (int k=0; k<nInvoked-1; k++) // The last one is c1 for sure; i don't care about it
           if (listaAuxiliar[k]==c2)
              return true;
    }
    return false;
}

int calcularLista() {
    nInvoked=0;
    char combinacion=0;
    for (int i=0; i<N; i++){
        // Invoke
        listaAuxiliar[nInvoked++]=invocaciones[i];
        // Combine??
        if (nInvoked>=2) {
            combinacion=combine(listaAuxiliar[nInvoked-1], listaAuxiliar[nInvoked-2]);
            if (combinacion!=0) {
               listaAuxiliar[nInvoked-2]=combinacion;
               nInvoked--;
            }
        }
        // Clear?
        if (nInvoked>=2 && isOpposed(listaAuxiliar[nInvoked-1]))
           nInvoked=0;
    }
    return nInvoked;
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
    cout << T << " casos de prueba." << endl;
    for (int j=1; j<=T; j++) {
              cout << "*** ** *" << endl;
          entrada >> C; cout << C << " combinaciones." << endl;
          for (int i=0; i<C; i++) {
//              cout << "..." << i << endl;
              for (int k=0; k<3; k++) {
                  do {
                     entrada >> combinaciones[i][k];
                  } while (!capLetter(combinaciones[i][k]));
//                  cout << combinaciones[i][k] << " ";
              }
        }
              cout << endl << " - " << endl;
          entrada >> D; cout << D << " oposiciones." << endl;
          for (int i=0; i<D; i++) {
              for (int k=0; k<2; k++) {
                  do {
                     entrada >> oposiciones[i][k];
                  } while (!capLetter(oposiciones[i][k]));
//                  cout << oposiciones[i][k] << " ";
              }
          }
              cout << endl << " - " << endl;
          entrada >> N; cout << N << " invocaciones." << endl;
          for (int i=0; i<N; i++) {
              do {
                 entrada >> invocaciones[i];
              } while (!capLetter(invocaciones[i]));
//              cout << invocaciones[i] << " ";
          }
          calcularLista();
          salida << "Case #" << j << ": [";
          for (int m=0; m<nInvoked-1; m++)
              salida << (char)listaAuxiliar[m] << ", ";
          if (nInvoked>0)
             salida << (char)listaAuxiliar[nInvoked-1];
          salida << "]" << endl;
    }
    
    
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
