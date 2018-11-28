#include <stdio.h>

char buscadores[102][102];
int consultas[1002];
int tabla[102];
int nBusq, nPreg;
int res;

bool iguales(char *a, char *b)
{
	while(*a != '\0' && *b != '\0')
	{
		if(*a != *b)
			return false;
		a++;
		b++;
	}
	if(*a != *b)
		return false;
	return true;
}

void leeLinea(char *cad)
{
	char aux;
	scanf(" %c", &aux);
	while(aux != '\n')
	{
		*cad = aux;
		cad++;
		scanf("%c", &aux);
	}
	*cad = '\0';
}



void dinamica()
{
	int minimo;
	for(int i=0; i<nBusq; i++)
		tabla[i] = 0;
	for(int i=nPreg-1; i>=0; i--)
	{
		minimo = 1000000;
		for(int j=0; j<nBusq; j++)
			if(tabla[j]<minimo && consultas[i] != j)
				minimo = tabla[j];
		if(consultas[i] != -1)
			tabla[consultas[i]] = minimo + 1;
	}
	res = 1000000;
	for(int i=0; i<nBusq; i++)
		if(res > tabla[i])
			res = tabla[i];
}

void caso(int nCaso)
{
	bool enc;
	char aux[102];
	scanf("%d", &nBusq);
	for(int i=0; i<nBusq; i++)
		leeLinea(buscadores[i]);
	scanf("%d", &nPreg);
	for(int i=0; i<nPreg; i++)
	{
		enc = true;
		leeLinea(aux);
		for(int j=0; j<nBusq; j++)
		{
			if(iguales(buscadores[j], aux))
			{
				consultas[i] = j;
				enc = false;
			}
		}
		if(enc)
			consultas[i] = -1;
	}
	dinamica();
	printf("Case #%d: %d\n", nCaso, res);
}

int main()
{
	int nCasos;
	scanf("%d", &nCasos);
	for(int i=0; i<nCasos; i++)
		caso(i+1);
	return 0;
}

