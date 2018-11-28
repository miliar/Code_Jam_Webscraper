#include <iostream>
#include <map>

using namespace std;

map <int, bool> m[1001];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("PCOUT.txt", "w", stdout);
	int t, n, c=1, i, sum, fsum, minn, a;
	cin >> t;
	while(t--)
	{
		cin >> n;
		minn = 1000001;
		sum = fsum = 0;
		for(i=1; i<=n; i++)
		{
			cin >> a;
			sum += a;
			fsum ^= a;
			minn = min(minn, a);
		}
		if(fsum)
			printf("Case #%d: NO\n", c++);
		else
			printf("Case #%d: %d\n", c++, sum - minn);
	}
}