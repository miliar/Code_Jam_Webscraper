#include <cstdlib>
#include <iostream>
#include <fstream>
#include <list>

using namespace std;

  FILE * prueba;

bool existeDuplaSorpresa(int puntaje, int k){
  bool existe = false;

  int kMenos2 = k-2;
  int kMenos1 = k-1;
  int kMas1 = k+1;
  int kMas2 = k+2;

  int puntajeCuentasKOpcion1 = puntaje - k;
  puntajeCuentasKOpcion1 -= kMenos2;
  int puntajeCuentasKOpcion2 = puntaje - k;
  puntajeCuentasKOpcion2 -= kMas2;
  int puntajeCuentasKOpcion3 = puntaje - kMenos1;
  puntajeCuentasKOpcion3 -= kMenos2;
  int puntajeCuentasKOpcion4 = puntaje - kMenos1;
  puntajeCuentasKOpcion4 -= kMas1;
  int puntajeCuentasKOpcion5 = puntaje - kMenos2;
  puntajeCuentasKOpcion5 -= kMenos2;
  int puntajeCuentasKOpcion6 = puntaje - kMas1;
  puntajeCuentasKOpcion6 -= kMas2;
  int puntajeCuentasKOpcion7 = puntaje - kMas2;
  puntajeCuentasKOpcion7 -= kMas2;

  bool existe1 = puntajeCuentasKOpcion1 == 0 && 0 <= kMenos2 && kMenos2 <= 10;
  bool existe2 = puntajeCuentasKOpcion2 == 0 && 0 <= kMas2 && kMas2 <= 10;
  bool existe3 = puntajeCuentasKOpcion3 == 0 && 0 <= kMenos1 && kMenos1 <= 10 && 0 <= kMenos2 && kMenos2 <= 10;
  bool existe4 = puntajeCuentasKOpcion4 == 0 && 0 <= kMenos1 && kMenos1 <= 10 && 0 <= kMas1 && kMas1 <= 10;
  bool existe5 = puntajeCuentasKOpcion5 == 0 && 0 <= kMenos2 && kMenos2 <= 10;
  bool existe6 = puntajeCuentasKOpcion6 == 0 && 0 <= kMas1 && kMas1 <= 10 && 0 <= kMas2 && kMas2 <= 10;
  bool existe7 = puntajeCuentasKOpcion7 == 0 && 0 <= kMas2 && kMas2 <= 10;

  existe = existe1 || existe2 || existe3 || existe4 || existe5 || existe6 || existe7;

       if(existe1) fprintf(prueba, "S existe1: (%d, %d, %d)\n", k, k, kMenos2);
  else if(existe2) fprintf(prueba, "S existe2: (%d, %d, %d)\n", k, k, kMas2);
  else if(existe3) fprintf(prueba, "S existe3: (%d, %d, %d)\n", k, kMenos1, kMenos2);
  else if(existe4) fprintf(prueba, "S existe4: (%d, %d, %d)\n", k, kMenos1, kMas1);
  else if(existe5) fprintf(prueba, "S existe5: (%d, %d, %d)\n", k, kMenos2, kMenos2);
  else if(existe6) fprintf(prueba, "S existe6: (%d, %d, %d)\n", k, kMas1, kMas2);
  else if(existe7) fprintf(prueba, "S existe7: (%d, %d, %d)\n", k, kMas2, kMas2);

  return existe;
}

bool existeTriplaSorpresaMayorIgualP(int puntaje, int p){
  bool existe = false;
  int puntajeCuentas = puntaje;
  for(int k=p; k<=10 && !existe; k++){
    puntajeCuentas -= k;
    if(puntajeCuentas >= 0){
        existe = existe || existeDuplaSorpresa(puntajeCuentas, k);
    }
    puntajeCuentas = puntaje;
  }
  return existe;
}

