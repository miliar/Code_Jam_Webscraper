#include <iostream>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("PAout.txt", "w", stdout);
	int pa, pb, a, b, maxn, i, j, t, c=1, n, ans, y;
	char x;
	cin >> t;
	while(t--)
	{
		cin >> n;
		a = b = 0;
		pa = pb = 1;
		ans = maxn = 0;
		while(n--)
		{
			cin >> x >> i;
			if(x == 'O')
				a += abs(i - pa) + 1, pa = i, y = a;
			else
				b += abs(i - pb) + 1, pb = i, y = b;
			if(y > maxn)
				ans += y - maxn;
			else
			{
				ans ++;
				if(x == 'O')
					a = maxn + 1;
				else
					b = maxn + 1;
			}
			maxn = max(a, b);
		}
		printf("Case #%d: %d\n", c++, ans);
	}
}
