#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <iostream>
#include <sstream>
#include <queue>
#include <cstring>
#include <ctime>
#include <cfloat>

using namespace std;

#define SZ 1005

__int64 gcd(__int64 a, __int64 b)
{
	if(b == 0)
		return a;
	return(gcd(b, a % b));
}
int main()
{
	//freopen("A-small-attempt2.in", "rt", stdin);
	//freopen("A-small.out", "wt", stdout);

	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	__int64 inp, tmp, r, kase, n, k, i, j, pg, pd;
	char ch;
	scanf("%I64d", &inp);
	
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%I64d %I64d %I64d", &n, &pd, &pg);
		printf("Case #%d: ", kase);
		if(pg == 0 && pd != 0)
		{
			printf("Broken\n");
			continue;
		}
		if(pg == 100 && pd != 100)
		{
			printf("Broken\n");
			continue;
		}
		
		__int64 gc = gcd(pd, 100);
		k = 100 / gc;
		if(k <= n)
			printf("Possible\n");
		else
			printf("Broken\n");

		
	}
	return 0;
}

