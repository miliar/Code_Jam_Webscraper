// snapper.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "math.h"

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("A-large.in","r",stdin); 
	freopen("A_out.out","w",stdout);
	int testcases;
	scanf("%d", &testcases);

	for (int i=1; i<= testcases; i++) {

        int N, K;
        scanf("%d", &N);
		scanf("%d", &K);

		long x;
		x = K +1;
		long y = (long) pow(2.0,N);
		
		double state = x % y;

		if (state == 0) {
			printf("Case #%d: ON\n", i);
		}
		else {
			printf("Case #%d: OFF\n", i);
		}

	}

	return 0;
}

