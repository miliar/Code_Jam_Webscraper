// test.cpp: define el punto de entrada de la aplicación de consola.
//

#include <stdio.h>

/*The first line of the input gives the number of test cases, T. T test cases follow.

Each test case consists of a single line beginning with a positive integer N,
representing the number of buttons that need to be pressed. 
This is followed by N terms of the form "Ri Pi" where Ri is a robot color (always 'O' or 'B'), and Pi is a button position. */

/*For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1)
and y is the minimum number of seconds required for the robots to push the given buttons, in order. */ 

FILE* archivoEntrada = fopen("C:\\Users\\carlos\\Downloads\\A-large.in","rt");
FILE* archivoSalida = fopen("A-large.out","wt");

int T,N;
char robot[101];
int boton[101];

void CargarCasos()
{
	fscanf(archivoEntrada, "%d", &T);
}

void CargarPrueba()
{
	fscanf(archivoEntrada, "%d", &N);
	for(int cont = 0; cont < N; cont++)
	{
		fscanf(archivoEntrada, " %c %d", &robot[cont], &boton[cont]);
	}
}

int ObtenerPosicionNaranja(int cont)
{
	int aux = 0;
	bool encontro = false;
	for(int i = 0; i < N; i++)
	{
		if(robot[i] == 'O')
		{
			aux++;
			if(aux>cont)
			{
				return i;
			}
		}
	}
	return -1;
}

int ObtenerPosicionAzul(int cont)
{
	int aux = 0;
	bool encontro = false;
	for(int i = 0; i < N; i++)
	{
		if(robot[i] == 'B')
		{
			aux++;
			if(aux>cont)
			{
				return i;
			}
		}
	}
	return -1;
}
int AnalizarMovimientos()
{
	bool turnoNaranja;
	int presionesNaranja = 0;
	int presionesAzul = 0;
	int segundos = 0;
	int posNaranja, posAzul;
	posNaranja = posAzul = 1;
	int cont = 0;
	turnoNaranja = (robot[cont] == 'O') ? true : false;
	
	//int cont = 0;
	while(cont < N)
	{
		if(turnoNaranja)
		{
			if(posNaranja == boton[cont])
			{
				cont++;
				presionesNaranja++;
				if(posAzul < boton[ObtenerPosicionAzul(presionesAzul)] )
				{
					posAzul++;
				}
				else if(posAzul > boton[ObtenerPosicionAzul(presionesAzul)] )
				{
					posAzul--;
				}

				turnoNaranja = (robot[cont] == 'O') ? true : false;
			}
			else
			{
				if(posNaranja < boton[ObtenerPosicionNaranja(presionesNaranja)] )
				{
					posNaranja++;
				}
				else if(posNaranja > boton[ObtenerPosicionNaranja(presionesNaranja)] )
				{
					posNaranja--;
				}
				if(posAzul < boton[ObtenerPosicionAzul(presionesAzul)] )
				{
					posAzul++;
				}
				else if(posAzul > boton[ObtenerPosicionAzul(presionesAzul)] )
				{
					posAzul--;
				}
				
			}
		}
		else
		{
			if(posAzul == boton[cont])
			{
				presionesAzul++;
				cont++;
				if(posNaranja < boton[ObtenerPosicionNaranja(presionesNaranja)] )
				{
					posNaranja++;
				}
				else if(posNaranja > boton[ObtenerPosicionNaranja(presionesNaranja)] )
				{
					posNaranja--;
				}
				turnoNaranja = (robot[cont] == 'O') ? true : false;
			}
			else
			{
				if(posAzul < boton[ObtenerPosicionAzul(presionesAzul)] )
				{
					posAzul++;
				}
				else if(posAzul > boton[ObtenerPosicionAzul(presionesAzul)] )
				{
					posAzul--;
				}
				if(posNaranja < boton[ObtenerPosicionNaranja(presionesNaranja)] )
				{
					posNaranja++;
				}
				else if(posNaranja > boton[ObtenerPosicionNaranja(presionesNaranja)] )
				{
					posNaranja--;
				}
				
			}
		}
		segundos++;
	}
	return segundos;
}

int main()
{
	int segundos;
	CargarCasos();
	for (int cont = 0; cont < T; cont++)
	{
		CargarPrueba();
		segundos = AnalizarMovimientos();
		fprintf(archivoSalida, "Case #%d: %d\n",cont+1,segundos);
	}
	fclose(archivoEntrada);
	fclose(archivoSalida);
	
	return 0;
}
