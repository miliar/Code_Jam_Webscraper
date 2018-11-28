#include <stdio.h>
#include <memory.h>
#include <stdlib.h>

typedef long long int64;

int g[1001];
int lik[1001];
int64 eru[1001];
bool vis[1001];

int main()
{
	int i,j;
	char  filename [] = "G:\\GCJ\\GCJ\\C-small-attempt0.in";
	char  output[] = "G:\\GCJ\\GCJ\\C-small.out";
	FILE * fp1, * fp2;
	int cas;
	int T, N, R, k;
	int tot_people = 0;

	fp1 = fopen( filename, "r" );
	fp2 = fopen( output, "w" );

	fscanf( fp1, "%d", &T );
	
	for ( cas = 1; cas <= T; cas++ )
	{
		tot_people = 0;
		fscanf(fp1, "%d %d %d", &R, &k, &N );
		for ( i = 0; i < N; i++ )
		{
			fscanf( fp1, "%d", &g[i] );
			tot_people += g[i];
		}
		if ( tot_people <= k )
		{
			fprintf( fp2, "Case #%d: %lld\n", cas, (int64)tot_people * R );
			continue;
		}
		for ( i = 0; i < N; i++ )
		{
			int64 val = 0;
			for ( j = i; ; j++ )
			{
				j %= N;
				val += g[j];
				if ( val > k )
				{
					val -= g[j];
					lik[i] = j;
					eru[i] = val;
					break;
				}
			}
		}

		int64 money0 = 0, money1 = 0;
		int runs0 = 0, runs1 = 0;
		int64 tot = 0;

		memset( vis, 0, sizeof( vis ) );
		money0 = eru[0];
		runs0  = 1;
		vis[0] = true;

		for ( i = lik[0]; i != 0; i = lik[i] )
		{
			if ( vis[i] )
			{
				break;
			}
			vis[i] = true;
			runs0++;
			money0 += eru[i];
		}
		for ( j = 0; R && j != i; j = lik[j] )
		{
			R--;
			tot += eru[j];
			runs0--;
			money0 -= eru[j];
		}

		tot += R / runs0 * money0;

		R %= runs0;
		while ( R )
		{
			R--;
			tot += eru[i];
			i = lik[i];
		}

		fprintf( fp2, "Case #%d: %lld\n", cas, tot );
	}

	fclose( fp1 );
	fclose( fp2 );
	return 0;
}