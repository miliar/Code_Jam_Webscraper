#include <algorithm>
#include <cstdio>
#include <iostream>

using namespace std;

struct vine
{
	long long position, length;
};

int main()
{
	int N;
	
	scanf("%d\n", &N);
	for(int t = 0; t < N; t++)
	{
		int A;
		scanf("%d\n", &A);
		
		struct vine X[A];
		for(int i = 0; i < A; i++)
			scanf("%lld %lld\n", &X[i].position, &X[i].length);
		
		long long D;
		scanf("%lld\n", &D);
		
		bool found = false;
		long long range[A];
		for(int i = 0; i < A; i++)
			range[i] = 0;
		range[0] = 2 * X[0].position;
		if(range[0] >= D)
			found = true;
		else for(int i = 1; i < A; i++)
		{
			for(int j = i - 1; j >= 0; j--)
				if(range[j] >= X[i].position)
				{
					long long value = X[i].position + min(X[i].position - X[j].position, X[i].length);
					if(value > range[i])
						range[i] = value;
					if(value >= D)
						found = true;
				}
			if(found)
				break;
		}
					
		printf("Case #%d: %s\n", t + 1, found ? "YES" : "NO");
	}
	
	return 0;
}
