#include <iostream>
#include <queue>
#include <memory.h>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int dp[102][102][102];
int d[] = {-1,0,1};

struct Q
{
	int i,j,k;
	Q(int a,int b,int c):i(a),j(b),k(c){}
};

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("res.txt", "w", stdout);
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc ++)
	{
		int ans = 1e9;
		int n;
		cin >> n;

		vector <pair<int,char> > arr;
		for (int i = 0; i < n; i ++)
		{
			int d;
			char c;
			cin >> c >> d;
			arr.push_back(make_pair(d,c));
		}
		for (int i =0 ; i < 101; i ++)
			for (int j = 0; j < 101; j ++)
				for (int k = 0; k < 101; k ++)
					dp[i][j][k] = 1e9;
		dp[0][1][1] = 0;
		queue <Q> q;
		q.push(Q(0,1,1));
		while (!q.empty())
		{
			Q x = q.front();
			q.pop();
			int i = x.i;
			int j = x.j;
			int k = x.k;
			if (i == n)
				continue;
			for (int r1 = -1; r1 < 2; r1 ++)
				for (int r2 = -1; r2 < 2; r2 ++)
				{
					if (j == 0 && r1 == -1 || k == 0 && r2 == -1 ||
						j == 100 && r1 == 1 || k == 100 && r2 == 1)
						continue;
					int m =0;
					if (arr[i].second == 'O' && arr[i].first == j && r1 == 0 ||
						arr[i].second == 'B' && arr[i].first == k && r2 == 0)
						m = 1;
					if ( dp[i+m][j+r1][k+r2] >dp[i][j][k]+1)
					{
						dp[i+m][j+r1][k+r2] = dp[i][j][k]+1;
						q.push(Q(i+m,j+r1,k+r2));
					}
				}
		}
	


		for (int j = 0; j < 101; j ++)
				for (int k = 0; k < 101; k ++)
					ans = min(ans,dp[n][j][k]);
		cout << "Case #" << tc <<": " << ans << endl;
	}

	return 0;
}
