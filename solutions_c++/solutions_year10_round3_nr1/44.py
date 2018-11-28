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

bool Intersect(pair<int, int> a, pair<int, int> b) {
	if (a.first > b.first) {
		return a.second < b.second;
	} else {
		return a.second > b.second;
	}
}

template <class AnswerType>
AnswerType SolveTestCase(const vector< pair<int, int> > & wires) {\
	int ans = 0;
	for (int i = 0; i < wires.size(); i++)
		for (int j = i + 1; j < wires.size(); j++) {
			ans += Intersect(wires[i], wires[j]);
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

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++) {
		int n;
		cin >> n;
		vector< pair<int, int> > wires(n);
		for (int i = 0; i < n; i++) {
			cin >> wires[i].first >> wires[i].second;
		}
		PrintAnswerToTestCase(caseNumber, SolveTestCase<int>(wires) );
	}

	return 0;
}