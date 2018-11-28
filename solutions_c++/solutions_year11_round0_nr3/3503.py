#include <cstdio>
using namespace std;

int main()
{
	int Z, N;
	scanf("%i", &Z);
	for(int test_case = 1; test_case <= Z; ++test_case)
	{
		scanf("%i", &N);
		
		int minim = 1000000, sum = 0, xorr = 0;
		for(int i = 0; i < N; ++i)
		{
			int a; scanf("%i", &a);
			minim = a < minim ? a : minim;
			sum += a;
			xorr ^= a;
		}
		
		if(xorr) printf("Case #%i: NO\n", test_case);
		else printf("Case #%i: %i\n", test_case, sum - minim);
	}
	return 0;
}
