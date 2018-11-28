#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <numeric>
using namespace std;
typedef long long LL;

static const int MOD = 10007;

LL solve(int H, int W, vector<int>& R, vector<int>& C)
{
	vector< vector<bool> > rock(H+1, vector<bool>(W+1, false));
	for(int i=0; i!=R.size(); ++i)
		rock[R[i]][C[i]] = true;

	vector< vector<LL> > dp(H+1, vector<LL>(W+1, 0));
	dp[1][1] = 1;

	for(int r=2; r<=H; ++r)
	for(int c=2; c<=W; ++c)
		if( !rock[r][c] )
			dp[r][c] = (dp[r-2][c-1] + dp[r-1][c-2]) % MOD;
	return dp[H][W];
}



int main()
{
	int NUM_CASE; cin >> NUM_CASE;
	for(int caseID=1; caseID<=NUM_CASE; ++caseID)
	{
		int H, W, R;
		cin >> H >> W >> R;
		vector<int> r(R);
		vector<int> c(R);
		for(int i=0; i!=R; ++i)
			cin >> r[i] >> c[i];

		cout << "Case #" << caseID << ": " << solve(H,W,r,c) << endl;
	}
}
