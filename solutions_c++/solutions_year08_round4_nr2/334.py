#include<iostream>
#include<algorithm>
#include<utility>

using namespace std;

typedef unsigned long UL;
typedef signed long SL;
typedef unsigned short US;
typedef signed short SS;

inline SL aabs(SL a)
{
	return(a>=0?a:-a);
}

typedef pair<SL, SL> point;

SL ar2(const point &a, const point &b, const point &c)
{
	return aabs(a.first*(b.second-c.second) + b.first*(c.second-a.second) + c.first*(a.second-b.second));
}

int main()
{
	UL tests;
	scanf("%lu", &tests);
	for(UL tt=1; tt<=tests; ++tt)
	{
		SL N, M, A;
		scanf("%ld %ld %ld", &N, &M, &A);
		printf("Case #%lu: ", tt);
		if(A<=M*N)
		{
			for(SL bx=0; bx<=N; ++bx)
			for(SL cx=bx+1; cx<=N; ++cx)
			for(SL by=0; by<=M; ++by)
			for(SL cy=0; cy<=M; ++cy)
				if(aabs(bx*cy - cx*by)==A)
				{
					printf("0 0 %ld %ld %ld %ld\n", bx, by, cx, cy);
					goto NEXT_TEST_CASE;
				}
		}
		printf("IMPOSSIBLE\n");
		NEXT_TEST_CASE:
		;
	}

}
