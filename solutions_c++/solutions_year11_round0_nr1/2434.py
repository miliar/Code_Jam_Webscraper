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


int Move(int pos, int nextGoal) {
	if (pos == nextGoal)
		return pos;
	if (pos > nextGoal)
		return pos - 1;
	if (pos < nextGoal)
		return pos + 1;
}

template <class AnswerType>
AnswerType SolveTestCase() {
	int n;
	cin >> n;
	vector<int> goals;
	vector<int> blue;
	vector<int> orange;
	for (int i = 0; i < n; i++) {
		string str;
		int goal;
		cin >> str >> goal;
		if (str == "O") {
			goals.push_back(goal);
			orange.push_back(goal);
		} else {
			goals.push_back(-goal);
			blue.push_back(-goal);
		}
	}
	blue.push_back(-1000);
	orange.push_back(1000);

	int bluePos = -1;
	int blueNext = 0;
	int orangePos = 1;
	int orangeNext = 0;
	int cur = 0;

	for (int t = 0; t < 100000; t++) {
		if (cur == n)
			return t;
		if (goals[cur] == bluePos) {
			blueNext++;
			cur++;
			orangePos = Move(orangePos, orange[orangeNext]);
		} else {
			bluePos = Move(bluePos, blue[blueNext]);
			if (goals[cur] == orangePos) {
				orangeNext++;
				cur++;
			} else {
				orangePos = Move(orangePos, orange[orangeNext]);
			}
		}
	}
	return -1;
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