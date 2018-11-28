/* Tomasz [Tommalla] Zakrzewski, Google Code Jam 2011 /
/  Qualification Round, Task "Goro sort" */
#include <cstdio>
#include <algorithm>

#define SIZE 1000

using namespace std;

unsigned int tab[SIZE], cp[SIZE];

int main()
{
    unsigned int t, test, n, i;
    double res;

    scanf("%u", &t );
    for( test = 1; test <= t; ++test )
    {
	printf("Case #%u: ", test );
	scanf("%u", &n);
	for( i = 0; i < n; ++i )
	{
	    scanf("%u", &tab[i]);
	    cp[i] = tab[i];
	}

	sort( cp, cp+n );

	res = n;
	for( i = 0; i < n; ++i )
	    if( tab[i] == cp[i] )
		--res;
	printf("%lf\n", res );
    }
    return 0;
}