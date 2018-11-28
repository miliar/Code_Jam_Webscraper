#include <cstdio>

using namespace std;

char palabras [5100][20];

int main () {

  int l, d, n;

  scanf ("%d %d %d", &l, &d, &n);

  for (int i = 0; i < d; i++)
    scanf ("%s", palabras[i]);

  // Palabras leídas

  // Ahora hacemos el parse de lo que viene y construimos el grafo
  
  for (int caso = 1; caso <= n; caso++) {

    char expresion [10000];
    scanf ("%s", expresion);

    //printf ("Leido: %s\n", expresion);

    bool grafo [30][20];

    for (int i = 0; i < 30; i++)
      for (int j = 0; j < 20; j++)
	grafo[i][j] = false;

    int pos = 0;
    for (int i = 0; i < l; i++) {
      if (expresion[pos] == '(') {
	pos++;
	while (expresion[pos] != ')') {
	  grafo[expresion[pos]-'a'][i] = true;
	  pos++;
	}
      } else grafo[expresion[pos]-'a'][i] = true;
      pos++;
    }

    // Grafo construido. Ahora probamos cada una de las palabras anteriores

    int cuentapalabras = 0;

    for (int i = 0; i < d; i++) {
      bool flag = true;
      for (int j = 0; j < l; j++)
	if (!grafo[palabras[i][j]-'a'][j]) {
	  flag = false;
	  break;
	}
      if (flag)
	cuentapalabras++;
    }

    printf ("Case #%d: %d\n", caso, cuentapalabras);

  }

  return 0;
}
