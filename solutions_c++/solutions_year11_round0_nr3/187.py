#include <iostream>

using namespace std;

void work()
{
	int sx = 0, s = 0, mi = 99999999, n, i, j, k;
	cin >> n;
	for(i = 1 ; i <= n ; i++)
	{
		cin >> k;
		s += k;
		if(k < mi) mi = k;
		sx ^= k;
	}
	if(sx != 0) cout << "NO\n";
	else cout << s - mi << endl;
}

int main()
{
	int t, i;
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	cin >> t;
	for(int i = 1 ; i <= t ; i++)
	{
		cout << "Case #" << i << ": ";
		work();
	}
	return 0;
}
