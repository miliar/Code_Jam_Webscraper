#include <iostream>
using namespace std;

int n;
int s;
int p;

int main(void)
{
	int T;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	cin >> T;
	for (int cnmb=1; cnmb<=T; cnmb++)
	{
		cin >> n >> s >> p;
		int ans = 0;
		for (int j=1; j<=n; j++)
		{
			int a;
			cin >> a;
			if (a >= p + max(0, p-1) + max(0, p-1)) ans++;
			else if (a >= p + max(0, p-2) + max(0, p-2) && s) s--, ans++;
		}
		cout << "Case #" << cnmb << ": " << ans << "\n";
	}
	return 0;
}
