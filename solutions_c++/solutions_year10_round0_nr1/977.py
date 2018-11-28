// Snapper.cpp : Defines the entry point for the console application.
//

#include <stdio.h>


int main(int argc, char* argv[])
{
	FILE *entrada=fopen("entrada.txt","r");
	FILE *salida=fopen("salida.txt","w");
	int T,N,K;
	fscanf(entrada,"%d",&T);
	for (int t=1;t<=T;t++)
	{
		fscanf(entrada,"%d %d",&N,&K);
		N=(1<<N)-1;
		if ((K&N)==N)
		{
			fprintf(salida,"Case #%d: ON\n",t);
		}
		else
		{
			fprintf(salida,"Case #%d: OFF\n",t);
		}
	}
	fclose(entrada);
	fclose(salida);
	return 0;
}

