/* Tomasz [Tommalla] Zakrzewski, Google Code Jam 2011 /
/  Round 1C, Problem C */
#include <cstdio>

#define SIZE 110

unsigned int tab[SIZE];

int main()
{
    unsigned int t, testId, n, l, h, i, j;
    scanf("%u", &t );

    for( testId = 1; testId <= t; ++testId )
    {
	printf("Case #%u: ", testId );
	scanf("%u%u%u", &n, &l, &h );
	
	for( i = 0; i < n; ++i )
	    scanf("%u", &tab[i]);
	
	for( ; l <= h; ++l )
	{
	    for( i = 0; i < n; ++i )
		if( l%tab[i] && tab[i]%l )
		    break;
		
	
	    if( i == n )
	    {
		printf("%u\n", l);
		break;
	    }
	}
	
	if( l == h+1 )
	    puts("NO");
    }
    return 0;
}
