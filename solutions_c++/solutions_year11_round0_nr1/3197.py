#include <stdio.h>

FILE * ent, * sal;
int t;
int n;
char robot[4];
int boton;
int posO = 1;
int posB = 1;
int tiempo;
int total;
char movAnt = 'I';


void limpia()
{
	posO = 1;
	posB = 1;
	total = 0;
	movAnt = 'I';
	tiempo = 0;
}

int damePos()
{
	int res;
	if (robot[0] == 'O')
	{
		res = posO;
		posO = boton;
	}
	else
	{	
		res = posB;
		posB = boton;
	}
	return res;
}
/*
void sumaTiempo(int tiempoP)
{
	if (robot[0] == 'O')
		tiempoO += tiempoP;
	else 
		tiempoB += tiempoP;
}

int tiempoRAnt()
{
	int res;
	if (robot[0] == 'O')
	{
		res = tiempoB;
		tiempoB = 0;
	}
	else
	{
		res = tiempoO;
		tiempoO = 0;
	}	
//	printf("%d ", res);
	return res;
}
*/
int abso(int a)
{
	if (a < 0)
		return -a;
}

int main()
{
	ent = fopen("inputL.txt", "r");
	sal = fopen("outputL.txt", "w");
	
	fscanf(ent, "%d", &t);
	
	
	for(int caso = 1; caso <= t; caso++)
	{
		
		//printf("asdfo\n");
		fscanf(ent, "%d", &n);
	
	
		for(int i = 1; i <= n; i++)
		{
			fscanf(ent, "%s %d", robot, &boton);
	
			

			int tiempoTemp = abso(boton - damePos()) + 1;
			
			if (tiempo == 0)
			{
				tiempo += tiempoTemp;
				movAnt = robot[0];
			}
			else if (tiempo > 0)
			{
				if (movAnt == robot[0])
				{
					tiempo += tiempoTemp;
				}
				else
				{
					tiempoTemp -= tiempo;					
					tiempo = 0;
					if (tiempoTemp <= 0)
						tiempoTemp = 1;
					tiempo += tiempoTemp;
					movAnt = robot[0];

				}
			}
			
			total += tiempoTemp;
			//printf("%d\n", total);
			//printf("%d %c %d\n", tiempoTemp, robot[0], boton);		*/
		}

		fprintf(sal, "Case #%d: %d\n", caso, total);
		limpia();
		//printf("g\n");
		
	}

	return 0;
}



