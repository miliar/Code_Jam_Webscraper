/* Tomasz [Tommalla] Zakrzewski, Google Code Jam 2011 /
/  Qualifications Round */
#include <cstdio>
#include <algorithm>

using namespace std;

char txt[3];

int main()
{
    char prevSgn;
    unsigned int t, n, testCase, result;
    int posO, posB, prevTime, x, tmp;

    scanf("%u", &t );
    for( testCase = 1; testCase <= t; ++testCase )
    {
	printf("Case #%u: ", testCase);
	posO = 1;
	posB = 1;
	prevTime = -1;

	scanf("%u", &n);
	scanf("%s%u",txt, &x );
	if( txt[0] == 'O' )
	{
	    posO = x;
	    posB = 1;
	}
	else
	{
	    posO = 1;
	    posB = x;
	}

	prevSgn = txt[0];
	tmp = prevTime = result = x;
	n--;


	while( n-- )
	{
	    //printf("result = %u\n", result );
	    scanf("%s%u",txt, &x );
	    
	    if( prevSgn == txt[0] )	//czy ruszamy się ciągle tym samym robotem
	    {
		if( txt[0] == 'O' )
		{
		    prevTime = abs( x-posO ) + 1;
		    posO = x;
		}
		else
		{
		    prevTime = abs( x-posB ) + 1;
		    posB = x;
		}
		tmp += prevTime;
	    }
	    else
	    {
		//printf("\tInny robot, tmp = %u\n", tmp );
		prevTime = tmp;
		tmp = 0;
		if( txt[0] == 'O' )	//poprzednio ruszaliśmy się B
		{
		    prevTime = abs(min( prevTime - abs( x-posO ), 0 )) + 1;
		    posO = x;
		}
		else
		{
		    prevTime = abs(min( prevTime - abs( x-posB ), 0 )) + 1;
		    posB = x;
		}
		
		tmp = prevTime;
	    }
	    result += prevTime;
	    prevSgn = txt[0];
	}
	printf("%u\n", result );
    }
    return 0;
}