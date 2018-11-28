#include "stdlib.h"
#include <algorithm>
#include "stdio.h"
using namespace std;

int T, N;

void solve(int t)
{
	int nim(0);
	int sum(0);
	int smallest(1<<20);
	int candy;

	scanf("%d\n",&N);
	for (int i=0; i<N; i++)
	{
		scanf("%d",&candy);
		nim ^= candy;
		sum += candy;
		smallest = min(smallest, candy);
	}
	
	printf("Case #%d: ",t);
	nim ? printf("NO\n") : printf("%d\n",sum-smallest);
}

int main()
{
	scanf("%d\n",&T);
	for (int i=0; i<T; i++)
		solve(i+1);
	return 0;
}
