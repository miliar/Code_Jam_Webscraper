#include <cassert>
#include <cstdio>
#include <vector>
#include <iostream>


int main()
{
	size_t T=0;
	scanf("%zu\n", &T);
	for(size_t t=1; t<=T; ++t)
	{
		size_t A=0, B=0;
		scanf("%zu %zu", &A, &B);

		// k: number of digits in B
		size_t k=0;
		for(size_t q=B; 0<q; q/=10)
			++k;

		// h=10^(k-1), highest digit's multiplier
		size_t h=1;
		for(size_t i=1; i<k; ++i)
			h*=10;
		// h=10^(k-1) <= A <= B < 10^k=10*h
		assert(h<=A && A<=B && B<10*h);
	
		size_t r=0;
		std::vector<size_t> got(B+1, 0);
		for(size_t n=A; n<B; ++n)
		{
			size_t m=n;
			// last digit moved to front, doing this k-1 times
			for(size_t i=1; i<k; ++i)
			{
				assert(m/10<h);
				// rotating right 1 digit
				m= m%10*h +m/10;
				// oyea
				if(n<m && m<=B && got[m]!=n)
				{
					r+=1;
					got[m]=n;
				}
			}
		}
		printf("Case #%zu: %zu\n", t, r); 
	}
	return 0;
}

