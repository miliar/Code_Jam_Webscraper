#include <iostream>
using namespace std;
int i, j, k, n, ci, cn;
int a[1010], b[1010];
double ans;

int main()
{
	FILE * fin = fopen( "D-large.in", "r" );
	FILE * fout = fopen( "D-large.out", "w" );
	fscanf( fin, "%d", &cn );
	for ( ci = 1; ci <= cn; ci++ )
	{
		fscanf( fin, "%d", &n );
		for ( i = 0; i < n; i++ ) 
		{
			fscanf( fin, "%d", &a[i] );
			a[i]--;
			b[i] = 0;
		}
		ans = 0.0;
		for ( i = 0; i < n; i++ )
		if ( b[i] == 0 )
		{
			k = 1;
			j = a[i];
			b[i] = 1;
			while ( j != i )
			{
				k++;
				b[j] = 1;
				j = a[j];
			}
			if ( k > 1 ) ans += k;
		}
		fprintf( fout, "Case #%d: %.6lf\n", ci, ans );

	}
	fclose( fin );
	fclose( fout );	
	return 0;
}
