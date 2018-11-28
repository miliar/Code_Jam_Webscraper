#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
#define INF 1000000000
#define EPS 1e-6
typedef long long ll;




ll primes[1000010], cnt;
ll slove(ll n)
{
	if (n == 0) return 0;
	if (n == 1) return 0;
	if (n == 2) return 1;
	ll res = 1;
	for (int i = 0; i < cnt && primes[i] * primes[i] <= n; i++)
	{
		ll cc = n;
		cc /= primes[i];
		while (cc >= primes[i])
		{
			res++;
			cc /= primes[i];
		}
	}
	return res;
}
void _main()
{
	ll N;
	scanf("%lld", &N);
	printf("%lld\n", slove(N));
}
int main()
{
	for (int i = 2; i <= 1000000; i++)
	{
		if (primes[i]) continue;
		primes[cnt++] = i;
		for (int j = i + i; j <= 1000000; j += i) primes[j] = 1;
	}
	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++)
	{
		printf("Case #%d: ", cases);
		_main();
	}
}