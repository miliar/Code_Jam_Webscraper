# include <cstdio>
# include <cmath>
# include <iostream>
using namespace std;

int main()
{
	int t, l, p, c, kk, ans, circle;
	
	freopen("B-small.in", "rt", stdin);
	freopen("B-small.out", "wt", stdout);

	for (cin >> t, circle = 1; circle <= t; circle++)
	{
		cin >> l >> p >> c;
		kk = ans = 0;

		while (l < p)
		{
			kk++;
			l *= c;
		}
		
		kk--;
		while (kk)
		{
			ans++;
			kk /= 2;
		}
		
		cout << "Case #" << circle << ": " << ans << endl;
	}
	
	fclose(stdout);
	fclose(stdin);	
	return 0;
}