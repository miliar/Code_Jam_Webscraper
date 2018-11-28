#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

struct tt
{
	int x, y;
};


int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	int r;
	cin >> r;
	for (int p = 1; p <= r; p++)
	{
		vector<tt> v;
		v.clear();
		tt temp;
		long long n, a, b, c, d, x0, y0, m;
		cin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;
		temp.x = x0;
		temp.y = y0;
		v.push_back(temp);
		for (int i = 1; i < n; i++)
		{
			temp.x = (temp.x * a + b) % m;
			temp.y = (temp.y * c + d) % m;
			v.push_back(temp);
		}
		long long cnt = 0;
		for (int i = 0; i < n; i++)
			for (int j = i + 1; j < n; j++)
				for (int u = j + 1; u < n; u++)
				{
					int x1, y1;
					x1 = (v[i].x + v[j].x + v[u].x) / 3;
					y1 = (v[i].y + v[j].y + v[u].y) / 3;
					if (x1 * 3 == (v[i].x + v[j].x + v[u].x) && y1 *3 == (v[i].y + v[j].y + v[u].y))
						cnt++;
				}		
		cout << "Case #" << p << ": " << cnt << endl;
	}
	return 0;
}