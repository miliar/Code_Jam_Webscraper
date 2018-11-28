// Welcome.cpp : Defines the entry point for the console application.
//

#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

char texto[1000];
int longitud;
int formas[500][100];
char welcome[]="welcome to code jam";

int cuentaformas(int pos,int letra)
{
	if (welcome[letra]==0)
	{
		return 1;
	}
	if (formas[pos][letra]>=0)
	{
		return formas[pos][letra];
	}
	int res=0;
	for (int i=pos;texto[i]!=0;i++)
	{
		if (texto[i]==welcome[letra])
		{
			res=(res+(cuentaformas(i+1,letra+1)))%1000;
		}
	}
	return formas[pos][letra]=res;
}

int main(int argc, char* argv[])
{
	FILE *entrada = fopen("input.txt","rt");
	FILE *salida = fopen("salida.txt","wt");
	int T;
	fscanf(entrada,"%d\n",&T);
	for (int t=0;t<T;t++)
	{
		if (t>0)
		{
			fprintf(salida,"\n");
		}
		fprintf(salida,"Case #%d: ",t+1);
		longitud=0;
		memset(formas,-1,sizeof(formas));
		char aux;
		while (fscanf(entrada,"%c",&aux)==1)
		{
			if (aux=='\n')
			{
				break;
			}
			texto[longitud]=aux;
			longitud++;
		}
		texto[longitud]=0;
		fprintf(salida,"%04d",cuentaformas(0,0));
	}
	fclose(entrada);
	fclose(salida);
	return 0;
}

