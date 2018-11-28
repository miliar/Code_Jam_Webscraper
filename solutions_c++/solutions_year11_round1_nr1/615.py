#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#ifdef WIN32
#define I64 "%I64d"
#else
#define I64 "%lld"
#endif

typedef long long ll;

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	int tt;
	scanf("%d", &tt);
	for (int t = 0; t < tt; ++t)
	{
		ll n, pd, pg;
		scanf(I64""I64""I64, &n, &pd, &pg);
		bool ok = 1;
		
		bool ok2 = 0;
		
		ll k = n;
		if (n > 100) k = 100;
		
		for (int i = 1; i <= k && !ok2; ++i)
			if (i * pd % 100 == 0) ok2 = 1;
			
		ok = ok2;
		
		if (pd != 0 && pg == 0
		 || pd != 100 && pg == 100)
		 	ok = 0;
		
		printf("Case #%d: ", t + 1);
		if (!ok)
		 	printf("Broken\n");
		else
			printf("Possible\n");
	}
	return 0;
}
