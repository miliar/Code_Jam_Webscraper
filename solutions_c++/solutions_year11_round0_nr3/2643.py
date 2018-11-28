#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int i, j, k, x, sum;
	int ca, T, n;

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	scanf("%d",&T);
	for(ca = 1; ca <= T; ca ++)
	{
		scanf("%d",&n);
		k = 10000010;
		j = 0; sum = 0;
		for(i=1;i<=n;i++){
			scanf("%d",&x);
			j ^= x;
			sum += x;
			k = min(k, x);
		}
		printf("Case #%d: ", ca);
		if(j != 0) printf("NO\n");
		else printf("%d\n", sum - k);
	}
	return 0;
}
			
