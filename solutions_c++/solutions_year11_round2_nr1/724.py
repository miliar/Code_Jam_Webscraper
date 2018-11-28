#include <string.h>
#include <stdio.h>

char res[100][104];
int win[100];
int tot[100];
double wp[100];
double owp[100];
double oowp[100];

int main()
{
	freopen( "A.in", "r", stdin );
	freopen( "A.out", "w", stdout );

	int t, i;
	int n, j, k;

	for( scanf( "%d", &t ), i = 1; i <= t; ++i )
		{
		for( scanf( "%d", &n ), j = 0; j < n; ++j )
			{
			scanf( "%s", res[j] );
			}//end for
		memset( win, 0, sizeof( win[0] ) * n );
		memset( tot, 0, sizeof( tot[0] ) * n );
		for( j = 0; j < n; ++j )
			{
			for( k = j + 1; k < n; ++k )
				{
				if( res[j][k] == '1' )
					{
					++tot[j];
					++tot[k];
					++win[j];
					}
				else if( res[j][k] == '0' )
					{
					++tot[j];
					++tot[k];
					++win[k];
					}//end if
				}//end for
			}//end for
		for( j = 0; j < n; ++j )
			{
			wp[j] = ((double)win[j]) / tot[j];
			}//end for
		for( j = 0; j < n; ++j )
			{
			owp[j] = 0.0;
			for( k = 0; k < n; ++k )
				{
				if( res[j][k] == '1' )
					{
					owp[j] += ((double)win[k]) / (tot[k] - 1);
					}
				else if( res[j][k] == '0' )
					{
					owp[j] += ((double)win[k] - 1) / (tot[k] - 1);
					}//end if
				}//end for
			owp[j] /= tot[j];
			}//end for
		for( j = 0; j < n; ++j )
			{
			oowp[j] = 0.0;
			for( k = 0; k < n; ++k )
				{
				if( res[j][k] != '.' )
					{
					oowp[j] += owp[k];
					}//end if
				}//end for
			oowp[j] /= tot[j];
			}//end for

		printf( "Case #%d:\n", i );
		for( j = 0; j < n; ++j )
			{
			printf( "%.08lf\n", 0.25 * wp[j] + 0.50 * owp[j] + 0.25 * oowp[j] );
			}//end for
		}//end for

	return 0;
}
