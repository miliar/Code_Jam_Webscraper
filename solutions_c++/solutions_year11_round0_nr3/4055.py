#include <stdio.h>
#define MAXN 1002

int arr[MAXN];
int n;

int izq, der;
int sIzq, sDer;

int max(int a, int b)
{
	if( a > b )
		return a;
	return b;
}

int buscaMaximo(int pos)
{
	int aux, aux2;
	if( pos == n )
	{
		if( (izq ^ der) != 0  && sIzq != 0 && sDer != 0)
			return max(sIzq, sDer);
		return -1;
	}
	izq ^= arr[pos];
	sIzq += arr[pos];
	aux = buscaMaximo(pos+1);
	izq ^= arr[pos];
	sIzq -= arr[pos];
	der ^= arr[pos];
	sDer += arr[pos];
	aux2 = buscaMaximo(pos+1);
	sDer -= arr[pos];
	return max(aux, aux2);
}

void caso(int nCaso)
{
	int acum = 0;
	scanf("%d", &n);
	for(int i=0; i<n; i++)
	{
		scanf("%d", &arr[i]);
		acum ^= arr[i];
	}
	if( acum != 0 )
	{
		printf("Case #%d: NO\n", nCaso);
		return;
	}
	else
	{
		if(buscaMaximo(0) == -1 )
			printf("Case #%d: NO\n", nCaso);
		else                               
			printf("Case #%d: %d\n", nCaso, buscaMaximo(0));

	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int i=1; i<=T; i++)
		caso(i);
	return 0;
}
