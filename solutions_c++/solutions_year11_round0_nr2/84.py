/* Tomasz [Tommalla] Zakrzewski, Google Code Jam 2011 /
/  Qualification Round */
#include <cstdio>
#include <algorithm>

using namespace std;

char combine[256][256];
bool oppose[256][256];
unsigned int present[256];
char txt[110];
char result[110];

int main()
{
    unsigned int t, test, c, n, i, size;
    char a, b;
    scanf("%u", &t );

    for( test = 1; test <= t; ++test )
    {
	printf("Case #%u: ", test );

	for( i = 'A'; i <= 'Z'; ++i )
	{
	    fill( combine[i]+'A', combine[i]+ 'Z' +1, NULL );
	    fill( oppose[i]+'A', oppose[i]+'Z'+1, false );
	}

	fill( present + 'A', present + 'Z'+1, 0);

	scanf("%u", &c );
	while( c-- )
	{
	    scanf("%s", txt );
	    combine[txt[0]][txt[1]] = combine[txt[1]][txt[0]] = txt[2];
	}

	scanf("%u", &c );
	while( c-- )
	{
	    scanf("%s", txt );
	    oppose[txt[0]][txt[1]] = oppose[txt[1]][txt[0]] = true;
	}

	scanf("%u%s", &n, txt );

	result[0] = txt[0];
	present[txt[0]]++;
	size = 1;

	for( i = 1; i < n; ++i )
	{
	    result[size++] = txt[i];
	    present[txt[i]]++;
	    while( size >= 2 && combine[result[size-2]][result[size-1]] != NULL )
	    {
		present[result[size-2]]--;
		present[result[size-1]]--;
		result[size - 2] = combine[result[size-2]][result[size-1]];
		--size;
	    }

	    for( a = 'A'; a <= 'Z'; ++a )
		for( b = 'A'; b <= 'Z'; ++b )
		    if( oppose[a][b] && present[a] && present[b] )
		    {
			size = 0;
			fill( present+'A', present+'Z'+1, 0 );
			a = 'Z'+1;
			break;
		    }
	}

	printf("[");
	for( i = 0; i+1 < size; ++i )
	    printf("%c, ", result[i]);
	if( size )
	    printf("%c", result[size-1]);
	puts("]");
    }
    return 0;
}