#include <cstdlib>
#include <iostream>
#include<stdio.h>
#define MAXIMO 31

using namespace std;

//void ordenar()

int Snappers(){
	 FILE* archivo;     FILE* archivo2;
	 archivo = fopen("A-small.in", "r");
	 archivo2 = fopen("A-small.out", "w+");
	 int e[MAXIMO];
	 int iNro_Casos = 0;
	 char* estado = "OFF";
	 
	 if(archivo!=NULL){
		fscanf(archivo, "%d\n",
					&iNro_Casos);
		printf("\nNro. de Casos: %d", iNro_Casos);
		// Recorre todos los casos
		int iSnappers = 0; // # de Snappers
		int iSnaps = 0; // # de Snaps
		for(int k = 1; k <= iNro_Casos; k++){
			// Leyendo el # de los Snappers y el # de Snaps
			fscanf(archivo, "%d %d\n", &iSnappers, &iSnaps);
			printf("\n# Snappers: %d # Snaps: %d\n", iSnappers, iSnaps) ;
            // Caso k
            estado = "OFF";
            for (int i = 1; i < MAXIMO; i++) e[i] = 0;
            for (int s = 1; s <= iSnaps; s++){
                e[1] = 1 - e[1];
                int iLimite = s % iSnappers; if (iLimite == 0) iLimite = iSnappers;
                printf("\nLimite: %d", iLimite) ;
                for (int j = 1; j <= iLimite; j++){
                    int nEstados = 0;
                    if (j == 1) {
                          if (e[j] == 0) estado = "OFF"; else estado = "ON";
                          continue;
                    }
                    for (int ee = 1; ee < j; ee++) if ( e[ee] == 1 ) nEstados++;
                    if ( nEstados == (j-1) ) {
                         e[j] == 1 - e[j]; 
                         if (e[j] == 0) estado = "OFF"; else estado = "ON";
                    }
                }
            }
            fprintf(archivo2, "Case #%d: %s\n", k, estado);
		    //if(k==2)  break;
		} // Fin de for k
		fclose(archivo);  fclose(archivo2);
	 } // Fin de if(archivo!=NULL)
  system("PAUSE");
    return EXIT_SUCCESS;
}
void rota(){
     int N = 4;
     int A[4] = {1, 4, 2, 1 };
     int B[4];
     int k = 6, R = 4, nEuros = 0, capacidad = 0;
     
     for (int r = 0; r < R; r++){
         capacidad = 0;
         int i = 0;
         while ( (capacidad + A[i]) <= k ){
            capacidad += A[i]; 
            B[i] = A[i]; i++;
         }
         int z = 0;
         for (int j = i; j <N; j++) {
             A[z] = A[j]; z++;
         }
         for (int j = 0; j < i; j++) {
             A[z] = B[j]; z++;
         }
         for (int j = 0; j < N; j++){
             printf("A[%d]=%d ", j, A[j]);
         }
         printf("\n Capacidad: %d\n", capacidad);
         nEuros += capacidad; 
     }
     printf("\n Euros: %d", nEuros);
}
int ThemePark(){
	 FILE* archivo;     FILE* archivo2;
	 archivo = fopen("C-small-attempt0.in", "r");
	 archivo2 = fopen("C-small-attempt0.out", "w+");
	 int iNro_Casos = 0;
	 int A[1000]; int B[1000];
	 if(archivo!=NULL){
		fscanf(archivo, "%d\n",
					&iNro_Casos);
		printf("\nNro. de Casos: %d", iNro_Casos);
		// Recorre todos los casos
		int k = 6, R = 4, N, nEuros = 0, capacidad = 0;
		for(int c = 1; c <= iNro_Casos; c++){
			 // Leyendo R k N
			 fscanf(archivo, "%d %d %d\n", &R, &k, &N);
			 printf("\nR: %d K: %d N: %d\n", R, k, N) ;
             // Caso k
             for (int a = 0; a < N; a++){
             //char sLinea[100];
                 //fscanf(archivo, "%s\n", &sLinea);
                 if (N == 1) fscanf(archivo, "%d", &A[a]);
                 else 
                 fscanf(archivo, "%d ", &A[a]);
                 
             }
             fscanf(archivo, "\n");
             //printf("\nLinea:%s", sLinea);
             nEuros = 0;
             for (int r = 0; r < R; r++){
                 capacidad = 0;
                 int i = 0;
                 while ( ( (capacidad + A[i]) <= k ) && (i < N) ){
                    capacidad += A[i]; 
                    B[i] = A[i]; i++;
                 }
                 int z = 0;
                 for (int j = i; j <N; j++) {
                     A[z] = A[j]; z++;
                 }
                 for (int j = 0; j < i; j++) {
                     A[z] = B[j]; z++;
                 }
                 for (int j = 0; j < N; j++){
                     printf("A[%d]=%d ", j, A[j]);
                 }
                 printf("\n Capacidad: %d\n", capacidad);
                 nEuros += capacidad; 
             }
             printf("\n Euros: %d", nEuros);
             fprintf(archivo2, "Case #%d: %d\n", c, nEuros);
		    //if(k==2)  break;
		} // Fin de for k
		fclose(archivo);  fclose(archivo2);
	 } // Fin de if(archivo!=NULL)
    system("PAUSE");
    return EXIT_SUCCESS;
}
int main(){
    ThemePark();
    //rota();

}
