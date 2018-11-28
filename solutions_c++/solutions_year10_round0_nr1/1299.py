# include <iostream>
# include <cstdio>
using namespace std;

int main()
{
	int LN[32] = {0};
	int t, i, n, k;


//	freopen("a-large.in", "rt", stdin);
//	freopen("a-large.out", "wt", stdout);
	LN[0] = 1;
	for (i = 1; i <= 30; i++) LN[i] = LN[i - 1] + LN[i - 1];
	cin >> t;
	for (i = 1; i <= t; i++)
	{
		cin >> n >> k;
		k %= LN[n];
		cout << "Case #" << i << ": ";
		if (k == LN[n] - 1) cout << "ON" << endl;
		else cout << "OFF" << endl;
	}
	
	return 0;
}