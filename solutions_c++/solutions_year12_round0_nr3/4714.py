// Dedicado a Villi & Natalia. Sin los animos que me dan y las manos que me echan, no se que haría ^_^

#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <map>
#include <hash_map>
#include <set>
#include <algorithm>

#define PUSH_FRONT(vec, elem) vec.insert(0, elem)
#define SORT_VEC(vec) sort(vec.begin(), vec.end())
#define FOR_VEC(it, vec) for(vec::iterator it = vec.begin(); it != vec.end(); ++it)


using namespace std;


//map<int, int> numerosUsados;

int A, B;

char AA[100], BB[100];
int tamanio;

int cuentaReciclados(int m)
{
	if(m > B) return -1;

	set<int> usados;
	char numero[50];
	sprintf(numero, "%d", m);
	char numAux[50];
	memset(numAux, 0, 50);

	int validos = 0;
	int n;

	int t = strlen(numero);
	if(t < 2) return 0;

	for(int i = 1; i < t; ++i)
	{
		memcpy(numAux, numero + i, t - i);
		memcpy(numAux + t - i, numero, i);
		n = atoi(numAux);
		if(usados.count(n)) continue;
		usados.insert(n);
		if(n <= B && n > A && m < n)
		{

			//numerosUsados[n] = true;
			++validos;
		}
	}
	return validos;
}


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
	
	int i, d, pos, cuenta, cuentaAux;

	fscanf(fin, "%d", &numCasos);

	for(int caso = 1; caso <= numCasos; ++caso)
	{
		fscanf(fin, "%d %d", &A, &B);

		// Esto es una chapuza... Lo se... Pero ando con prisa y no tengo ganas de comerme el tarro haciendolo mejor -.-
		// Aparte. si pasa, pasa :P
		sprintf(AA, "%d", A);
		sprintf(BB, "%d", B);

		

		tamanio = strlen(AA);
		
		

		cuenta = 0;

		for(int nnn = A; nnn <= B; ++nnn)
		{
			cuenta += cuentaReciclados(nnn);
		}

		fprintf(fout, "Case #%d: %d\n", caso, cuenta);
	}

	fclose(fin);
	fclose(fout);

    delete [] archEntrada;
    delete [] archSalida;
}