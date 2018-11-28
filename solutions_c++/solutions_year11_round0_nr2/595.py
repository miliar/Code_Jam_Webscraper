#include <iostream>
using namespace std;
int ci, cn, n, m, i, j;
int a[26][26], b[26][26];
int ans[2000];
char s[2000];

int main()
{
	FILE * fin = fopen( "B-large.in", "r" );
	FILE * fout = fopen( "B-large.out", "w" );
	fscanf( fin, "%d", &cn );
	for ( ci = 1; ci <= cn; ci++ )
	{
		for ( i = 0; i < 26; i++ )
		for ( j = 0; j < 26; j++ ) 
		{
			a[i][j] = -1;
			b[i][j] = 0;
		}
		
		fscanf( fin, "%d", &m );
		for ( i = 0; i < m; i++ ) 
		{
			fscanf( fin, "%s", &s );
			a[s[0]-'A'][s[1]-'A'] = s[2]-'A';
			a[s[1]-'A'][s[0]-'A'] = s[2]-'A';
		}
		fscanf( fin, "%d", &m );
		for ( i = 0; i < m; i++ ) 
		{
			fscanf( fin, "%s", &s );
			b[s[0]-'A'][s[1]-'A'] = 1;
			b[s[1]-'A'][s[0]-'A'] = 1;
		}
		m = 0;
		fscanf( fin, "%d%s", &n, &s );
		for ( i = 0; i < n; i++ ) 
		{
			ans[m] = s[i]-'A';
			while ( m > 0 && a[ans[m-1]][ans[m]] >= 0 )
			{
				ans[m-1] = a[ans[m-1]][ans[m]];
				m--;
			}		
			for ( j = 0; j < m; j++ )
			if ( b[ans[j]][ans[m]] )
			{
				m = -1;
				break;
			}	
			if ( m == -1 ) m = 0;
			else m++;
		}
		fprintf( fout, "Case #%d: [", ci );
		for ( i = 0; i < m; i++ )
		{
			if ( i > 0 ) fprintf( fout, ", " );
			fprintf( fout, "%c", 'A'+ans[i] );
		}
		fprintf( fout, "]\n" );
	}
	fclose( fin );
	fclose( fout );
	return 0;
}
