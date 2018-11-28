#include <cstdio>

int main()
{
	long long t, k, n, r, co = 0;
	scanf( "%lld", &t );
	while( t-- > 0 )
	{
		scanf( "%lld%lld%lld", &r, &k, &n );
		/*
		 * r -> veces que se usa
		 * k -> capacidad cada vez
		 * n -> numero de grupos
		 */
		long long G[n];
		for( int i = 0; i < n; ++i )
			scanf( "%lld", &G[i] ); /* tamano de cada grupo */
		/*
		 * el tamano de cada grupo es maximo 1000
		 * calcular para cada i de n como si fuera el primero en la cola
		 * la cantidad de personas que suben y el nuevo indice del frente
		 */
		long long M[n][2], total = 0; /* tamano,nuevo indice */
		for( long long i = 0; i < n; ++i )
		{
			M[i][0] = M[i][1] = 0;
			for( long long j = i; M[i][0] <= k; )
			{
				if( M[i][0] + G[j] > k )
					break;
				M[i][0] += G[j];
				++j;
				if( j >= n )
					j = 0;
				M[i][1] = j;
				if( j == i )
					break; /* no repetir */
			}
		}
		/*
		 * Hacer los calculos con el arreglo precalculado
		 */
		for( long long i = 0, ix = 0; i < r; ++i )
		{
			total += M[ix][0];
			ix = M[ix][1];
		}
		printf( "Case #%lld: %lld\n", ++co, total );
	}
	return 0;
}

