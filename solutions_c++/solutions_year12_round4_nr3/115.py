#include <iostream>
#include <algorithm>
#include <string.h>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

const int MAXN = 2048;

int n;
int x[MAXN];
int h[MAXN], hm[MAXN], hn[MAXN];

bool Work()
{
	memset(x, 0, sizeof(x));
	cin >> n;
	for (int i = 1; i <= n - 1; i ++)
		cin >> x[i];

	for (int i = 1; i <= n; i ++)
		hm[i] = 1000000000;

	memset(h, 0xff, sizeof(h));
	memset(hn, 0xff, sizeof(h));
	
	
	for (int i = 1; i <= n; i ++)
	{
		if (h[i] < 0)  h[i] = hn[i] + 1;

		if (h[x[i]] < 0)
		{
			for (int j = x[i] + 1; j <= n; j ++)
				if (h[j] >= 0)
					hn[x[i]] = max(hn[x[i]], h[i] + (int)((double)(h[j] - h[i]) / (j - i) * (x[i] - i)));

			h[x[i]] = max(hn[x[i]] + 2, min(h[i] + (x[i] - i) * 500, hm[x[i]] - 1));
		}
		
		for (int j = i + 1; j <= n; j ++)
		{
			hm[j] = min(hm[j], h[i] + (int)ceil((double)(h[x[i]] - h[i]) / (x[i] - i) * (j - i)));
			if (j != x[i] && h[j] > hm[j])  return false;
		}
	}

	for (int i = 1; i <= n; i ++)
		cout << " " << h[i];

	cout << endl;
	return true;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin.sync_with_stdio(false);
	int T;
	cin >> T;
	for (int k = 1; k <= T; k ++)
	{
		cout << "Case #" << k << ":";
		if (!Work())
			cout << " Impossible" << endl;
	}

	return 0;
}