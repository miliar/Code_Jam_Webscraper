#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int n;
int nt;

int main()
{
	scanf("%d", &nt);
	
	for(int tt = 1; tt <= nt; tt++)
	{	
		printf("Case #%d: ", tt);
		
		scanf("%d", &n);
		
		int xorsum = 0, giveaway = 1000000000, sum = 0;
		
		for(int i = 0; i < n; i++)
		{
			int x;
			scanf("%d", &x);
			xorsum ^= x;
			sum += x;
			giveaway = min(giveaway, x);
		}
		
		if (xorsum) puts("NO"); else printf("%d\n", sum - giveaway);
	}
	
	return 0;
}
