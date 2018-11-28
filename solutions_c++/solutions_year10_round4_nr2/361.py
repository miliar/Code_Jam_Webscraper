#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;
#define INF 100000000
vector<int> constraints;
vector<long long> prices;
int numTeams;
long long dp[2000][2000];


long long solve(int pos, int games)
{
	//cout << pos << " " << games << endl;
	if(pos >= prices.size())
	{
		//cout << "pos is " << pos << endl;
		int teamPos = pos - numTeams;
		//cout << "teamPos is " << teamPos << endl;
		if(games > constraints[teamPos])
			return INF;
		return 0;
	}
	
	if(dp[pos][games] != -1)
	{
		return dp[pos][games];
	}
	
	long long cost1 = prices[pos] + solve(pos*2, games) + solve(pos*2 + 1, games);
	
	long long cost2 = solve(2*pos, games+1) + solve(2*pos+1, games+1);
	
	long long x = min(cost1,cost2);
	
	//cout << pos << " " << games << " " << x << endl;
	
	dp[pos][games] = x;
	return x;

}

int main()
{
	int T;
	cin >> T;
	for(int t = 0; t < T;t++)
	{

		for(int i = 0; i < 2000;i++)
		{
			for(int j = 0; j < 2000;j++)
			{	
				dp[i][j] = -1;
			}
		}
		int p;
		cin >> p;
		constraints.clear();
		for(int i = 0; i < pow(2,p);i++)
		{
			int x;
			cin >> x;
			constraints.push_back(x);
		}
		numTeams = constraints.size();
		prices.clear();
		prices.resize(pow(2,p));
		for(int i = p-1; i >= 0;i--)
		{
			int offset = pow(2,i);
			for(int j = 0; j < pow(2,i);j++)
			{
				long long x;
				cin >> x;
				prices[offset + j] = x;
			}
		}
		
		cout << "Case #" << (t+1) << ": " << solve(1,0) << endl;

	}
}
