#include <vector>
#include <algorithm>

#include <cstdio>

using namespace std;

#define INF 25600

int distAdd(int I, int M, int a, int b)
{
	if (a == b)
		return 0;
	else if (M == 0)
		return INF;
	else
	{
		if (a < b)
			return (b - a + M - 1) / M * I;
		else
			return (a - b + M - 1) / M * I;
	}
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int idxCase = 0; idxCase < T; ++idxCase)
    {
        int D, I, M, N;
        scanf("%d%d%d%d", &D, &I, &M, &N);
    	vector<int> a(N);
    	for (int i = 0; i < N; ++i)
	    	scanf("%d", &a[i]);
    	vector<int> cost(256, 0);
    	vector<int> prevCost(256);
    	for (int i = 0; i < N; ++i)
    	{
//printf("<%d>\n", i);
    		swap(cost, prevCost);
    		for (int last = 0; last <= 255; ++last)
    		{
    			cost[last] = prevCost[last] + D;
    			for (int k = 0; k <= 255; ++k)
    			{
	    			int da = min(D + I, max(k - a[i], a[i] - k)) + distAdd(I, M, k, last);
	    			for (int j = max(0, k - M); j <= min(255, k + M); ++j)
	    				cost[last] = min(cost[last], prevCost[j] + da);
    			}
//printf("%d: %d\n", last, cost[last]);
    		}
    	}
    	int minCost = INF;
    	for (int last = 0; last <= 255; ++last)
	    	minCost = min(minCost, cost[last]);
    	printf("Case #%d: %d\n", idxCase + 1, minCost);
    }
    return 0;
}
