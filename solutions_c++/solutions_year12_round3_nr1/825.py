#include <cassert>
#include <cstdio>
#include <iostream>


size_t const A=1000;
size_t N=0;
bool adj[A][A];
bool visited[A];


bool travel(size_t n)
{
	if(!visited[n])
	{
		visited[n]=1;
		for(size_t i=0; i<N; ++i)
			if(adj[n][i])
			{
				if(visited[i] || travel(i))
					return true;
			}
	}
	return false;
}


int main()
{
	size_t T=0;
	scanf("%zu\n", &T);
	for(size_t t=1; t<=T; ++t)
	{
		bool r=0;
		scanf("%zu\n", &N);
		assert(N<=A);
		for(size_t i=0; i<N; ++i)
			for(size_t j=0; j<N; ++j)
				adj[i][j]=0;
		for(size_t n=0; n<N; ++n)
		{
			size_t k=0;
			scanf("%zu", &k);
			for(size_t i=0; i<k; ++i)
			{
				size_t b=0;
				scanf("%zu", &b);
				assert(b!=0);
				adj[n][b-1]=1;
			}
		}
		for(size_t n=0; !r && n<N; ++n)
		{
			for(size_t i=0; i<N; ++i)
				visited[i]=0;
			r+=travel(n);
		}
		printf("Case #%zu: %s\n", t, (r?"Yes":"No")); 
	}
	return 0;
}


/* e3500 3.0G, i686, g++ 4.6.2

8) g++ -O6 a.cc
8) ./a.out < test.in
Case #1: No
Case #2: Yes
Case #3: Yes
8) time ./a.out < A-small-attempt1.in > A-small-attempt1.out
./a.out < A-small-attempt1.in > A-small-attempt1.out  0.00s user 0.00s system 0% cpu 0.003 total
8)
8) time ./a.out < A-large.in > A-large.out
./a.out < A-large.in > A-large.out  1.90s user 0.00s system 99% cpu 1.905 total
8)
*/
