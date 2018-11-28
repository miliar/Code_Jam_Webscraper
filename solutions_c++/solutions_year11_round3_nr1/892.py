/* Tomasz [Tommalla] Zakrzewski, Google Code Jam 2011 /
/  Round 1C, Problem A */
#include <cstdio>

#define SIZE 70
#define INF 9999999

char matrix[SIZE][SIZE];
unsigned int r, c;

inline bool redify( const unsigned int i, const unsigned int j )
{
    if( i+1 >= r || j+1 >= c )
	return false;
    if( matrix[i][j] == '.' || matrix[i+1][j] == '.' || matrix[i+1][j+1] == '.' || matrix[i][j+1] == '.' )
	return false;
    
    matrix[i][j] = matrix[i+1][j+1] = '/';
    matrix[i+1][j] = matrix[i][j+1] = '\\';
    return true;
}

int main()
{
    unsigned int t, testId, i,j;
    scanf("%u", &t );

    for(testId = 1; testId <= t; ++testId )
    {
	printf("Case #%u:\n", testId );
	scanf("%u%u", &r, &c );
	
	for( i = 0; i < r; ++i )
	    scanf("%s", matrix[i] );
	
	for( i = 0; i < r; ++i )
	    for( j = 0; j < c; ++j )
		if( matrix[i][j] == '#' )
		    if( ! redify(i,j) )
		    {
			i = INF-1;
			break;
		    }
		    
	if( i == INF )
	    puts("Impossible");
	else
	    for( i = 0; i < r; ++i )
		printf("%s\n", matrix[i]);
    }
    return 0;
}