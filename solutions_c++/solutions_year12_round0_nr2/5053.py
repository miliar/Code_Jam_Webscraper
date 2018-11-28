#include <iostream>

#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <complex>
#include <cmath>
#include <map>
#include <numeric>
#include <set>
#include <iterator>
#include <bitset>
#include <limits>
#include <cassert>

using namespace std;

//ostream_iterator<int> spout(cout, " ");

vector<int> scores;
int N, S, P;

void parseCase(istream &inp)
{
	scores.clear();

	inp >> N >> S >> P;

	scores.push_back(0);
	for (int j = 0; j < N; ++j)
	{
		int x;
		inp >> x;
		scores.push_back(x);
	}
}

int memo[128][128];

int dp(int n, int s)
{
	if (memo[n][s] != -1)
		return memo[n][s];

	if (s > n)
		return -128;

	int v = scores[n];
	int mx = (v != 0 ? (v-1)/3+1 : 0);
	int best = (mx >= P ? 1 : 0) + dp(n-1, s);
	if (s > 0 && v >= 2 && v <= 28)
	{
		mx = (v-2)/3+2;
		best = max(best, (mx >= P ? 1 : 0) + dp(n-1,s-1));
	}

	return (memo[n][s] = best);
}

int answer()
{
	for (int x = 1; x <= N; ++x)
	for (int y = 0; y <= S; ++y)
		memo[x][y] = -1;

	return dp(N, S);
}

#ifndef ANS_NOMAIN
int main()
{
	for (int j = 1; j < 128; ++j)
		memo[0][j] = 0;
		
	int T;
	cin >> T;
	for (int caseNum = 1; caseNum <= T; ++caseNum)
	{
		parseCase(cin);
		cout << "Case #" << caseNum << ": " << answer() << endl;
	}

	return 0;
}
#endif
