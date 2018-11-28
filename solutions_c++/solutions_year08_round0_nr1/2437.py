#include <stdio.h>
#include <limits.h>
struct nodo
{
	int sig[256];
	int val;
};
char cadena[105];
int tam;
int nLetra;
int nBusca;
nodo hash[100000];
int lista[10001];
int tabla[1001][101];
int sig;
void mete(int code)
{
	int pos=0;
	for(int i=0;i<tam;i++)
	{
		if(hash[pos].sig[cadena[i]]==0)
		{
			sig++;
			hash[pos].sig[cadena[i]]=sig;
			pos=sig;
		}else
		{
			pos=hash[pos].sig[cadena[i]];
		}
	}
	sig++;
	hash[pos].sig[0]=sig;
	hash[sig].val=code;
}
int saca()
{
	int pos=0;
	for(int i=0;i<tam;i++)
	{
			pos=hash[pos].sig[cadena[i]];
	}
	pos = hash[pos].sig[0];
	return hash[pos].val;
}
void leer()
{
	char aux;
	scanf("%d ",&nLetra);
	for(int i=0;i<nLetra;i++)
	{
		tam=0;
		scanf("%c",&aux);
		while(aux!='\n')
		{
			cadena[tam]=aux;
			tam++;
			scanf("%c",&aux);
		}
		mete(i);
	}
	scanf("%d ",&nBusca);
	for(int i=0;i<nBusca;i++)
	{
		tam=0;
		scanf("%c",&aux);
		while(aux!='\n')
		{
			cadena[tam]=aux;
			tam++;
			scanf("%c",&aux);
		}
		lista[i] = saca();
	}
}

void resolver()
{
	int si;
	for(int pos=nBusca-1;pos>=0;pos--)
	{
		si=INT_MAX;
		for(int i=0;i<nLetra;i++)
		{
			if(lista[pos]!=i)
			{
				tabla[pos][i] = tabla[pos+1][i];
				if(si>tabla[pos][i])
				{
					si=tabla[pos][i];
				}
			}
		}
		tabla[pos][lista[pos]] = si +1;
		
	}
	si=INT_MAX;
	for(int i=0;i<nLetra;i++)
	{
		if(si>tabla[0][i])
		{
			si=tabla[0][i];
		}
	}
	printf("%d\n",si);
}
void limpia()
{
	for(int i=0;i<101;i++)
	{
		for(int j=0;j<1001;j++)
		{
			tabla[j][i]=0;
		}
	}
	for(int i=0;i<=sig;i++)
	{
		for(int j=0;j<256;j++)
		{
			hash[i].sig[j]=0;
			hash[i].val=0;
		}
	}
	sig=0;
}
int main()
{
	int casos;
	scanf("%d",&casos);
	for(int i=0;i<casos;i++)
	{
		printf("Case #%d: ",(i+1));
		
		leer();
		resolver();
		limpia();
	}
	return 0;
}
