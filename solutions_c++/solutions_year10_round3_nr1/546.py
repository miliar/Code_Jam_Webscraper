#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;
int l[1100], r[1110];
int main()
{
	int i, j, k, t, n, m, temp, cas = 0, count;
//	freopen("A-small.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	while(t--)
	{
		count = 0;
		scanf("%d", &n);
		for(i = 0; i < n; i ++)
			scanf("%d %d",&l[i], &r[i]);
		for(i = 0; i < n; i ++)
		{
			for(j = i + 1; j < n; j ++)
			{
				if((l[i] <= l[j] && r[i] <= r[j])|| (l[i] >= l[j] && r[i] >= r[j]))
					continue;
				else count ++;
			}
		}
		printf("Case #%d: %d\n", ++cas, count );
	}
}