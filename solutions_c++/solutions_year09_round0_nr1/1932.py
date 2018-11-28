#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <map>
#include <hash_map>
#include <algorithm>

using namespace std;

char diccio[5000][16];


void main(int argc, char **args)
{
	vector <char *> vecPosibles;
	

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
	int palabros;
	int longitud;


	fscanf(fin, "%d %d %d", &longitud, &palabros, &numCasos);

	
	for(int i = 0; i < palabros; i++) 
	{		
		fscanf(fin, "%s", diccio[i]);		
	}

	char *linea = new char[0xFFFFFFF];
	char *letras = new char[0xFFFFFFF];
	char *letrasAux;
	char *palAux;

	int posicion;

	int palabrasPosibles;

	for(int caso = 1; caso <= numCasos; caso++)
	{		
		vecPosibles.clear();
				
		fscanf(fin, "%s", linea);

		//vecPosibles.push_back(new char[longitud]);

		posicion = 0;

		for(int p = 0; p < palabros; p++) vecPosibles.push_back(diccio[p]);

		for(unsigned int c = 0; c < strlen(linea); c++)
		{
			if(linea[c] == '(')
			{
				letrasAux = letras;
				++c;
				while(linea[c] != ')') 
				{
					*letrasAux  = linea[c];
					++letrasAux;
					++c;					
				}

				*letrasAux = 0;

				for(unsigned int p = 0; (p < vecPosibles.size()) && vecPosibles.size(); ++p)
				{
					palAux = vecPosibles.at(p);
					letrasAux = letras;
					while(*letrasAux)
					{
						if(palAux[posicion] == *letrasAux)
						{
							break;
						}
						++letrasAux;
					}
					if(*letrasAux == 0) 
					{
						vecPosibles.erase(vecPosibles.begin() + p);
						--p;
					}
				}
			}
			else
			{
				for(unsigned int p = 0; (p < vecPosibles.size()) && vecPosibles.size(); ++p)
				{
					palAux = vecPosibles.at(p);
					letrasAux = letras;
					if(palAux[posicion] != linea[c])
					{
						vecPosibles.erase(vecPosibles.begin() + p);
						--p;
					}												
				}
			}

			posicion++;
		}

		palabrasPosibles = vecPosibles.size();

		fprintf(fout, "Case #%d: %d\n", caso, palabrasPosibles);
	}

	fclose(fin);
	fclose(fout);

    delete [] archEntrada;
    delete [] archSalida;
}