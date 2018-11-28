#include <cstdio>
#include <cstdlib>

#define MAXVETOR 800
#define MAXNUMSIZE 8

using namespace std;

int cmpint ( const void *p1, const void *p2 )
{
    int *i1, *i2;
    i1 = (int *)p1;
    i2 = (int *)p2;

    return *i1 < *i2;
}
int cmpint2 ( const void *p1, const void *p2 )
{
    int *i1, *i2;
    i1 = (int *)p1;
    i2 = (int *)p2;

    return *i1 > *i2;
}

int main (void)
{
    int vetor1[MAXVETOR], vetor2[MAXVETOR];
    char linha[MAXVETOR*MAXNUMSIZE];
    int t, n, i, j, tam, tamtemp, sum;

    fgets(linha, sizeof(linha), stdin);
    sscanf(linha, "%d", &t);

    for ( i = 0 ; i < t ; i++ )
    {
	fgets(linha, sizeof(linha), stdin);
	sscanf(linha, "%d", &n);
	
	fgets(linha, sizeof(linha), stdin);
	tam = 0;
	for ( j = 0 ; j < n ; j++ )
	{
	    sscanf(&linha[tam],"%d%n", &vetor1[j], &tamtemp);
	    tam+=tamtemp;
	}

	fgets(linha, sizeof(linha), stdin);
	tam = 0;
	for ( j = 0 ; j < n ; j++ )
	{
	    sscanf(&linha[tam],"%d%n", &vetor2[j], &tamtemp);
	    tam+=tamtemp;
	}

	qsort(vetor1, n, sizeof(vetor1[0]), cmpint);
	qsort(vetor2, n, sizeof(vetor2[0]), cmpint2);
	sum = 0;

	for ( j = 0 ; j < n ; j++ )
	{
	    sum += vetor1[j] * vetor2[j];
	}

	printf("Case #%d: %d\n", i+1, sum);

    }

    return 0;
}

