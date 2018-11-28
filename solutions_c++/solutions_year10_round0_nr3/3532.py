#include <cstdio>

int grupos [1100];

int main () {

  int ncasos;

  scanf ("%d", &ncasos);

  for (int caso = 1; caso <= ncasos; caso++) {

    int nviajes, capacidad, ngrupos;

    scanf ("%d%d%d", &nviajes, &capacidad, &ngrupos);

    for (int i = 0; i < ngrupos; i++)
      scanf ("%d", &grupos[i]);

    int actual = 0;

    int euros = 0;

    for (int viaje = 0; viaje < nviajes; viaje++) {
      int acum = 0;
      int ginicio = actual;
      bool flag = false;
      while (1) {
	if (acum + grupos[actual] > capacidad || (flag && ginicio == actual))
	  break;
	acum += grupos[actual];
	actual++;
	if (actual == ngrupos) {
	  actual = 0;
	  flag = true;
	}
      }
      euros += acum;
    }

    printf ("Case #%d: %d\n", caso, euros);
      
  }
  
  return 0;
}
