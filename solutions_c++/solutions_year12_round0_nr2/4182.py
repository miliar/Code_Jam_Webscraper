#include <cmath>
#include <vector>
#include <string>
#include <cstdlib>
#include <iterator>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAX_SCORE = 30;
const int MAX_POINT = 10;
const int UNDEFINED = -1;

bool possibleSurprising[MAX_SCORE + 1][MAX_POINT + 1];
bool possibleNonSurprising[MAX_SCORE + 1][MAX_POINT + 1];

#undef _GCJ_DEBUG_

void InitPossibility()
{
	for(int score = 0; score <= MAX_SCORE; score++)
	{
		fill_n(possibleSurprising[score], MAX_POINT + 1, false);
		fill_n(possibleNonSurprising[score], MAX_POINT + 1, false);
	}

	for(int first = 0; first <= MAX_POINT; first++)
	{
		for(int second = first; second <= first + 2 && second <= MAX_POINT; second++)
		{
			for(int third = second; third <= first + 2 && third <= MAX_POINT; third++)
			{
				bool surprise = second - first == 2 || third - first == 2 || third - second == 2;
				if(surprise)
				{
					possibleSurprising[first + second + third][third] = true;
				#ifdef _GCJ_DEBUG_
					cout << first << ' ' << second << ' ' << third << " S" << endl;
				#endif
				}
				else
				{
					possibleNonSurprising[first + second + third][third] = true;
				#ifdef _GCJ_DEBUG_
					cout << first << ' ' << second << ' ' << third << " N" << endl;
				#endif
				}
			}
		}
	}
}

int Solve(int n, int surprising, int leastMaxScore, vector<int> total)
{
	vector<vector<int> > dp(n + 1, vector<int>(surprising + 1, UNDEFINED));
	dp[0][0] = 0;
	for(int i = 1; i <= n; i++)
	{
		for(int nowSurprising = 0; nowSurprising <= min(i, surprising); nowSurprising++)
		{
			for(int maxScore = 0; maxScore <= MAX_POINT; maxScore++)
			{
				if(possibleNonSurprising[total[i - 1]][maxScore] && dp[i - 1][nowSurprising] != UNDEFINED)
				{
					dp[i][nowSurprising] = max(dp[i][nowSurprising], dp[i - 1][nowSurprising] + (maxScore >= leastMaxScore ? 1 : 0));
				}

				if(possibleSurprising[total[i - 1]][maxScore] && nowSurprising > 0 && dp[i - 1][nowSurprising - 1] != UNDEFINED)
				{
					dp[i][nowSurprising] = max(dp[i][nowSurprising], dp[i - 1][nowSurprising - 1] + (maxScore >= leastMaxScore ? 1 : 0));
				}
			}
		}
	}

	return dp[n][surprising];
}

int main(int argc, char * argv[])
{
	int cases;
	InitPossibility();
	freopen("in.txt", "r", stdin);
	cin >> cases;
	int n;
	int surprising;
	int leastMaxScore;
	vector<int> total;
	for(int test = 1; test <= cases; test++)
	{
		cin >> n >> surprising >> leastMaxScore;
		total.resize(n);
		std::copy_n(istream_iterator<int>(cin), n, total.begin());
		cout << "Case #" << test << ": " << Solve(n, surprising, leastMaxScore, total) << endl;
	}

	return 0;
}