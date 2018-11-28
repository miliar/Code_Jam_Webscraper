#include <iostream>
#include <cmath>

using namespace std;

long t;
long n;
long g[1001];
long tot;
long ans;

long gcd(long a, long b)
{
	if(b == 0) return a;
	else return gcd(b, a % b);
}

void work()
{
	for(int i = 1; i <= t; i++)
	{
		scanf("%ld", &n);
		for(int j = 1; j <= n; j++)
			scanf("%ld", &g[j]);
		tot = abs(g[2] - g[1]);
		for(int j = 2; j < n; j++)
			tot = gcd(tot, abs(g[j] - g[j + 1]));
		ans = ((g[1] / tot) * tot) - g[1];
		if(ans)
            ans = ((g[1] / tot + 1) * tot) - g[1];
		printf("Case #%d: %ld\n",i , ans);
	}
}

int main()
{
	freopen("2.in", "r", stdin);
	freopen("2.out", "w", stdout);
	scanf("%ld", &t);
	work();
	return 0;
}
