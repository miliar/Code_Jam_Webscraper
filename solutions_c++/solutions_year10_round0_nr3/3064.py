//  Pos este problema va por todos los usuarios de MSX habidos y por haber ^_^ .
// Por cierto, por si alguien que conozca a Nestor lee esto... Decidle que queremos el Dumas!!!! ^_^
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <map>
#include <hash_map>
#include <algorithm>

#define PUSH_FRONT(vec, elem) vec.insert(0, elem)
#define SORT_VEC(vec) sort(vec.begin(), vec.end())
#define FOR_VEC(it, vec) for(vec::iterator it = vec.begin(); it != vec.end(); ++it)

using namespace std;

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

	fscanf(fin, "%d", &numCasos);

	unsigned long R, k, N;
	unsigned long g[2000];
	unsigned long cuantos[1000];
	unsigned long siguiente[1000];

	unsigned long i, j, aux;

	for(int caso = 1; caso <= numCasos; ++caso)
	{
		fscanf(fin, "%d %d %d", &R, &k, &N);
		memset(g, 0, sizeof(g));
		memset(cuantos, 0, sizeof(cuantos));
		memset(siguiente, 0, sizeof(siguiente));

		for(i = 0; i < N; ++i)
		{
			fscanf(fin, "%d", &aux);
			//  No se los demás, pero yo odio los bucles circulares, por eso voy a repetir el vector.
			g[i] = aux;
			g[i + N] = aux;
		}

		// Calculemos cuanta peña pasaría en cada posición del vector, y el próximo grupo que pasaría.
		for(i = 0; i < N; ++i)
		{
			j = i;
			aux = 0;
			while((aux <= k) && (j < (i + N))) // Ojito no nos pasemos.
			{
				aux += g[j++];
			}
			--j;
			if(k < aux)
			{
				aux -= g[j]; // Hay que quitar el exceso.
			}
			

			cuantos[i] = aux;
			j %= N;
			siguiente[i] = j;
		}

		//  Y ahora a ver los que pasan;
		j = aux = 0;
		for(i = 0; i < R; ++i)
		{
			aux += cuantos[j];
			j = siguiente[j];
		}

		fprintf(fout, "Case #%d: %d\n", caso, aux);
	}

	fclose(fin);
	fclose(fout);

    delete [] archEntrada;
    delete [] archSalida;
}