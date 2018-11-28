#include <cstdio>
#include <cstring>
#include <cctype>

using namespace std;

char referencia[] = "$welcome to code jam";

int main () {

  int numcasos;

  scanf ("%d", &numcasos);

  char caca = getchar ();

  for (int caso = 1; caso <= numcasos; caso++) {

    char linea [600];

    linea[0] = '$';

    fgets (linea+1, 599, stdin);

    linea[strlen(linea)-1] = '\0';

    int matriz [600][20];

    for (int i = 0; i < 600; i++)
      for (int j = 0; j < 20; j++)
	matriz[i][j] = 0;

    for (int i = 1; i < strlen(linea); i++)
      if (linea[i] == referencia[1])
	matriz[i][1] = 1;

    for (int j = 2; j < strlen(referencia); j++) {   
      for (int i = j; i < strlen (linea); i++) {
	if (linea[i] == referencia[j])
	  for (int k = 0; k < i; k++)
	    matriz[i][j] = (matriz[i][j] + matriz[k][j-1]) % 10000;
      }
     }

    int solucion = 0;

    for (int i = 0; i < strlen(linea); i++)
      solucion = (solucion + matriz[i][strlen(referencia)-1]) % 10000;
     
    printf ("Case #%d: ", caso);

    if (solucion < 10)
      printf ("000");
    else if (solucion < 100)
      printf ("00");
    else if (solucion < 1000)
      printf ("0");
    printf ("%d\n", solucion);

  }

  return 0;
}
