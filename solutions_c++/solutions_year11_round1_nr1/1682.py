#include <stdio.h>

bool isPossible(int N, int pD, int pG)
{
    if((pG == 100 && pD != 100) || (pG == 0 && pD > 0))
    {
	return false;
    }

    if( pG == pD )
	return true;
    

    for(int D = 1; D <= N; D++)
    {
	// if % is round
	if((D * pD) % 100 == 0)
	{
	    int winD = D*pD/100;
	    int A = 0;
	    int wApluswD100 = pG*(D+A);

	    while( A <= 100000)
	    {
		if(wApluswD100 % 100 == 0)
		    return true;

		
		A++;

		wApluswD100 = pG*(D+A);
	    }
		    
		
	}
    }

    return false;
}


int main()
{
    int T;
    int N, pD, pG;
    bool possible;

    scanf("%d", &T);

    for(int test = 1; test <= T; test++)
    {
	scanf("%d%d%d", &N, &pD, &pG);
	
	if(isPossible(N, pD, pG))
	{
	    printf("Case #%d: Possible\n", test);
	}
	else
	{
	    printf("Case #%d: Broken\n", test);
	}
    }

    return 0;
}
