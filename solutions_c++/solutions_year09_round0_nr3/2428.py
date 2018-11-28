#include <stdio.h>
#include <string.h>

#define MAXN 1024*2

char welcome[] = "welcome to code jam";

char linha[MAXN];
int tam;
int qnt;

void buscaWelcome(int s, int w)
{
    if ( w >= tam )
    {
	qnt++;
	qnt %= 10000;
	return;
    }

    int t = strlen(linha);

    for ( int j = s ; j < t; j++ )
    {
	if ( linha[j] == welcome[w] ) 
	    buscaWelcome(j+1,w+1);
    }
}

int main (void)
{
    int n;
    scanf("%d%*c",&n);

    tam = strlen(welcome);

    for ( int i = 0 ; i < n ; i++ )
    {
	qnt = 0;
	fgets(linha, sizeof(linha), stdin);
	int t = strlen(linha);

	for ( int j = 0 ; j < t; j++ )
	    if ( linha[j] == welcome[0] )
		    buscaWelcome(j+1,1);

	printf("Case #%d: %04d\n",i+1,qnt);
    }
}

