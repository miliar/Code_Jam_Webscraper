#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <memory>
#include <string>
#include <set>
#include <map>
#include <queue>
using namespace std;
int main(void)
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,q;
	scanf("%d",&t);
	int n,l,h,c[105];
	for (q = 1; q <= t; q++)
	{
		scanf("%d%d%d",&n,&l,&h);
		for (int i = 0 ; i < n; i++)
			scanf("%d",&c[i]);
		bool ok;
		int i;
		for (i = l; i <= h; i++)
		{
			ok = true;
			for (int j = 0 ; j< n; j++)
			{
				if (((i % c[j]) == 0) ||((c[j] % i) == 0))
					ok &= true; else
				{
					ok = false;
					break;
				}
			}
			if (ok)
				break;
		}
		printf("Case #%d: ",q);
		if (ok)
			printf("%d\n",i); else
			printf("NO\n");
	}
	return 0;
}