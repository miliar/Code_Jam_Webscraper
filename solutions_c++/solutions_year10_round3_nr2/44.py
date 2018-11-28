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
AnswerType SolveTestCase(int L, int P, int C) {
	int s = P / L;
	if (P % L) s++;
	int logc = 0;
	long long pow = 1;
	while (pow < s) {
		pow *= C;
		logc++;
	}
	return answers[logc];
}

vector<int> answers(41, 10000);

void Solve(int n) {
	if (answers[n] != 10000)
		return;
	for (int i = 1; i < n; i++)	{
		Solve(i);
		Solve(n - i);
		answers[n] = min(answers[n], max(answers[i], answers[n - i]) + 1);
	}
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("small.in", "r", stdin);
	freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);
	answers[0] = 0;
	answers[1] = 0;
	Solve(40);
	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++) {
		int L, P, C;
		cin >> L >> P >> C;
		PrintAnswerToTestCase(caseNumber, SolveTestCase<int>(L, P, C) );
	}
	return 0;
}