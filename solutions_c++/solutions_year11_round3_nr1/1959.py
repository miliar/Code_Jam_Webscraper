#include <stdio.h>
#include <string>

using namespace std;

int tc;

int r, c;
char tile[51][51];

bool change( int i, int j ) 
{
	if ( tile[i][j] == '#' 
		&& i+1 <= r && tile[i+1][j] == '#'
		&& j+1 <= c && tile[i][j+1] == '#' && tile[i+1][j+1] == '#' ) {
			tile[i][j]='/';
			tile[i][j+1] = '\\';
			tile[i+1][j] = '\\';
			tile[i+1][j+1] = '/';

			return true;
	}

	return false;
}

int main()
{

	
	freopen("input.a.txt", "r", stdin);
	freopen("output.a.txt", "w", stdout);

	scanf("%d", &tc);

	

	for ( int t=1; t<=tc; t++ ){

		scanf("%d %d", &r, &c);

		memset(tile, 0, sizeof(tile));

		bool ok = true;

		for ( int i=0; i<r; i++ ) {
			scanf("%s", tile[i]);
		}

		for ( int i=0; i<r; i++ )
			for ( int j=0; j<c; j++ ) 
				if ( tile[i][j] == '#' && !change(i,j) ) {
					
					ok = false;
					break;
				}


		printf("Case #%d:\n", t);

		if ( ok ) {
			for ( int i=0; i<r; i++ ){
				for ( int j=0; j<c; j++) printf("%c", tile[i][j]);
				printf("\n");
			}
		}
		else {
			printf("Impossible\n");
		}

		
	
	}

	fclose(stdout);
	fclose(stdin);	

	return 0;
}