bool existeDuplaNoSorpresa(int puntaje, int k){
  bool existe = false;

  int kMenos1 = k-1;
  int kMas1 = k+1;

  int puntajeCuentasKOpcion1 = puntaje - k;
  puntajeCuentasKOpcion1 -= kMenos1;
  int puntajeCuentasKOpcion2 = puntaje - k;
  puntajeCuentasKOpcion2 -= k;
  int puntajeCuentasKOpcion3 = puntaje - k;
  puntajeCuentasKOpcion3 -= kMas1;
  int puntajeCuentasKOpcion4 = puntaje - kMenos1;
  puntajeCuentasKOpcion4 -= kMenos1;
  int puntajeCuentasKOpcion5 = puntaje - kMas1;
  puntajeCuentasKOpcion5 -= kMas1;

  bool existe1 = puntajeCuentasKOpcion1 == 0 && 0 <= kMenos1 && kMenos1 <= 10;
  bool existe2 = puntajeCuentasKOpcion2 == 0;
  bool existe3 = puntajeCuentasKOpcion3 == 0 && 0 <= kMas1 && kMas1 <= 10;
  bool existe4 = puntajeCuentasKOpcion4 == 0 && 0 <= kMenos1 && kMenos1 <= 10;
  bool existe5 = puntajeCuentasKOpcion5 == 0 && 0 <= kMas1 && kMas1 <= 10;

       if(existe1) fprintf(prueba, "N existe1: (%d, %d, %d)\n", k, k, kMenos1);
  else if(existe2) fprintf(prueba, "N existe2: (%d, %d, %d)\n", k, k, k);
  else if(existe3) fprintf(prueba, "N existe3: (%d, %d, %d)\n", k, k, kMas1);
  else if(existe4) fprintf(prueba, "N existe4: (%d, %d, %d)\n", k, kMenos1, kMenos1);
  else if(existe5) fprintf(prueba, "N existe5: (%d, %d, %d)\n", k, kMas1, kMas1);

  existe = existe1 || existe2 || existe3 || existe4 || existe5;

  return existe;
}

bool existeTriplaNoSorpresaMayorIgualP(int puntaje, int p){
  bool existe = false;
  int puntajeCuentas = puntaje;
  for(int k=p; k<=10 && !existe; k++){
    puntajeCuentas -= k;
    if(puntajeCuentas >= 0){
        existe = existe || existeDuplaNoSorpresa(puntajeCuentas, k);
    }
    puntajeCuentas = puntaje;
  }
  return existe;
}

int procesarDatos(int* googlers, int N, int S, int p){
  //if(p==0) return N;
  int cantMejor = 0;
  bool comunes[N];
  bool sopresas[N];
  int existenAmbasPosibilidades = 0;
  int csorpresas = S;
  int cantSorpresas = 0;
  for(int i = 0; i < N; i++){

    fprintf(prueba, "Puntaje: %d\n", googlers[i]);//////

    int puntaje = googlers[i];
    comunes[i] = existeTriplaNoSorpresaMayorIgualP(puntaje, p);
    sopresas[i] = existeTriplaSorpresaMayorIgualP(puntaje, p);
  }
  for(int j = 0; j < N; j++){
    if (comunes[j]){
      cantMejor++;
    }
    if (sopresas[j] && !comunes[j]){
      cantSorpresas++;
    }
  }
  if(cantSorpresas <= S){
      cantMejor += cantSorpresas;
  } else if(cantSorpresas > S){
    cantMejor += S;
  }

//  for(int j = 0; j < N; j++){
//    if ((comunes[j]) && !(sopresas[j])){
//      cantMejor++;
//    } else if(csorpresas > 0 && !(comunes[j]) && (sopresas[j])){
//      cantMejor++;
//      csorpresas--;
//    } else if(csorpresas > 0 && (comunes[j]) && (sopresas[j])){
//      existenAmbasPosibilidades++;
//    } else if(csorpresas == 0 && (comunes[j]) && (sopresas[j])){
//      cantMejor++;
//    }
//  }
//  if(csorpresas==0 || (csorpresas>0 && csorpresas <= existenAmbasPosibilidades)) cantMejor += existenAmbasPosibilidades;

  return cantMejor;
}

int main(int argc, char *argv[]){

    prueba = fopen("pruebaL.out","w");////

  int T, N, S, p, cantidad, puntaje;
  char* s;
  //bool existe = true;
  FILE * origen;
  FILE * destino;

  origen = fopen ("B-large.in" , "r");
  if (origen == NULL){
    perror ("Error opening in file");
  } else {
    destino= fopen("B-large.out","w");
    if (destino == NULL){
      perror ("Error opening out file");
    } else {
      fscanf (origen, "%d", &T);
      for(int tc=1; tc<=T; tc++){
        fprintf(prueba, "**********Case #%d:**********\n", tc);////
        //existe = true;
        fscanf (origen, "%d", &N);
        fscanf (origen, "%d", &S);
        fscanf (origen, "%d", &p);
        fprintf(prueba, "N: %d - S: %d - p: %d\n", N, S, p);
        int googlers[N];
        for(int ti=0; ti<N; ti++){
          fscanf (origen, "%d", &puntaje);
          googlers[ti] = puntaje;
          //if(puntaje > 30) existe = false;
        }
        //(!existe) ? cantidad = 0 : cantidad = procesarDatos(googlers,N,S,p);
        cantidad = procesarDatos(googlers,N,S,p);

        fprintf(prueba, "Cantidad: %d\n", cantidad);////

        fprintf(destino,"Case #%d: %d", tc, cantidad);
        if(tc != T) fprintf(destino,"\n");
        //delete[] googlers;
      }
    }
  }

  fclose(origen);
  fclose(destino);
  fclose(prueba);

  return EXIT_SUCCESS;
}
