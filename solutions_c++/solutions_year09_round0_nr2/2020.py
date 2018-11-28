#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int mapAlt[100][100];
char mapBas[100][100];

int x, y, px, py, W, H;

int basX[10001], basY[10001];
int *pbasX, *pbasY;

char basin, basLoc;

int mueve(int &px, int &py)
{
	int d = 0;
	int alt = mapAlt[px][py], alt2;

	if(py)
	{
		alt2 = mapAlt[px][py - 1];
		if(alt2 < alt)
		{
			d = 1;
			alt = alt2;
		}
	}
	if(px)
	{
		alt2 = mapAlt[px - 1][py];
		if(alt2 < alt)
		{
			d = 2;
			alt = alt2;
		}
	}
	if(px < W - 1)
	{
		alt2 = mapAlt[px + 1][py];
		if(alt2 < alt)
		{
			d = 3;
			alt = alt2;
		}
	}
	if(py < H - 1)
	{
		alt2 = mapAlt[px][py + 1];
		if(alt2 < alt)
		{
			d = 4;
			alt = alt2;
		}
	}
	switch(d)
	{
		case 1: 
			--py;
			break;
		case 2: 
			--px;
			break;
		case 3: 
			++px;
			break;
		case 4: 
			++py;
			break;				
	}
	return d;
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

	fscanf(fin, "%d", &numCasos);

	for(int caso = 1; caso <= numCasos; caso++)
	{
		memset(mapAlt, -1, sizeof(mapAlt));
		memset(mapBas, 0, sizeof(mapBas));

		fscanf(fin, "%d %d", &H, &W);
        
        for(y = 0; y < H; y++)
			for(x = 0; x < W; x++)
				fscanf(fin, "%d", &(mapAlt[x][y]));

		basin = 'a';

		for(y = 0; y < H; y++)
			for(x = 0; x < W; x++)
			{
				if(mapBas[x][y]) continue;
				px = x; 
				py = y;
                pbasX = basX;
                pbasY = basY;

                basLoc = basin;
				if(mapBas[px][py] == 0)
                {
                	*pbasX = px;
                    *pbasY = py;
                    ++pbasX;
                    ++pbasY;
                    while(1)
                    {
                        if(mueve(px, py))
                        {
                            if(mapBas[px][py])
                            {
                                basLoc = mapBas[px][py];
								--basin;
                                *pbasX = -1;
                                break;
                            }
                            else
                            {
                                *pbasX = px;
                                *pbasY = py;
                                ++pbasX;
			                    ++pbasY;
                            }
                        }
                        else
                        {
                            *pbasX = -1;
                            break;
                        }
                    }

                    basin++;
                    pbasX = basX;
                    pbasY = basY;
                    while(*pbasX != -1)
                    {
                        mapBas[*pbasX][*pbasY] = basLoc;
                        ++pbasX;
                        ++pbasY;
                    }
                }
			}



		fprintf(fout, "Case #%d:\n", caso);
        for(y = 0; y < H; y++)
        {
			for(x = 0; x < W; x++)
            {
            	fprintf(fout, "%c", mapBas[x][y]);
	            if(x < W - 1) fprintf(fout, " ");
            }
            fprintf(fout, "\n");
        }
	}

	fclose(fin);
	fclose(fout);

    delete [] archEntrada;
    delete [] archSalida;
}