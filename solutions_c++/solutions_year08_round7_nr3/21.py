#include <cstdio>
#include <algorithm>

double p[10][5];
double v[ 1 << 13 ];
int qtd, Q;

void go( int x, double q )
{
	if( x == Q )
	{
		v[qtd++] = q;
		return;
	}
	
	for(int i = 0; i < 4; i++)
		go( x+1, q * p[x][i] );
}

int main()
{
	int K;
	scanf("%d", &K);
	for(int k = 1; k <= K; k++)
	{
		int M;
		scanf("%d %d", &M, &Q);
		for(int i = 0; i < Q; i++)
			scanf("%lf %lf %lf %lf", &p[i][0], &p[i][1], &p[i][2], &p[i][3]);
		
		qtd = 0;
		go( 0, 1.0 );
		
		std::sort( v, v+qtd );
		double res = 0;
		for(int i = qtd-1; i >= 0 && M; i--, M--)
			res += v[i];
			
		printf("Case #%d: %.6lf\n", k, res);
	}
}