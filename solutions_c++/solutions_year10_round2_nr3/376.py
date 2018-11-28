#include <iostream>
#include <string>
#include <string.h>
using namespace std;

typedef long long LL;

int d[512][512];

int Cnt(int n, int k)
{
	if(n < 1 || k < 1)
		return 1;
	LL res = 1;
	int nL = max(k, n - k);
	for(int i = nL + 1; i <= n; i++)
		res *= (LL)i;
	for(int i = 2; i <= min(k, n - k); i++)
		res /= (LL)i;
	return res % 100003;
}

int D(int p, int n)
{
	if(p == 1)
		return 1;
	if(d[n][p] == -1)
	{
		d[n][p] = 0;
		for(int i = 1; i < p; i++)
		{
			if(i <= p - 1 && p - i <= n - p)
			{
				d[n][p] = (d[n][p] + (D(i, p) * Cnt(n - p - 1, p - i - 1)) % 100003) % 100003;
			}
		}
	}
	return d[n][p];
}

void Solve()
{
	int n;
	cin >> n;
	memset(d, -1, sizeof(d));
	int cnt = 0;
	for(int p = 1; p < n; p++)
	{
		cnt = (cnt + D(p, n)) % 100003;
	}
	cout << cnt << endl;
}

int main()
{
	freopen("d:\\input.in", "r", stdin);
	freopen("d:\\output.out", "w", stdout);
	int T;
	cin >> T;
	for(int tt = 1; tt <= T; tt++)
	{
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}