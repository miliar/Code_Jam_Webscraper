#include <iostream>

using namespace std;

const int MAX_N = 54;

int x[MAX_N], v[MAX_N];

int main()
{
	int nTests;
	cin >> nTests;
	for (int run = 1; run <= nTests; ++run)
	{
		int n, k, b, t;
		cin >> n >> k >> b >> t;
		for (int i = 0; i < n; ++i)
			cin >> x[i];
		for (int i = 0; i < n; ++i)
			cin >> v[i];
		int c = 0;
		for (int i = n-1; i >= 0; --i)
			if (t * v[i] >= b - x[i])
			{
				if (k == 0) break;
				--k;
				for (int j = i+1; j < n; ++j)
					if (t * v[j] < b - x[j]) ++c;
				
			}
		cout << "Case #" << run << ": ";
		if (k > 0) cout << "IMPOSSIBLE" << endl;
		else cout << c << endl;
	}
	return 0;
}
