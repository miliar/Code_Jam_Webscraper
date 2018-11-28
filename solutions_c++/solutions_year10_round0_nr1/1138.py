#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int tt, n, k;

int main()
{
//	freopen("input","r",stdin);
//	freopen("output","w",stdout);
	scanf("%d", &tt);
	for (int t = 0; t < tt; ++t)
	{
		scanf("%d%d", &n, &k);
		int z = (1<<n);
		k %= z;
		printf("Case #%d: ", t+1);
		if (z-1==k) printf("ON");
		else printf("OFF");
		printf("\n");
	}
	return 0;
}
