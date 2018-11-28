#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstdlib>

using namespace std;

int main()
{
	int T, K, N;
	
	scanf("%d", &T);
	
	for (int test=1; test<=T; test++)
	{
		scanf("%d%d", &N, &K);
		
		int Power = 2;
		for (int i=1; i<N; i++)
			Power *= 2;
			
		if ( K%Power == Power-1)
			printf("Case #%d: ON\n", test);
		else printf("Case #%d: OFF\n", test);
	}
	
	return 0;
}
