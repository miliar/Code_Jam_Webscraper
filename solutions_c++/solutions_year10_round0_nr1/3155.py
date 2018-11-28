//  Saludos a los depres de parte de Aburrrrrrrrr (hoy estamos a 8, ergo 9 erres ^_^ ).
// Y a ^galoncete^ también, faltaría más, a ver si algún año te apuntas ¬¬

#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <map>
#include <hash_map>
#include <algorithm>
#include <cmath>


using namespace std;


// 2^27 = 134217728
// 10^8 = 100000000
// Ergo, solo hace falta mirar casos con R <= 26

void main(int argc, char **args)
{
	if(argc < 2) return;

    char *archEntrada = new char[strlen(args[1]) + 4];
    char *archSalida = new char[strlen(args[1]) + 5];
    strcpy(archEntrada, args[1]);
    strcpy(archEntrada + strlen(args[1]), ".in");
	strcpy(archSalida, args[1]);
    strcpy(archSalida + strlen(args[1]), ".out");

    FILE *fin = fopen(archEntrada, "r");
	FILE *fout = fopen(archSalida, "w");

	int numCasos;

	unsigned long R, k;

	unsigned long long RR, i, kk;

	char estado[4];

	fscanf(fin, "%d", &numCasos);

	for(int caso = 1; caso <= numCasos; caso++)
	{
		fscanf(fin, "%d %d", &R, &k);

		strcpy(estado, "OFF");

		//if((R <= k) && (k % 2) && (R < 27)) // Por si acaso... Si no ejecuta en 8 minutos la descomento
		if((R <= k) && (k % 2))				
		{
			RR = 1 << R;

			for(i = 0, kk = 0; kk < k; ++i)
			{
				kk = (RR * (i + 1)) - 1;
			}		
			
			if(kk == k)
			{
				strcpy(estado, "ON");				
			}
		}


		fprintf(fout, "Case #%d: %s\n", caso, estado);
	}

	fclose(fin);
	fclose(fout);

    delete [] archEntrada;
    delete [] archSalida;
}