#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define mp make_pair
#define X first
#define Y second
typedef long long LL;
LL dp[111][111];
bool u[111][111];
const LL mod = 10007;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; cin >> t;
	for(int z = 1; z <= t; ++z)
	{
		memset(u, 0, sizeof u);
		int h, w, r;
		cin >> h >> w >> r;
		vector< pair<int, int> > a(r);
		for(int i = 0; i < r; ++i)
		{
			cin >> a[i].X >> a[i].Y;
			u[a[i].X-1][a[i].Y-1] = true;
		}
		memset(dp, 0, sizeof dp);
		dp[0][0] = 1;
		for(int i = 0; i < h; ++i)
			for(int j = 0; j < w; ++j) if(!u[i][j])
			{
				for(int k = 0; k <= 5; ++k)
					for(int l = 0; l <= 5; ++l) if(k || l)
						if(k * k + l * l == 5 && !u[i+k][j+l])
							dp[i+k][j+l] += dp[i][j],
							dp[i+k][j+l] %= mod;
			}
		cout << "Case #" << z << ": " << dp[h-1][w-1] << endl;
	}
	return 0;
}