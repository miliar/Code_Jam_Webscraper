#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

template<class AnswerType>
void PrintAnswerToTestCase(size_t caseNumber, AnswerType ans)
{
	cout << "Case #" << caseNumber << ": " << ans << endl;
}

template <class AnswerType>
AnswerType SolveTestCase(vector<int> miss, vector< vector<int> > prices) {
	int rounds = prices.size();
	int teams = 1 << rounds;
	const int INF = 1 << 28;
	vector< vector< vector<long long> > > dp(rounds + 1, vector< vector<long long> > (rounds + 1, vector<long long> ()));
	for (int i = 0; i < dp.size(); i++)
		for (int j = 0; j < dp[i].size(); j++)
			dp[i][j] = vector<long long>((1 << (rounds - i)), INF);

	for (int m = 0; m < dp[0][0].size(); m++)
		for (int j = 0; j <= miss[m]; j++)
			dp[0][j][m] = 0;

	for (int p = 1; p <= rounds; p++) {
		for (int m = 0; m < dp[p][0].size(); m++) 
			for (int w = 0; w <= rounds - p; w++) {
				dp[p][w][m] = min(dp[p - 1][w + 1][2 * m + 1] + dp[p - 1][w + 1][2 * m],
								  dp[p - 1][w][2 * m + 1] + dp[p - 1][w][2 * m] + prices[p - 1][m]);
			}
	}
	
	return dp[rounds][0][0];
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("small.in", "r", stdin);
	freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++) {
		int p;
		cin >> p;
		int teams = 1 << p;
		vector<int> miss(teams);
		for (int i = 0; i < teams; i++)
			cin >> miss[i];
		vector< vector<int> > prices(p, vector<int>() );
		for (int i = 0; i < p; i++) {
			prices[i] = vector<int> ((1 << (p - i - 1)), 0);
			for (int j = 0; j < prices[i].size(); j++)
				cin >> prices[i][j];
		}
		PrintAnswerToTestCase(caseNumber, SolveTestCase<int>(miss, prices) );
	}
	return 0;
}