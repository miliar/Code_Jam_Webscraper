#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <ctype.h>
#include <stack>
#include <queue>
#include <map>
#include <set>
using namespace std;


long long p;
vector <long long> m;
vector <vector <long long> > price;
vector <vector <long long> > need;
vector <vector <vector <long long> > > dp; // x,y, tickets

long long DP(int x, int y, int tiks)
{
	if (x == 0)
	{
		if (tiks < p-m[y])
			return -2;
		else
			return 0;
	}
	if (dp[x][y][tiks] != -1)
		return dp[x][y][tiks];
	dp[x][y][tiks] = -2;
	/// try to buy
	long long b1 = DP(x-1,2*y,tiks+1);
	long long b2 = DP(x-1,2*y+1,tiks+1);
	if (b1 >= 0 && b2 >= 0)
		dp[x][y][tiks] = b1+b2+price[x-1][y];
	/// try not to buy
	b1 = DP(x-1,2*y,tiks);
	b2 = DP(x-1,2*y+1,tiks);
	if (b1 >= 0 && b2 >= 0)
	{
		if (dp[x][y][tiks] == -2 || dp[x][y][tiks] > b1+b2)
			dp[x][y][tiks] = b1+b2;
	}

	return dp[x][y][tiks];
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int tests;
	
	cin >> tests;

	for (int t = 1; t <= tests; t ++)
	{

		cin >> p;
		long long sum = 0;
		m.resize(1 << p);
		for (int i = 0; i < m.size(); i ++)
		{
			cin >> m[i];
			sum += p-m[i];
		}
		price.resize(p);
		dp.resize(p+1);
		for (int i = 0; i < p; i ++)
		{
			price[i].resize(1 << (p-i-1));
			dp[i].assign(1 << (p-i), vector <long long> (p+1,-1));
			for (int j= 0; j < price[i].size(); j ++)
				cin >> price[i][j];
		}
		dp[p].assign(1,vector <long long> (p+1,-1));

		cout << "Case #" << t << ": " << DP(p,0,0) << endl;
	}

	return 0;
}
