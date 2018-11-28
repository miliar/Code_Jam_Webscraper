#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

long long a[1000];
long long b[100];
long long c[1000];

const long long mod = 1000000007;

int main()
{
	int N;
	scanf("%d", &N);
	for (int yy = 0; yy < N; yy++)
	{
		long long n, m, x, y, z;
		cin >> n >> m >> x >> y >> z;
		for (int i = 0; i < m; i++)
			cin >> b[i];
		long long ans = 0;
		c[0] = 1;
		for (int i = 0; i < n; i++)
		{
			a[i] = b[i % m];
			b[i % m] = (x * b[i % m] + y * (i + 1)) % z;
			if (i > 0)
			{
				c[i] = 1;
				for (int j = 0; j < i; j++)
					if (a[j] < a[i])
					{
						c[i] += c[j];
						c[i] %= mod;
					}
			}
			ans += c[i];
			ans %= mod;
		}
		printf("Case #%d: ", yy + 1);
		cout << ans << endl;
	}
	return 0;
}
