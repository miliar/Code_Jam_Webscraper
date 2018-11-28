#include <stdio.h>

char grilla[6][6];
int points;

void clean_grilla()
{
	int i,j;
	for(i = 0; i < 6; i++)
		for(j = 0; j < 6; j++)
			grilla[i][j] = 'k';
}

void print_grilla()
{
	int i,j;
	for(i = 0; i < 6; i++)
	{
		printf("\n");
		for(j = 0; j < 6; j++)
			printf(" %c",grilla[i][j]);
	}
}

void count_points()
{
	int i,j;
	for(i = 1; i < 5; i++)
		for(j = 1; j < 5; j++)
			if(grilla[i][j] == '.')
			 	points++;
}

int main (int argc, char** argv)
{
	FILE * in, *out;
	in = fopen (argv[1],"r");
	out = fopen ("sample.out","w");
	//leer archivo
	int nro_casos;
	int N = 4,M = 4;

	int i,j,k;
	
	int caso_activo = 1;

	fscanf(in, "%d", &nro_casos);


	for(caso_activo = 1 ; caso_activo <= nro_casos ; caso_activo++)
	{
		bool gano_X = false;
		bool gano_O = false;
		points = 0;

		clean_grilla();
		//printf("\n N %d M %d", N, M);
		char aux_c;
		//fscanf(in, "%c", &aux_c);
		for(i = 1 ; i <= N ; i++)
		{
			for(j = 1 ; j <= M ; j++)
			{
				fscanf(in, "%c", &aux_c);
				if(aux_c != '\n') grilla[i][j] = aux_c;
				else j--;
			}
		}

		count_points();
		//print_grilla();
		//todo leído, momento de verificar la condición

		//verificando filas
		for(i = 1 ; i <= 4 ; i++)
		{
			int nro_X = 0, nro_O = 0;
			for(j = 1 ; j <= 4 ; j++)
			{
				if(grilla[i][j] == 'X')
					nro_X++;
				if(grilla[i][j] == 'O')
					nro_O++;
				if(grilla[i][j] == 'T')
				{
					nro_X++;
					nro_O++;
				}
			}
			if(nro_O == 4){ gano_O = true; break;}
			if(nro_X == 4){ gano_X = true; break;}
		}
		//verificando columnas
		for(j = 1 ; j <= 4 ; j++)
		{
			int nro_X = 0, nro_O = 0;
			for(i = 1 ; i <= 4 ; i++)
			{
				if(grilla[i][j] == 'X')
					nro_X++;
				if(grilla[i][j] == 'O')
					nro_O++;
				if(grilla[i][j] == 'T')
				{
					nro_X++;
					nro_O++;
				}
			}
			if(nro_O == 4){ gano_O = true; break;}
			if(nro_X == 4){ gano_X = true; break;}
		}
		int nro_X = 0, nro_O = 0;
		//verificando diagonales
		for(i = 1 ; i <= 4 ; i++)
		{
			
			if(grilla[i][i] == 'X')
					nro_X++;
			if(grilla[i][i] == 'O')
				nro_O++;
			if(grilla[i][i] == 'T')
			{
				nro_X++;
				nro_O++;
			}
		}

		if(nro_O == 4){ gano_O = true; }
		if(nro_X == 4){ gano_X = true; }

		nro_X = 0; nro_O = 0;
		for(i = 1 ; i <= 4 ; i++)
		{
			
			if(grilla[i][5-i] == 'X')
					nro_X++;
			if(grilla[i][5-i] == 'O')
				nro_O++;
			if(grilla[i][5-i] == 'T')
			{
				nro_X++;
				nro_O++;
			}
		}

		if(nro_O == 4){ gano_O = true; }
		if(nro_X == 4){ gano_X = true; }

		if(gano_X)
		{
			fprintf(out,"Case #%d: X won\n", caso_activo);
		}
		else if(gano_O)
		{
			fprintf(out,"Case #%d: O won\n", caso_activo);
		}
		else if(points > 0)
		{
			fprintf(out,"Case #%d: Game has not completed\n", caso_activo);
		}
		else
		{
			fprintf(out,"Case #%d: Draw\n", caso_activo);
		}

	}

	fclose (in);
	fclose (out);
	return 0;
}