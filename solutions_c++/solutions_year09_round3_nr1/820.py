#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <map>
#include <hash_map>
#include <algorithm>

using namespace std;

char numero[64];
int numDesc[64];
int longitud;
unsigned long long segundos;

map<char, int> alf;

int base ;
unsigned long long baseMul;


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

	//bool sigue;
	for(int caso = 1; caso <= numCasos; caso++)
	{
		fscanf(fin, "%s", numero);

		
		longitud = strlen(numero);
		
		/*if(longitud == 1)
		{
			fprintf(fout, "Case #%d: 0\n", caso);
			continue;
		}*/

		/*sigue = false;
		for(int n = 1; n < longitud; ++n)
		{
			if(numero[n -1] == numero[n]) 
			{
				if(n == longitud - 1)
				{
					fprintf(fout, "Case #%d: 0\n", caso);
					sigue = true;
				}
			}
		}

		if(sigue) continue;*/

		
		alf.clear();
		memset(numDesc, 0, 64);
		base = 0;

		
		for(int n = 0; n < longitud; ++n)
		{
			if(alf.count(numero[n]))
			{				
				numDesc[n] = alf[numero[n]];
			}
			else
			{
				numDesc[n] = (base == 0) ? 1 : ((base == 1) ? 0 : base);

				alf[numero[n]] = numDesc[n];

				base++;
			}
		}

		if(base <= 1) base = 2;
		segundos = 0;
		baseMul = 1;
		for(int n = 0; n < longitud; n++)
		{			
			segundos += (baseMul * numDesc[longitud - n - 1]);
			baseMul *= base;
		}

		fprintf(fout, "Case #%d: %I64d\n", caso, segundos);
	}

	fclose(fin);
	fclose(fout);

    delete [] archEntrada;
    delete [] archSalida;
}