#include <cstdlib>
#include <iostream>
#include <fstream>
#include <list>
#include <set>

using namespace std;

bool iguales(char* pI, char* iGiro, int nI){
  bool iguales = true;
  for(int g=0; g<nI; g++){
    iguales = iguales && (pI[g] == iGiro[g]);
  }
  return false;
}

void girarK(char* pI, int nI, int k, char* giro){
  int posInGiro = 0;
  for(int j = nI-k; j<nI; j++){
    giro[posInGiro] = pI[j];
    posInGiro++;
  }
  for(int h = 0; h < nI-k; h++){
    giro[posInGiro] = pI[h];
    posInGiro++;
  }
  int iGiro = atoi(giro);
}

int recycledPairCantForIBetweemAB(int i, int A, int B){
  int cant = 0;
  char pI[8];
  itoa(i,pI,10);
  int nI = strlen(pI);

  set<int> giros;

//  cout << "nI es " << nI << endl;

  for(int k = 1; k<nI; k++){
    char giro[nI];
    girarK(pI,nI,k,giro);
    int iGiro = atoi(giro);

//    fprintf(stdout,"   i: %s \n", pI);
//    fprintf(stdout,"giro: %s (%d) \n", giro, k);

    if(i < iGiro && A <= iGiro && iGiro <= B && giros.count(iGiro)<=0){
      giros.insert(iGiro);
      cant++;
    }
  }
//  fprintf(stdout,"cant: %d **\n", cant);
  return cant;
}

int procesarDatos(int A, int B){
  if(B<A) return 0;
  int cantidad = 0;
  int n = B - A + 1;
  for(int i= A; i <= B; i++){
    cantidad += recycledPairCantForIBetweemAB(i, A, B);

//    fprintf(stdout,"cant: %d -----\n", cantidad);
  }
  return cantidad;
}

void imprimir(char* num, int size){
    for(int i = 0; i < size; i++){
      cout << num[i];
    }
    cout << endl;
}

int main(int argc, char *argv[]){

  int T, cantidad, A, B;
  char pA [8];
  char pB [8];
  FILE * origen;
  FILE * destino;

  origen = fopen ("C-large.in" , "r");
  if (origen == NULL){
    perror ("Error opening in file");
  } else {
    destino= fopen("C-large.out","w");
    if (destino == NULL){
      perror ("Error opening out file");
    } else {
      fscanf (origen, "%d", &T);
      for(int tc=1; tc<=T; tc++){
        fscanf (origen, "%d", &A);
        itoa(A, pA,10);
        fscanf (origen, "%d", &B);
        itoa(B, pB,10);
//        printf ("decimal: %s\n",pA);
//        printf ("decimal: %s\n",pB);
//        imprimir(pA,strlen(pA));
//        imprimir(pB,strlen(pB));
        cantidad = procesarDatos(A,B);
        fprintf(destino,"Case #%d: %d", tc, cantidad);
        if(tc != T) fprintf(destino,"\n");
      }
    }
  }

  fclose(origen);
  fclose(destino);

  return EXIT_SUCCESS;
}
