#include <iostream>
using namespace std;

int a[200];
int b[200];
int p[2], t[2];
int cn, ci, i, cur, n, ans;
char s[20];

int main()
{
	FILE * fin = fopen( "A-large.in", "r" );
	FILE * fout = fopen( "A-large.out", "w" );
	
	fscanf( fin, "%d", &cn );
	for ( ci = 1; ci <= cn; ci++ )
	{
		fscanf( fin, "%d", &n );
		for ( i = 0; i < n; i++ )
		{
			fscanf( fin, "%s", &s );
			if ( s[0] == 'O' ) a[i] = 0;
			else a[i] = 1;
			fscanf( fin, "%d", &b[i] );
		}
		t[0] = 0;
		t[1] = 0;
		p[0] = 1;
		p[1] = 1;
		cur = 0;
		ans = 0;
		for ( i = 0; i < n; i++ )
		{
			cur = abs(b[i]-p[a[i]])+1+t[a[i]];
			p[a[i]] = b[i];
			if ( cur <= t[1-a[i]] ) cur = t[1-a[i]]+1;
			t[a[i]] = cur;
		}
		fprintf( fout, "Case #%d: %d\n", ci, cur );
	}
	fclose( fin );
	fclose( fout );
	return 0;
}
