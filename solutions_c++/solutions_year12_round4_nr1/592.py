#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <cstring>
#include <set>
#include <climits>

using namespace std;

#define LL long long
#define mp make_pair
#define F first
#define S second

LL vine[10001][2];
LL res[10001];

int main()
{
	int t, n;
	LL d;
	scanf("%d", &t);
	
	for (int q = 1; q<= t; ++q)
	{
		printf("Case #%d: ", q);
		scanf("%d", &n);
		for (int i = 0 ; i< n; ++i)
			scanf("%lld%lld", &vine[i][0], &vine[i][1]);
		scanf("%lld", &d);
		vine[n][0] = d;
		vine[n][1] = INT_MAX;
		++n;
		memset(res, -1, sizeof res);
		res[0] = vine[0][0];
		
		for (int i = 0; i < n-1; ++i)
		{
			if (res[i] == -1) continue;
			for (int j = i+1; j < n; ++j)
			{
				if (vine[j][0]-vine[i][0] <= res[i])
					res[j] = max(res[j], min(vine[j][1], vine[j][0]-vine[i][0]));
			}
		}
		
		if (res[n-1] == -1) printf("NO\n");
		else printf("YES\n");
	}
	
	return 0;
}

