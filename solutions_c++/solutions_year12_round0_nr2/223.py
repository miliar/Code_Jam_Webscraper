#include <cassert>
#include <cstdio>
#include <iostream>
#include <algorithm>


// h[s][n] highest possible point for a 
// surprising s=[0,1] triplet with
// total score n=[0,30]
// h<=10 if valid
size_t h[2][31];


int main()
{
	for(size_t s=0; s<2; ++s)
		for(size_t n=0; n<=30; ++n)
			h[s][n]=42;
	for(size_t a=0; a<=10; ++a)
		for(size_t b=a; b<=a+2 && b<=10; ++b)
			for(size_t c=b; c<=a+2 && c<=10; ++c)
			{
				size_t n=a+b+c;
				bool s=a+1<c;
				if(10<h[s][n] || h[s][n]<c)
					h[s][n]=c;
			}

	/*printf("    ");
	for(size_t n=0; n<=30; ++n)
		printf("%02zu ", n);
	printf("\n");
	for(size_t s=0; s<2; ++s)
	{
		printf("%02zu  ", s);
		for(size_t n=0; n<=30; ++n)
			if(h[s][n]<=10)
				printf("%02zu ", h[s][n]);
			else printf("-- ");
		printf("\n");
	}*/

	size_t T=0;
	scanf("%zu\n", &T);
	for(size_t t=1; t<=T; ++t)
	{
		size_t K=0, S=0, p=0;
		size_t total[100]={};
		scanf("%zu %zu %zu", &K, &S, &p);
		size_t r=0, m=0;
		for(size_t k=0; k<K; ++k)
		{
			size_t n=0;
			scanf(" %zu", &n);

			// cannot be surprising
			if(n<2 || 28<n)
				r+= p<=h[0][n];

			// we score if these are surprising
			// we want as much of these triplets to be surprising as possible
			// so we score more
			else if(h[0][n]<p && p<=h[1][n])
				++m;

			// these will act as surprise sinks if we have some surplus

			// we score no matter what
			else if(p<=h[0][n])
				++r;
			// doesn't matter if it's surprising or not,
			// we get the same highest possible best score
			else if(h[0][n]==h[1][n])
				r+= p<=h[0][n];
			// sry noob
			else if(h[1][n]<p)
				;
		}
		r+=std::min(m, S);
		printf("Case #%zu: %zu\n", t, r); 
	}
	return 0;
}

