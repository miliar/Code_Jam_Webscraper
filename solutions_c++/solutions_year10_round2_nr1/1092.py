#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <map>
#include <hash_map>
#include <algorithm>
#include <string>

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

	int N, M, pos;
	char dir[1000];

	string dirAux;

	unsigned long long numMkdirs;

	typedef hash_map<string, bool> MapStr;
		
	MapStr mapDirsExistentes;

	vector<string> vecDirsPaCrear;





	fscanf(fin, "%d", &numCasos);

	for(int caso = 1; caso <= numCasos; ++caso)
	{
		fscanf(fin, "%d %d", &N, &M);
		mapDirsExistentes.clear();
		vecDirsPaCrear.clear();
		numMkdirs = 0;
		for(int i = 0; i < N; ++i)
		{
			fscanf(fin, "%s", dir);
			dirAux = dir;

			while(dirAux.size() > 1)
			{
				if(mapDirsExistentes.count(dirAux) == 0)
				{				
					mapDirsExistentes[dirAux] = true;					
				}
				else
				{
					break;
				}
				pos = dirAux.find_last_of('/');
				
				dirAux = dirAux.substr(0, pos);									
			}

		}

		for(int i = 0; i < M; ++i)
		{
			fscanf(fin, "%s", dir);
			vecDirsPaCrear.push_back(dir);
		}

		sort(vecDirsPaCrear.begin(), vecDirsPaCrear.end());

		for(vector<string>::iterator it = vecDirsPaCrear.begin(); it != vecDirsPaCrear.end(); ++it)
		{
			dirAux = *it;
			//  Hay q extraer los directorios al reves.
			if(mapDirsExistentes.count(dirAux) == 0)
			{
				++numMkdirs;
				mapDirsExistentes[dirAux] = true;
			
				while(1)
				{
					pos = dirAux.find_last_of('/');
					if(pos)
					{
						dirAux = dirAux.substr(0, pos);
						if(mapDirsExistentes.count(dirAux) == 0)
						{
							++numMkdirs;
							mapDirsExistentes[dirAux] = true;
						}
						else
						{
							break;
						}
					}
					else
					{
						break;
					}
				}
			}
		}

	


		fprintf(fout, "Case #%d: %d\n", caso, numMkdirs);
	}

	fclose(fin);
	fclose(fout);

    delete [] archEntrada;
    delete [] archSalida;
}