#include<string.h>
#include<stdio.h>
#include<stdlib.h>

int a,b;
int saida;
int repeticao[2000002];
int contador;


void combina(int j)
{
	char numero[2000002];
	char permut[2000002];
	int comb;
	int cont;


	sprintf(numero,"%d",j);
	for(int i=0;i<strlen(numero);i++)
	{
		j = i;
		cont = 0;
		while(cont != strlen(numero))
		{
			permut[cont] = numero[j];
			cont++;

			if(j == strlen(numero)-1)
				j = 0;
			else
				j++;
		}
		permut[cont] = '\0';
		comb = atoi(permut);

		if(comb >= a && comb <= b && repeticao[comb] == 0)
		{
			contador++;
			repeticao[comb] = 1;
		}
	}

}

int main()
{
	int t,i,j;
	int pares;
	
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		memset(repeticao,0,sizeof(repeticao));
		saida = 0;

		scanf("%d %d",&a,&b);
		for(j=a;j<=b;j++)
		{
			contador = 0;

			if(repeticao[j] == 0)
				combina(j);

			pares = contador*(contador-1)/2;
			saida += pares;
		}
		
		printf("Case #%d: %d\n",i,saida);
	}

	return 0;
}
