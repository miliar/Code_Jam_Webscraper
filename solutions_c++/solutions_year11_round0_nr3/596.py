#include <iostream>
using namespace std;
int ci, cn, i, t, s, a[2000], n;

int main()
{
	FILE * fin = fopen( "C-large.in", "r" );
	FILE * fout = fopen( "C-large.out", "w" );
	fscanf( fin, "%d", &cn );
	for ( ci = 1; ci <= cn; ci++ )
	{
		fscanf( fin, "%d", &n );
		for ( i = 0; i < n; i++ ) fscanf( fin, "%d", &a[i] );
		sort( a, a+n );
		t = 0;
		s = 0;
		for ( i = 0; i < n; i++ ) 
		{
			t = t ^ a[i];
			s = s + a[i];
		}
		fprintf( fout, "Case #%d: ", ci );
		if ( t ) fprintf( fout, "NO\n" );
		else fprintf( fout, "%d\n", s - a[0] );
	}
	fclose( fin );
	fclose( fout );
	return 0;
}
