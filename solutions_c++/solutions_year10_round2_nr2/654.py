#include <iostream>
#include <vector>
#include <string>
#include <math.h>
using namespace std;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int c, n, k, b, t;
	int x[60], v[60];
	cin >> c;
	for (int z = 1; z <= c; z++)
	{
		int count = 0;
		cin >> n >> k >> b >> t;
		for (int i = 0; i < n; i++)
			cin >> x[i];
		for (int i = 0; i < n; i++)
			cin >> v[i];
		int pass = 0, jump = 0, cur = n - 1;
		while (cur >= 0 && pass < k)
		{
			if (double(b - x[cur]) / v[cur] < t || fabs(double(double(b - x[cur]) / v[cur] - t)) < 1e-6)
			{
				pass++;
				count += jump;
			}
			else
				jump++;
			cur--;
		}
		if (pass < k)
			cout << "Case #" << z << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << z << ": " << count << endl;
	}
	return 0;
}
