#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

__int64 gcd(__int64 a, __int64 b)
{
	if(b == 0)return a;
	return gcd(b, a%b);
}

int main()
{
	int cas, T;
	scanf("%d", &T);
	for(cas = 1; cas <= T; cas ++)
	{
		__int64 n, m, pd, pg;
		scanf("%I64d %I64d %I64d", &n, &pd, &pg);
		printf("Case #%d: ", cas);
		if(pg == 0 && pd != 0)puts("Broken");
		else if(pg == 100 && pd != 100)puts("Broken");
		else {
			m = 100 / gcd(pd, 100);
			if(m > n)puts("Broken");
			else puts("Possible");
		}
	}
	return 0;
}
