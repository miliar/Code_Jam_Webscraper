#include <stdio.h>
#include <vector>
#include <map>
#include <math.h>
#include <algorithm>

using namespace std;

#define MAX 1048576
int mas[2][MAX];
int cs[1000];

int main()
{
	freopen("out.txt", "w", stdout);
	freopen("in.txt", "r", stdin);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		int N;
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
			scanf("%d", &cs[i]);
		int sum = 0, xor = 0;
		int mn = 1000000000;
		for (int i = 0; i < N; i++)
		{
			sum += cs[i];
			xor = xor ^ cs[i];
			mn = min(mn, cs[i]);
		}
		if (xor != 0)
			printf("Case #%d: NO\n", t+1);
		else
			printf("Case #%d: %d\n", t+1, sum - mn);
	}

	return 0;
}