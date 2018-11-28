#include <iostream>
using namespace std;

int ci, cn, i, j, k;
char s[210];
int u[110], v[110], a[110][110];
double wp[110], owp[110], oowp[110];
int n;
double rpi[110];

int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );
	scanf( "%d", &cn );
	for ( ci = 1; ci <= cn; ci++ )
	{
		scanf( "%d", &n );
		for ( i = 0; i < n; i++ )
		{
			u[i] = 0;
			v[i] = 0;
		}
		for ( i = 0; i < n; i++ )
		{
			scanf( "%s", &s );
			for ( j = 0; j < n; j++ )
				if ( s[j] == '0' )
				{
					a[i][j] = -1;
					v[i]++;
				}
				else if ( s[j] == '1' )
				{
					a[i][j] = 1;
					u[i]++;
				}
				else a[i][j] = 0;
			wp[i] = double(u[i])/double(u[i]+v[i]);
		}
		for ( i = 0; i < n; i++ )
		{
			k = 0;
			owp[i] = 0;
			for ( j = 0; j < n; j++ )
				if ( a[i][j] != 0 )
				{
					k++;
					if ( a[j][i] == 1 ) owp[i] += double(u[j]-a[j][i])/double(u[j]+v[j]-1);
					else owp[i] += double(u[j])/double(u[j]+v[j]-1);
				}
			owp[i] /= k;
		}
		for ( i = 0; i < n; i++ )
		{
			k = 0;
			oowp[i] = 0;
			for ( j = 0; j < n; j++ )
				if ( a[i][j] != 0 )
				{
					k++;
					oowp[i] += owp[j];
				}
			oowp[i] /= k;
		}
		for ( i = 0; i < n; i++ ) rpi[i] = 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
		printf( "Case #%d:\n", ci );
		for ( i = 0; i < n; i++ ) printf( "%.8lf\n", rpi[i] );
	}
}