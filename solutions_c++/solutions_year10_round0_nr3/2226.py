#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <sstream>
#include <iomanip>

using namespace std;

#define all(x) (x).begin(), (x).end()
#define for0(i,n) for (int i = 0; i < (n); ++i)
#define PB push_back
#define SS size()

typedef long long LL;

int R, K, N;
vector<int> g, lastR;
vector<LL> lastM;

LL solve()
{
	int i = 0;
	LL m = 0;
	for (int r = 0; r < R;)
	{
		if (lastR[i] != -1)
		{
			int dr = r - lastR[i];
			int dm = m - lastM[i];
			int j = (R - r) / dr;
			if (j > 0)
			{
				m += j * dm;
				r += j * dr;
				continue;
			}
		}
		
		lastR[i] = r;
		lastM[i] = m;
		int k = K;
		int j = i;
		while(g[i] <= k)
		{
			m += g[i];
			k -= g[i];
			i = (i+1)%N;
			if (i == j) break;
		}
		++r;
	}
	return m;
}

int main()
{
	int T;
	cin >> T;
	for (int c = 1; c <= T; ++c)
	{
		cin >> R >> K >> N;
		
		g = vector<int>(N, 0);
		lastR = vector<int>(N, -1);
		lastM = vector<LL>(N, -1);
		
		for0 (i, N)
			cin >> g[i];
		
		cout << "Case #" << c << ": ";
		cout << solve();
		cout << endl;
	}
}