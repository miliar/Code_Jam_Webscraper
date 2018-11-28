#include <cstdio>
#include <string>
#include <cmath>
#include <vector>
#include <memory>
#include <algorithm>
using namespace std;
int main(void)
{
	int t,q;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (q = 1; q <= t; q++)
	{
		int n,x;
		scanf("%d",&n);
		int ans = 0;
		int sum = 0;
		int mi = 10000000;
		for (int i = 0 ; i < n; i++)
		{
			scanf("%d",&x);
			ans ^= x;
			sum += x;
			mi = min(mi,x);
		}
		printf("Case #%d: ",q);
		if (ans)
			printf("NO\n"); else
			printf("%d\n",sum-mi);
	}
	return 0;
}