#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int nt;
__int64 n;

int prime[1000001];

/*bool isPrime(__int64 x)
{
	if (x == 2) return true;
	if (x % 2 == 0) return false;
	for(int i = 3; i * i <= x; i++) if (x % i == 0) return false;
	return true;
}*/

__int64 calc(__int64 p)
{
	int cnt = 0;
	__int64 cur = 1;
	while(cur * p <= n)
	{
		cur *= p;
		cnt++;
	}
	
	return cnt - 1;
}

int main()
{
	prime[2] = 1;
	for(__int64 i = 3; i <= 1000000; i += 2)
	if (prime[i] != -1)
	{
		prime[i] = 1;
		__int64 k = i * i;
		while(k <= 1000000)
		{
			prime[k] = -1;
			k += i;
		}		
	}

	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);
		
		scanf("%I64d", &n);
		
		if (n == 1)
		{
			puts("0");
			continue;
		}
		
		__int64 res = calc(2);		
		__int64 p = 3;
		
		while(p * p <= n)
		{
			if (prime[p] == 1) res += calc(p);
			p += 2;
		}
		
		printf("%I64d\n", res + 1);
	}
	
	return 0;
}