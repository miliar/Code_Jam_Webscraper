
// (c) Alvaro Salmador 2010

#include <stdio.h>
#include <stdlib.h>

int K=0, N=0;

bool get_input()
{
	static int T = -1;
	
	if (T<0)
		scanf("%d", &T);
	
	if (T>0)
	{
		--T;
		if (scanf("%d %d", &N, &K)==2)
			return true;
		else
			return false;
	}
	else
		return false;
}


int main()
{
	int ncase = 0;
	while(get_input())
	{
		++ncase;

		printf(	"Case #%d: %s\n", 
				ncase, 
				((K+1)%(1<<N)==0) ? "ON" : "OFF");

		// if and only if K+1 is a multiple of 2^N, the light bulb is ON
	}

	return 0;
}