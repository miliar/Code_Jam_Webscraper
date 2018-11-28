#include <cstdio>

struct snapper {

  bool encendido;
  bool power;

};

snapper snappersAct [40];
snapper snappersSig [40];

void inicializarSnappers (void) {

  for (int i = 0; i < 40; i++) {
    snappersAct[i].encendido = false;
    snappersAct[i].power = false;
    snappersSig[i].encendido = false;
    snappersSig[i].power = false;
  }

  snappersAct[0].power = true;
  snappersSig[0].power = true;

}


int main () {

  int ncasos;

  scanf ("%d", &ncasos);

  snapper *act, *sig, *inter;

  for (int caso = 1; caso <= ncasos; caso++) {

    inicializarSnappers ();

    act = snappersAct;
    sig = snappersSig;

    bool bombilla = false;

    int nsnappers, ncambios;

    scanf ("%d%d", &nsnappers, &ncambios);

    //for (int i = 0; i < nsnappers; i++) 
    //printf ("Snapper %d: encendido = %d power = %d\n", i, act[i].encendido, act[i].power);
    //    printf ("\n");

    for (int c = 0; c < ncambios; c++) {
      
      sig[0].encendido = !act[0].encendido;

      for (int i = 1; i < nsnappers; i++) {

	if (act[i].power)
	  sig[i].encendido = !act[i].encendido;
	else
	  sig[i].encendido = act[i].encendido;
	

	if (sig[i-1].power && sig[i-1].encendido)
	  sig[i].power = true;
	else
	  sig[i].power = false;
      }

      // Mostramos el contenido

      //for (int i = 0; i < nsnappers; i++) 
      //printf ("Snapper %d: encendido = %d power = %d\n", i, sig[i].encendido, sig[i].power);
      //printf ("\n");
      
      // Intercambio de punteros
      inter = act;
      act = sig;
      sig = inter;
      
    }

    bombilla = (act[nsnappers-1].encendido && act[nsnappers-1].power) ? true : false;

    printf ("Case #%d: %s\n", caso, bombilla ? "ON" : "OFF");

  }

  return 0;
}
