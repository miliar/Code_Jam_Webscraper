#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory>
#include <cstring>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <set>
#include <iostream>

using namespace std;
typedef pair <int, int> pii;
typedef pair <long long, long long> pll;
typedef long long ll;

int l[20000], d[20000];
int maxH[20000];

void test(int testNo)
{
    printf("Case #%d: ", testNo+1);
    int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		scanf("%d%d", d+i, l+i);
	}

	memset(maxH, -1, sizeof(maxH));

	int D;
	scanf("%d", &D);

	bool res = false;
	maxH[0] = min(l[0], d[0]);
	for(int i = 1; i < n; i++)
		for(int j = 0; j < i; j++)
		{
			int dd = d[i] - d[j];
			if (dd <= maxH[j])
			{
				maxH[i] = max(maxH[i], dd);
				maxH[i] = min(maxH[i], l[i]);
			}
			if (d[j] + maxH[j] >= D && maxH[j] != -1)
				res = true;
		}
	if (d[n-1] + maxH[n-1] >= D && maxH[n-1] != -1)
			res = true;
	if (res)
	{
		printf("YES\n");
	}
	else
		printf("NO\n");
}

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TC;
    scanf("%d", &TC);
    
    for (int i = 0; i < TC; i++)
        test(i);
    
    return 0;
}