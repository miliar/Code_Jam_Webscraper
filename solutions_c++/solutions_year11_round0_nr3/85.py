/* Tomasz [Tommalla] Zakrzewski, Google Code Jam 2011 /
/  Qualification Round, Task "Candy Splitting" */
#include <cstdio>

int main()
{
    unsigned int t, test, n, c, sum, min, x;

    scanf("%u", &t );
    for( test = 1; test <= t; ++test )
    {
	printf("Case #%u: ", test );
	scanf("%u", &n );
	x = sum = 0;
	min = 99999999;
	while( n-- )
	{
	    scanf("%u", &c );
	    sum+=c;
	    x^=c;
	    min = (min > c)? c : min;
	}

	if( x )
	    puts("NO");
	else
	    printf("%u\n", sum - min );
    }
    return 0;
}