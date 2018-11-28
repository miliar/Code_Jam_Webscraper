#include<iostream>
using namespace std;

const int maxn = 3;
int n;
int a[maxn];
long long ans;
int ret;

long long gcd(long long x, long long y)
{
	return y == 0 ? x : gcd(y, x % y);
}

long long lcm(long long x, long long y)
{
	long long d = gcd(x, y);
	return x / d * y;
}

void check(int val)
{
	int tval = a[0] % val;
	for (int i = 0; i < n; i++)
		if (a[i] % val != tval)
			return;
	if (val > ans)
	{
		ans = val;
		ret = tval == 0 ? 0: val - tval;
	}
}

int main()
{
	freopen("B-small.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		scanf("%d", &n);
		for (int i = 0; i < n; i++) scanf("%d", &a[i]);
		int cur = 0;
		for (int i = 0; i < n; i++)
			for (int j = i + 1; j < n; j++)
				if (a[i] > a[j])
					cur = gcd(cur, a[i] - a[j]);
				else cur = gcd(a[j] - a[i], cur);
		/*if (cur == 1) { cout << 0 << endl; continue; }
		long long ans = 1;
		for (int i = 0; i < n; i++)
			ans = lcm(ans, cur - a[i] % cur);
		cout << ans << endl;
		*/
		//cout << cur << endl;
		ret = 0;ans = 1;
		for (int i = 1; i * i <= cur; i++)
		{
			if (cur % i > 0) continue;
			check(i);
			check(cur / i);
		}
		cout << ret << endl;
	}
}