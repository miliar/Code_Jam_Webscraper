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
	cerr << "Case #" << caseNumber << endl;
	cout << "Case #" << caseNumber << ": " << ans << endl;
}

template <class AnswerType>
AnswerType SolveTestCase() {
	int n;
	cin >> n;
	if (n == 0)
		return 0;
	vector<int> counts(11100, 0);
	for (int i = 0; i < n; i++) {
		int t;
		cin >> t;
		counts[t]++;
	}
	
	for (int ans = n; ans > 0; ans--) {
		vector<int> rest = counts;
		bool good = true;
		for (int i = 1; i < rest.size() && good; i++) {
			int d = rest[i] - (counts[i - 1] - (counts[i] - rest[i]));
			if (d > 0) {
				for (int h = i + 1; h < i + ans; h++)
					if (rest[h] < d) {
						good = false;
						break;
					} else {
						rest[h] -= d;
					}
			}
			rest[i] = 0;
		}
		if (good)
			return ans;
	}
	return 0;
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
		PrintAnswerToTestCase(caseNumber, SolveTestCase<int>() );

	return 0;
}