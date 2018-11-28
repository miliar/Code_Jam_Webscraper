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
	cout.precision(18);
	cout << "Case #" << caseNumber << ": " << ans << endl;
}

template <class AnswerType>
AnswerType SolveTestCase() {
	int len, s, r, t, n;
	cin >> len >> s >> r >> t >> n;
	vector<pair<int, int> > roads(n + 1);
	int sum = 0;
	for (int i = 0; i < n; i++) {
		int b, e, w;
		cin >> b >> e >> w;
		roads[i].second = e - b;
		roads[i].first = w;
		sum += roads[i].second;
	}
	roads[n].second = len - sum;
	roads[n].first = 0;
	sort(roads.begin(), roads.end());

	double ans = 0;
	double timeLeft = t;
	for (int i = 0; i < roads.size(); i++) {
		if (timeLeft * (r + roads[i].first) >= roads[i].second) {
			double z = roads[i].second / (double)(r + roads[i].first);
			ans += z;
			timeLeft -= z;
		} else if (timeLeft > 1E-9) {
			ans += timeLeft + (roads[i].second - timeLeft * (r + roads[i].first)) / (double)(roads[i].first + s);
			timeLeft = 0;
		} else {
			ans += roads[i].second / (double)(s + roads[i].first);
		}
	}

	return ans;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("small.in", "r", stdin);
	freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase<double>() );

	return 0;
}