
// (c) Alvaro Salmador 2010

#include <stdio.h>
#include <stdlib.h>

int R=0, k=0, N=0;
int group[1000];

bool get_input()
{
	static int T = -1;
	
	if (T<0)
		scanf("%d", &T);
	
	if (T>0)
	{
		--T;

		if (scanf("%d %d %d", &R, &k, &N)!=3)
			return false;

		int i;
		for(i=0; i<N; ++i)
		{
			if (scanf("%d", &group[i])!=1) 
				return false;
		}
		group[i] = 0;

		return true;
	}
	else
		return false;
}


int main()
{
	for(int ncase=1; get_input(); ++ncase)
	{
		printf("Case #%d: ", ncase);

		int dough=0, offset=0;

		for(int j=0; j<R; ++j)
		{
			int i,accum=0;
			for(i=0; i<N; ++i)
			{
				if (accum+group[(offset+i)%N] > k)
					break;
				else
					accum += group[(offset+i)%N];
			}
			offset = (offset+i)%N;
			dough += accum;				
		}

		printf("%d\n", dough);
	}

	return 0;
}